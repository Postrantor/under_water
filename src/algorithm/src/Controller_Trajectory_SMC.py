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
import rospy, time, tf
# Math
from numpy import sin, cos, matrix, pi
# Algorithm
from controller_sliding import ControllerPositionClass, ControllerHeadingClass
from trajectory import TrajectoryClass
# Message
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Point, Quaternion, Twist

# %%
# NodeInfo
NodeName = 'Trajectory_SMC'
PublisherTraj = 'odom'
# Param
pos_type = 'line'  # 'line', 'point', 'curve', 'circle', 'orign', 'initial_orign', 'posture_circle_actual'


# %% class
class Trajectory_Tracking_SMC(ControllerPositionClass, ControllerHeadingClass,
                              TrajectoryClass):
    ''''''

    def __init__(self):
        self.inits_node()
        self.inits_parameter()

    def inits_node(self):
        ## Initial Node
        rospy.init_node(NodeName,
                        anonymous=False,
                        log_level=rospy.INFO,
                        disable_signals=False)
        ## Advertise Publisher
        self.traj_pub = rospy.Publisher(PublisherTraj, Odometry, queue_size=10)

    def inits_parameter(self):
        ## Sample
        self.rate = rospy.get_param('traj/rate', 20)  # max = 20(Hz) = 0.05(s)
        self.time_prev = rospy.Time.now()  # 机器人的时间状态
        # TF transform
        self.tf_broadcaster = tf.TransformBroadcaster()
        # Msg_Publisher
        self.odom_msg = Odometry()
        self.frame_id = rospy.get_param('~frame_id', '/odom')  # 坐标系id
        # self.child_frame_id = rospy.get_param('~child_frame_id', '/base_link') # 子坐标系id
        self.child_frame_id = rospy.get_param('~child_frame_id',
                                              '/imu')  # 子坐标系id
        self.pose = {'x': 0, 'y': 0, 'th': 0}  # 机器人的位置信息
        ## Parameters
        self.postrure_select(pos_type)
        self.q_c_prev = self.q_c
        self.q_r_prev = self.q_r

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
        self.z_c = self.z_r + u_init  # @式(21)
        if self.z_c[0, 0] > .6: self.z_c[0, 0] = .6
        if self.z_c[0, 0] <= -.6: self.z_c[0, 0] = -.6

    def update(self, q_c, q_r):
        self.q_c_prev = q_c
        self.q_r_prev = q_r

    def update_callback(self):
        time_curr = rospy.Time.now()
        delta_t = (time_curr - self.time_prev).to_sec()
        self.time_prev = time_curr

        q_c, dot_q_c = self.trajectory(self.z_c, self.q_c_prev, delta_t)
        q_r, dot_q_r = self.trajectory(self.z_r, self.q_r_prev, delta_t)
        self.controller(q_c, dot_q_c, q_r, dot_q_r, delta_t)
        self.update(q_c, q_r)
        self.data_array(q_c, q_r)

    # ==================================================
    #                      Publisher_Msg
    # ==================================================
    def coordinate(self, rho, theta):
        return (rho * cos(theta)), (rho * sin(theta))

    def data_array(self, q_c, q_r):
        self.x_r, self.y_r = self.coordinate(q_r[0, 0], q_r[1, 0])
        self.x_c, self.y_c = self.coordinate(q_c[0, 0], q_c[1, 0])

    def pub_odometry(self, pose):
        # Header
        self.odom_msg.header.frame_id = self.frame_id
        self.odom_msg.child_frame_id = self.child_frame_id
        self.odom_msg.header.stamp = self.time_prev
        # position: 只有x、y是有用的
        self.odom_msg.pose.pose.position = Point(self.x_r, self.y_r, 0)
        # orientation: 需要构造一个合法的四元数来表征一个三维空间的旋转
        self.odom_msg.pose.pose.orientation = Quaternion(
            *tf.transformations.quaternion_from_euler(0, 0, 0))  # pose['th']
        # Publish
        self.odom_pub.publish(self.odom_msg)

    def pub_tf(self, pose):
        self.tf_broadcaster.sendTransform(
            (self.x_r, self.y_r, 0),
            tf.transformations.quaternion_from_euler(0, 0, 0),  # pose['th']
            self.time_prev_update,
            self.frame_id,
            self.child_frame_id,
        )

    def update_msg(self):
        self.pub_odometry(self.pose)  # 构造并发布Odometry消息
        self.pub_tf(self.pose)  # 构造并广播TF消息

    # ==================================================
    #                        @main
    # ==================================================
    def spin(self):
        rospy.loginfo('# Start::%s::%s #', NodeName, time.asctime())
        rate = rospy.Rate(self.rate)
        while not rospy.is_shutdown():
            self.update_callback()
            self.update_msg()
            rate.sleep()
        rospy.on_shutdown(self.shutdown_node)
        rospy.spin()

    def shutdown_node(self):
        rospy.loginfo('# Stop::%s::%s #', NodeName, time.asctime())
        # self.update_msg(stop=True)
        rospy.sleep(1)


# %% main
def main():
    trajectory = Trajectory_Tracking_SMC()
    trajectory.spin()


if __name__ == "__main__":
    main()
