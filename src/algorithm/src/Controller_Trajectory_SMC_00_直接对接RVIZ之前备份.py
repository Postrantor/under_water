#! /usr/bin/env python
# -*- coding:utf-8 -*-
'''README
[20220420]:在 RPi 上实现 Trajectory_SMC 算法
    - 分析，原仿真程序开出两个接口，分别为Publisher和Subscriber：
    1. 将 controller 计算的 $z_control$ Publish；
    2. 由`命令转换程序`计算左右两轮的转速；
    3. 在仿真中，真实轨迹是 controller 计算值，修改为 Subscriber 订阅机器人左右两侧电机的转速；
    4. 实际中也加一个文件，将左右两轮的转速转换成电机的 $z_center$ 再给订阅者；
    综上，需要添加一个Publisher，一个Subscriber；以及命令转换程序，将 $z_control$ -> $\dot{\theta}_{l}, \dot{\theta}_{r}$，同时可逆。
    - 实现：
    1. 原来由`Joy_2_Twist`控制，发送 $z_control$，由 `command` 转换为左右两轮的转速，发送到 `Controller_DiffDrive` 驱动电机运动；
    2. 现在由 smc 中的 controller 计算 $z_control$，再继续命令发送...
    3. 其中，`Joy_2_Twist`发送的指令格式如下，类似的 smc 计算的 $z_control$ 也要为相应的格式给 Publisher。具体为，linear.x -> $v_{control}$，angular.z -> $omega_{control}$
        ---
        linear:
        x: 0.0
        y: 0.0
        z: 0.0
        angular:
        x: 0.0
        y: 0.0
        z: -0.0
        ---
    1. 在 `odom_diffdrive` 中有订阅真实轨迹与控制轨迹的方法，将相应的真实轨迹订阅话题移植到smc中即可；
    2. 需要注意的是，话题采用的消息格式是自定义的 ucr_msg，不是 ROS 中 Twist 格式；

[20220416]:
    程序已经基本跑通了，和文章呈现的效果相同。接下来对代码进行简单重构。

[20220415]:
    之前的期望轨迹是直接指定 $q_{r}$ 可以简单得到一条匀速直线运动的轨迹，但是对于复杂的曲线就不太方便。在文章的 `IV. Simulation Result` 中有通过给出 $q_{r}$ 和 $z$ 由运动学模型计算后得到 $\dot{q}_{r}$ 的方式。这里就此对原期望轨迹函数 `reference_trajectory()` 作出更改，为了更贴合的复现原文的算法。
    需要注意，由此引发的其他量也要逐一进行核对、修改。

[README]:
    @article{chwa2004sliding,
        title={Sliding-mode tracking control of nonholonomic wheeled mobile robots in polar coordinates},
        author={Chwa, Dongkyoung},
        journal={IEEE transactions on control systems technology},
        volume={12},
        number={4},
        pages={637--644},
        year={2004},
        publisher={IEEE}
    }
'''

# %% import
# Lib
import rospy, time
# Math
from numpy import sin, cos, matrix, pi
# Algorithm
from controller_sliding import ControllerPositionClass, ControllerHeadingClass
from trajectory import TrajectoryClass
# Message
from copley.msg import cmd2drive_msg, ucr_msg
# Tools
from bag_lib.bag_path import BagPathClass
# from tools_lib.debug_stream import DebugSteam
# Hardware
import motor_lib.Motor as Motor
from constant_lib.Constant_Serial import *
from constant_lib.Constant_Motor import Maxon_306090

# %%
# NodeInfo
NodeName = 'Trajectory_SMC'
PublisherNameTrajVel = 'control/drive'
# Param
pos_type = 'posture_circle_actual'  # 'line', 'point', 'curve', 'circle', 'orign', 'initial_orign', 'posture_circle_actual'
# delta_t = 0.001  # 时间间隔
# iteration = 8000  # 迭代
# density = 100  # 图像点的密度
# save2csv = False
# save2figure = False
# Constant
# Max_Vel=549546.6 (count/s) <-> 8050 (rpm) <-> 805*pi/3 (rad/s)
# 86:1 => 9.8(rad/s) * 0.065(m) = 637(mm/s)
max_rad = Maxon_306090.Nominal_speed * (2 * pi / 60) / 86.  # 9.8
max_count = Maxon_306090.Max_Vel  # 549547
l = .2  # wheel separation distance (m)
r = .065  # wheel radius (m)
J_inv = matrix([[1., -(l / 2.)], [1., (l / 2.)]]) \
            * (1. / r) * (max_count / max_rad)
J_for = matrix([[(1. / 2.), (1. / 2.)], [-(1. / l), (1. / l)]]) \
            * (r) * (max_rad / max_count)


# %%
class Trajectory_Tracking_SMC(ControllerPositionClass, ControllerHeadingClass,
                              TrajectoryClass, BagPathClass):

    def __init__(self):
        self.inits_Node()
        self.inits_Parameter()
        self.inits_Motor()

    def inits_Node(self):
        ## Initial Node
        rospy.init_node(NodeName,
                        anonymous=False,
                        log_level=rospy.INFO,
                        disable_signals=False)
        ## Advertise Publisher
        # 这里想要发布的就不再是单纯的电机的速度或者位置了
        # 而是相应的在笛卡尔坐标系内的坐标信息
        self.traj_pub = rospy.Publisher(PublisherNameTrajVel,
                                        cmd2drive_msg,
                                        queue_size=1)
        ## Bag
        self.bag = self.bag_path(PublisherNameTrajVel)

    def inits_Parameter(self):
        ## Sample
        self.rate = rospy.get_param('traj/rate', 20)  # max = 20(Hz) = 0.05(s)
        self.time_prev = rospy.Time.now()  # 机器人的时间状态
        ## Msg_Publisher
        ## Parameters
        self.postrure_select(pos_type)
        self.q_c_prev = self.q_c
        self.q_r_prev = self.q_r

    def inits_Motor(self):
        self.Motor_UCR = Motor.MotorClass(PortID=PortID_UCR,
                                          NodeID=0,
                                          Mode='Speed',
                                          vel=0, # Maxon_306090.Max_Vel,
                                          acc=500000,
                                          dec=500000)

    # ==================================================
    #                      Callback_Msg
    # ==================================================
    def odom(self):
        '''
        $z_{c}$ 由机器人正向运动学关系计算
        $q$ 由`航位推算`计算，即对 `trajectory()` 反馈值进行积分
        $z_{c}$ 与 $q$ 由IMU组成的传感测量系统获取，才最为正确

        :return z_c: [$v_{c}$, $\omega_{c}$] 机器人质心速度
        '''
        # 在`Motor`中临时创建函数，仅反馈速度
        dot_theta_l = self.Motor_UCR.trajectory_motor(node_id=0)
        dot_theta_r = self.Motor_UCR.trajectory_motor(node_id=1)

        dot_theta = matrix([[dot_theta_l], [dot_theta_r]])
        self.z_c = J_for * dot_theta
        # print("dot_theta = {}\n".format(dot_theta)) # 550000 (count)
        print("z_c = {}\n".format(self.z_c)) # z_c = [[6.37e-01], [-2.14e-05]] (m)

        # time_curr = rospy.Time.now()
        # delta_t = (time_curr - self.time_prev).to_sec()
        # self.time_prev = time_curr
        # print("delta_t = {}".format(delta_t))

    # ==================================================
    #                      Callback_Func
    # ==================================================
    def trajectory(self, z, q_prev, delta_t):
        '''
        :param S_q:
        :param z:
        :return q:
        :return dot_q:
        '''
        rho = q_prev[0, 0]
        phi = q_prev[1, 0]
        theta = q_prev[2, 0]
        S_q = matrix([
            [cos(phi - theta), 0],
            [-(1 / rho) * sin(phi - theta), 0],
            [0, 1],
        ])  #@式(12)
        dot_q = S_q * z
        q = q_prev + dot_q * delta_t
        return q, dot_q

    def controller(self, q_c, dot_q_c, q_r, dot_q_r, delta_t):
        '''还需补姿态控制器，停止运动时校正姿态'''
        u_init = self.Position(q_c, dot_q_c, q_r, dot_q_r, delta_t)
        z_ctrl = self.z_r + u_init  # @式(21)
        return z_ctrl

    def update_callback(self):
        time_curr = rospy.Time.now()
        delta_t = (time_curr - self.time_prev).to_sec()
        self.time_prev = time_curr

        self.odom()  # --> self.z_c
        q_c, dot_q_c = self.trajectory(self.z_c, self.q_c_prev, delta_t)
        q_r, dot_q_r = self.trajectory(self.z_r, self.q_r_prev, delta_t)
        z_ctrl = self.controller(q_c, dot_q_c, q_r, dot_q_r, delta_t)

        dot_theta = J_inv * z_ctrl
        # print(dot_theta)
        self.Motor_UCR.control_motor_vel(target=dot_theta[0, 0], node_id=0)
        self.Motor_UCR.control_motor_vel(target=dot_theta[1, 0], node_id=1)

        self.q_c_prev = q_c  # 由`航位推算`反馈
        self.q_r_prev = q_r

    # ==================================================
    #                      Publisher_Msg
    # ==================================================
    def update_msg(self, stop=False):
        ## Header
        self.feedback_msg.header.stamp = rospy.Time.now()
        self.feedback_msg.header.frame_id = self.frame_feedback
        # self.feedback_msg.header.seq = self.seq
        ## Feedback Position
        if stop:
            self.feedback_msg.velocity.drive.motor_l = 0.
            self.feedback_msg.velocity.drive.motor_r = 0.
            self.feedback_msg.position.drive.motor_l = 0.
            self.feedback_msg.position.drive.motor_r = 0.
        else:
            self.feedback_msg.velocity.drive.motor_l = self.amp_vel_l
            self.feedback_msg.velocity.drive.motor_r = self.amp_vel_r
            self.feedback_msg.position.drive.motor_l = self.amp_pos_l
            self.feedback_msg.position.drive.motor_r = self.amp_pos_r
        ## Publish
        self.feedback_pub.publish(self.feedback_msg)
        ## Bag
        self.bag_feedback.write(PublisherNameTrajVel, self.feedback_msg)

    def bag_close(self):
        self.bag.close()

    # ==================================================
    #                        @main
    # ==================================================
    def spin(self):
        rospy.loginfo('# Start::%s::%s #', NodeName, time.asctime())
        rate = rospy.Rate(self.rate)
        while not rospy.is_shutdown():
            self.update_callback()
            # self.update_msg()
            # self.odom()
            rate.sleep()
        rospy.on_shutdown(self.shutdown_node)
        rospy.spin()

    def shutdown_node(self):
        rospy.loginfo('# Stop::%s::%s #', NodeName, time.asctime())
        # self.update_msg(stop=True)
        rospy.sleep(1)
        # self.bag_close()


# %% main
def main():
    trajectory = Trajectory_Tracking_SMC()
    trajectory.spin()


if __name__ == "__main__":
    main()

# %%
'''[Reference]:
@ref.[Python 列表切片应用](https://www.runoob.com/python/python-lists.html#:~:text=21-,python%20%E5%88%97%E8%A1%A8%E5%88%87%E7%89%87%E5%BA%94%E7%94%A8,-%23%20-*-%20coding%3A%20UTF-8)
'''