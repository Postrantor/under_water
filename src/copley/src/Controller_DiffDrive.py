#! /usr/bin/env python
# -*- coding:utf-8 -*-
'''md
    [20210413]:
        √1. 装控制箱体
        2. 关闭驱动器但是并不关闭继电器，统计一下电池的消耗
        4. urdf
        5. odom那个节点还没完
        6. 算法
        7. 考虑给VMware中的copley功能包改个名字
        8. 针对参数的问题还是需要调整的，现在这些文件里面都是获取参数，还应该要设置默认参数吧，就像imu里面那样
    [20210407]:
        √1. 回头把topic也做成常量的形式
        √2. 对于每个节点中的rosbag，添加时间戳；
            把路径也单独做一个变量吧。要不做成一个包，导入常量
            对于bag保存路径的问题，如果没有这个路径要单独创建，这个方法考虑作为一个包，导入进去，因为所有用到bag的地方都能用到
            若没有路径则自动创建路径，将bag做成一个节点，直接调用，包含了创建路径的功能
        3. rospy.sleep(1)放置的位置再好好考虑一下
        4. 对于风扇这个节点可以保留，但是还是需要将启动风扇的程序设置成开机启动；因为发现即使是静止调试程序的时候，温度都能升到50+甚至更高
        5. 节点启动的先后顺序需要确定好，对于手柄什么的没有太大关系；在RPi端启动电机时候需要注意，因为现在引入了手柄开关（控制继电器），开关没有开启的时候不能启动电机节点
        [issue]:
        Bag还不完善，其中总结点的存储路径会根据终端改变；
        目前每个结点都有单独的bag文件存储信息
        是否应该增加组包这样方便一些
        对于树莓派上的节点记录是否考虑转移到虚拟机上，可以减轻树莓派的运算压力
    [20210405]:
        [Task]:
        1. 图形可视化，3D
        2. 电脑操作界面
        √3. 数据采集
        4. 库仑计
        5. imu
        6. 算法
    [20210326]:
        [issue]: 
        - 如果之前意外中止节点，并且并没有重启驱动器，导致驱动器内部保留有内存数据，如电机编码器数据等，可能会导致当再次启动节点的时候电机出现意外的运动。
        所以需要设置当发送电机命令的有关节点意外中止的时候，一定要让电机停下来，或者保证电机复位一类的
        这里是不是需要分别考虑，驱动电机和钩刺、推拉电机不一样。因为驱动电机是速度模式，钩刺、推拉电机是位置模式
            1. 当驱动电机的时候，且处于速度模式，此时控制量是速度；当节点意外中止时，需要电机停止运动，不然会机器会和周围环境发生碰撞
            2. 当推拉、钩刺电机的时候，且处于位置模式，此时控制的是位置；当节点意外中止时，需要电机保持当前位置，并且驱动器保持工作状态
        - 钩刺机构和推拉机构是不是应该分开，刚进入调试模式的时候可能会出现归零的指令，这时候就会对另一组机构产生影响
            但是之所以将两个机构放在一起，是因为两个机构是相互配合工作的，后期加入算法的话会方便的多，不用消息机制传来传去的
        [Task]:
        - 钩刺和推拉一定要控制好行程
        - 添加位置极限以及电流极限，避免碰撞
        - 完善库仑计节点
        - 熟悉使用rosbag
        - 熟悉使用roslaunch
        - 熟悉使用rosparam
        - 学习服务、动作通讯机制

        - 将从CME软件中保存的电机信息做成程序的方式，这样就可以更进一步的脱离CME软件了；此后只有一个功能还要依赖CME软件，那就是电机的整定
    [20210319]:
        [issue]: 关于算法模块的位置，如何搭建架构
        算法模块单纯的就是算法，只要输入输出就好
        Motor电机模块是接收算法模块的输出，最终将算法的效果体现在电机上
        这样的话，可以将算法模块继承到电机模块中，在节点上只留一个输入就好，输出内置到Motor中了
        但是，有一些反馈信息不是电机模块能提供的，比如IMU等传感器的反馈信息，这些信息是通过节点的形式订阅到的
        如果按照前述方式，就要从外面订阅来，再传入到Motor内，才能供算法使用
        然而，如果换一种方式的话，将算法以及Motor模块上调至callback中，就可以和其他订阅的信息在一个水平上
        好处是，反馈信息调用的时候不用多层传入传出，保证各个模块之间参数输入输出的层级差不多
        缺点是，会有更多的内容留在callback中
        最终，还是选了下沉的方式，即只在callback中留一个接口就好，因为本身节点存在的意义就是转发信息，在callback中写太多东西不好
        其他callback中如果有较多信息，也只是不太多，暂时没有写成单独的class，不过后期可以考虑

        算法模块是最底层，怎么用算法模块是第二层，节点是第三层
        第一层是纯数学编程，继承到第二层；
        第二层被第三层调用，把参数发布出去
    
    # 
    /drive_controller
    将由编码器读数转换而来的角速度用于PID控制器来校正误差（目标角速度 - 测量角速度）
    /diffdrive_controller
                    ↓
   {lwheel_angular_vel_target  → /drive_controller → {lwheel_angular_vel_motor
    rwheel_angular_vel_target}                                          rwheel_angular_vel_motor}
                                                                        ↑
                                                    {lwheel_angular_vel_enc
                                                     rwheel_angular_vel_enc}
    # 
    wheel_angular_vel_target: 电机的角速度控制命令
    wheel_angular_vel_control: PID算法校正后电机的角速度控制命令
    wheel_angular_vel_motor: 电机的控制指令
    # 
    1.检测各端口通讯状态，在上位机软件上显示，具体在`CopleyControl.py`部分
'''

# %% import
# Lib
import rospy
import time
# Messages
from std_msgs.msg import Float32
from copley.msg import cmd2drive_msg, ucr_msg
# Hardware
import motor_lib.Motor as Motor
# Algorithm
from algorithm_lib.PID.PID import AlgorithmPIDClass
# Tools
from tools_lib.debug_stream import DebugSteam
from bag_lib.bag_path import BagPathClass
# Serial
from constant_lib.Constant_Serial import *

# %% Constant
# NodeInfo
NodeName = 'Controller_DiffDrive'
SubscriberNameCmdVel = 'cmd/vel'
PublisherNameControlDrive = 'control/drive'
PublisherNameFeedbackDrive = 'feedback/drive'


# %%
class ControlsToMotors(DebugSteam, BagPathClass):
    # ==================================================
    #                   Initial_Parameters
    # ==================================================
    def __init__(self):
        self.inits_Node()
        self.inits_Parameter()
        self.inits_Motor()
        self.inits_AlgorithmPID()

    def inits_Node(self):
        ## Initial Node
        rospy.init_node(NodeName,
                        anonymous=False,
                        log_level=rospy.INFO,
                        disable_signals=False)
        ## Advertise Subscriber
        rospy.Subscriber(SubscriberNameCmdVel, cmd2drive_msg,
                         self.callback_msg)
        ## Advertise Publisher
        self.control_pub = rospy.Publisher(PublisherNameControlDrive,
                                           ucr_msg,
                                           queue_size=1)
        self.feedback_pub = rospy.Publisher(PublisherNameFeedbackDrive,
                                            ucr_msg,
                                            queue_size=1)
        ## Bag
        self.bag_control = self.bag_path(PublisherNameControlDrive)
        self.bag_feedback = self.bag_path(PublisherNameFeedbackDrive)

    def inits_Parameter(self):
        ## Sample
        self.rate = rospy.get_param('/control/diff_drive/rate', 10)
        # 5Hz - 163 - 3
        # 7Hz - 211 - 2
        # 10Hz - 311 - 1
        ## Msg_Subscriber
        self.target_vel_l = 0
        self.target_vel_r = 0
        ## Msg_Publisher
        self.control_msg = ucr_msg()
        self.frame_control = rospy.get_param('~frame_name',
                                             PublisherNameControlDrive)
        self.target_vel_l = 0
        self.target_vel_r = 0

        self.feedback_msg = ucr_msg()
        self.frame_feedback = rospy.get_param('~frame_name',
                                              PublisherNameFeedbackDrive)
        self.amp_cur_l = 0
        self.amp_cur_r = 0
        self.amp_vel_l = 0
        self.amp_vel_r = 0
        self.amp_pos_l = 0
        self.amp_pos_r = 0
        ## Parameter
    def inits_Motor(self):
        '''
        主驱动机构x2
            * 功率：60 Watt
            * 额定转速：8050 rpm
            * 减速比：86:1
            * 编码器：1024 线
        '''
        # [issue]:
        # 加速度和减速度的大小还要进一步商榷
        self.Motor_UCR = Motor.MotorClass(PortID=PortID_UCR,
                                          NodeID=0,
                                          Mode='Speed',
                                          vel=0,
                                          acc=200000,
                                          dec=200000)

    def inits_AlgorithmPID(self):
        '''
        # PID: 
        [issue]: 
        这里虽然抽象除了算法层，但是ros的动态参数调整貌似没有起作用，下面的4个参数应该同时配置到实例中
        这个后面在改吧

        这几个参数的变量名是直接和算法里面的相关联的
        '''
        self.Control_PID = AlgorithmPIDClass()
        self.Control_PID.pid_on = rospy.get_param('~pid_on',
                                                  False)  # 开启PID算法/False
        self.Control_PID.Kp = rospy.get_param('~Kp', 0.3)
        self.Control_PID.Ki = rospy.get_param('~Ki', 1.0)
        self.Control_PID.Kd = rospy.get_param('~Kd', 1.0)

    # ==================================================
    #                       Callback_Msg
    # ==================================================
    def callback_msg(self, msg):
        self.target_vel_l = msg.drive.motor_l
        self.target_vel_r = msg.drive.motor_r

    # ==================================================
    #                      Callback_Func
    # ==================================================
    def update_callback(self):
        """
        [issue]:
        在算法应用层中，尽可能的用传参以及return的方式。少用self
        这样到底有哪些是输入，那些是输出就清楚得多
        其他情况用self，多是在一个脚本文件中
        但是，算法本身中的可调参数，比如P、I、D就保持用self，并在最上层中使用ROS的动态参数调节

        另外，控制算法打开的开关也是要改用参数传递的方式，还需要修改

        还是采用在callback中配置算法，否则的话，只能接收到当前层的电机参数，目前是一对，但是可能会同时用到4个，那就不能用了
        其次，算法还是在节点中进行实例化，因为，如果在Motor中以继承的方式使用，就会被局限于Motor中。并且，在节点中也同样不采用继承的方式，为了更好得到区分，这样也可以提高兼容性
        """
        ## 1. 获取反馈值
        # get feedback from motor
        get_all_0 = self.Motor_UCR.feedback_motor(node_id=0)
        self.amp_cur_l = get_all_0['current_amp']
        self.amp_vel_l = get_all_0['velocity_amp']
        self.amp_pos_l = get_all_0['position_amp']
        get_all_1 = self.Motor_UCR.feedback_motor(node_id=1)
        self.amp_cur_r = get_all_1['current_amp']
        self.amp_vel_r = get_all_1['velocity_amp']
        self.amp_pos_r = get_all_1['position_amp']
        # get feedback from other senser
        ## 2.调用PID算法，若未经过PID，则直接返回订阅指令
        # [issue]:
        # 因为电机在同一时刻下只能处在一个模式：位置模式、速度模式、电流模式
        # 所以不论用什么控制算法，最终控制的量只有一个，其他的量只能是约束(辅助作用)
        # self.target_vel_l = self.Control_PID.update(self.target_vel_l, self.amp_vel_l)
        # self.target_vel_r = self.Control_PID.update(self.target_vel_r, self.amp_vel_r)
        ## 3. 控制量
        self.Motor_UCR.control_motor_vel(target=self.target_vel_l, node_id=0)
        self.Motor_UCR.control_motor_vel(target=self.target_vel_r, node_id=1)

    # ==================================================
    #                     Publisher_Msg
    # ==================================================
    def update_msg_control(self, stop=False):
        ## Header
        self.control_msg.header.stamp = rospy.Time.now()
        self.control_msg.header.frame_id = self.frame_control
        # self.control_msg.header.seq = self.seq
        ## Control Velocity
        if stop:
            self.control_msg.velocity.drive.motor_l = 0
            self.control_msg.velocity.drive.motor_r = 0
            self.target_vel_l = 0
            self.target_vel_r = 0
        else:
            self.control_msg.velocity.drive.motor_l = self.target_vel_l
            self.control_msg.velocity.drive.motor_r = self.target_vel_r
        ## Publish
        self.control_pub.publish(self.control_msg)
        ## Bag
        self.bag_control.write(PublisherNameControlDrive, self.control_msg)

    def update_msg_feedback(self, stop=False):
        ## Header
        self.feedback_msg.header.stamp = rospy.Time.now()
        self.feedback_msg.header.frame_id = self.frame_feedback
        # self.feedback_msg.header.seq = self.seq
        ## Feedback Position
        if stop:
            self.feedback_msg.current.drive.motor_l = 0
            self.feedback_msg.current.drive.motor_r = 0
            self.feedback_msg.velocity.drive.motor_l = 0
            self.feedback_msg.velocity.drive.motor_r = 0
            self.feedback_msg.position.drive.motor_l = 0
            self.feedback_msg.position.drive.motor_r = 0
        else:
            self.feedback_msg.current.drive.motor_l = self.amp_cur_l
            self.feedback_msg.current.drive.motor_r = self.amp_cur_r
            self.feedback_msg.velocity.drive.motor_l = self.amp_vel_l
            self.feedback_msg.velocity.drive.motor_r = self.amp_vel_r
            self.feedback_msg.position.drive.motor_l = self.amp_pos_l
            self.feedback_msg.position.drive.motor_r = self.amp_pos_r
        ## Publish
        self.feedback_pub.publish(self.feedback_msg)
        ## Bag
        self.bag_feedback.write(PublisherNameFeedbackDrive, self.feedback_msg)

    def update_msg(self, stop=False):
        self.update_msg_control(stop)
        self.update_msg_feedback(stop=False)

    def bag_close(self):
        self.bag_control.close()
        self.bag_feedback.close()

    # ==================================================
    #                       @main
    # ==================================================
    def spin(self):
        rospy.loginfo('# Start::%s::%s #', NodeName, time.asctime())
        rate = rospy.Rate(self.rate)
        while not rospy.is_shutdown():
            self.update_callback()
            self.update_msg()
            rate.sleep()
        rospy.on_shutdown(self.shutdown)
        rospy.spin()

    def shutdown(self):
        rospy.loginfo('# Stop::%s::%s #', NodeName, time.asctime())
        # [issue]:
        # 这个顺序是不是有问题呀，在结束程序时候，还要再考虑一下
        self.update_msg(stop=True)
        self.update_callback()
        # [issue]:
        # 这里在发布控制速度为零后，应该需要再调用一下callback函数来执行一下才可以
        # 同时需要修改update中的stop，不光是对外发布的数值是0，对内执行的数值也要是0
        # 还有一些问题，在程序结束的这个过程，有一些报错需要解决
        self.bag_close()
        rospy.sleep(1)


# %%
def main():
    controls_to_motors = ControlsToMotors()
    controls_to_motors.spin()


if __name__ == '__main__':
    main()