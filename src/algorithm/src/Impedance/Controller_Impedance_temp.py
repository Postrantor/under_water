#! /usr/bin/env python
# -*- coding:utf-8 -*-
'''md
    [20210819]: 
        关于阻抗控制
            关于阻抗控制的算法以及原理是已经搞明白了，以及怎么应用在实际的机器人身上(主要是如何获取实际值与期望值做差，仿真中是通过建立的机器人模型获得实际值，在实际机器人中是通过实际机器人获得的实际值)
            但是，对于电机而言还不太清楚。网络上有直接用手转动电机并且能体现出“阻尼-弹簧”特性的视频，但是不太能理解是如何做到的(使用了力矩传感器吗？)
            对于应用阻抗控制，驱动机构为何会表现出“阻尼-弹簧”特性这点从理论上以及感性上都能理解
            对于如何从代码的角度实现这一功能还是隔了一层窗户纸
            从阻抗控制的控制律中得到力矩，再通过动力学模型建立`状态方程`反解出相应的状态量(位置、速度，涉及到了积分)；问题是，如何使用这两个量来控制电机
            迷惑的是，对于直流伺服电机来说有3种模式可以控制：电流模式、速度模式、位置模式，在不同的模式下可以控制的量不同，但是要如何控制两个量呢(位置、速度)。然而实际并不是这样的，得到的位置和速度量是有导数关系的，所以实际上独立的量只有一个。
            这里考虑可以尝试从位置模式和速度模式实现，如果是速度模式下，那么前面通过状态方程解算出来的速度值发送给伺服电机即可，但是这里有一个问题，对于实际的机器人来说，是有期望值的，这里期望的是机构能够达到一个指定位置，并且在该位置下的速度和加速度是零，也就是稳定状态。这点是不是不用担心...因为算出来的速度积分就是相应的位置呀，在这个速度下得到的位置就是期望的位置，这个可以从数学模型中得到很好的解释。
            换句话说，如果电机处于位置模式，需要不断的向电机发送通过状态方程解算出来的位置信息，但是这里有一个问题，就是电机每次获得的新的位置是当做下一个目标值(这里的目标值应该是与期望值区分的)发送给伺服电机，所以实际上的期望值并不是设置给电机的，而是设置给算法的，算法计算出新的目标值不断更新给电机。需要注意的是，电机处于位置模式又可以细分为2种模式，S曲线、梯形曲线，这里应该采用S曲线的方式。
        1. 尝试在速度模式下控制直流伺服电机实现阻抗控制
            这里套用的代码是手柄摇杆的变化控制主驱动电机转动的程序
            指令的发送是从手柄节点处得来的，这里需要更换成阻抗控制算法发送指令
            也就是说不需要手柄这类操作了，让阻抗控制算法取代手柄不断的循环发送指令先试试
            暂时先不给电机设置上下限位了：
            因为采用的是速度模式，最后稳定的时候得到的是速度，积分之后才是位置，虽然两者是导数关系，理论上只要控制一个量就可以了。但对于实际机构而言还是要检测实际的机构位置的，为了保险起见呀，这歌时候位置仅仅当做一个限位使用，因为不能同时控制电机的位置和速度。
        2. 尝试在位置模式下控制直流伺服电机实现阻抗控制
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
    [README]: 待更新...
        /drive_controller
        将由编码器读数转换而来的角速度用于HDK控制器来校正误差（目标角速度 - 测量角速度）
        /diffdrive_controller
                        ↓
        {lwheel_angular_vel_target  → /drive_controller → {lwheel_angular_vel_motor
        rwheel_angular_vel_target}                                          rwheel_angular_vel_motor}
                                                                            ↑
                                                        {lwheel_angular_vel_enc
                                                        rwheel_angular_vel_enc}
        # 
        wheel_angular_vel_target: 电机的角速度控制命令
        wheel_angular_vel_control: HDK算法校正后电机的角速度控制命令
        wheel_angular_vel_motor: 电机的控制指令
        # 
        1.检测各端口通讯状态，在上位机软件上显示，具体在`CopleyControl.py`部分
'''

# %% import
# Lib
import rospy
import time
# Math
from math import pi
import numpy as np
# Messages
from std_msgs.msg import Float32
from copley.msg import cmd2drive_msg, ucr_msg
# Hardware
import motor_lib.Motor as Motor
# Algorithm
# from methods_lib.impedance_control import AlgorithmImpedanceClass
from methods_lib.impedance_control_temp import AlgorithmImpedanceClass  # 去除所有的运动学建模，直接驱动电机进行测试
from methods_lib.kalman_filter import SingleStateKalmanFilter
# Tools
from tools_lib.debug_stream import DebugSteam
from bag_lib.bag_path import BagPathClass

# %% Constant
from constant_lib.Constant_Serial import *
from constant_lib.Constant_Motor import Maxon_266761, Maxon_305474, Maxon_306090
# 负极限值
CcwLimit_Wing = (-Maxon_305474.Stroke / 10 * 5)
# NodeInfo
NodeName = 'Controller_Impedance'
# [issue]: 所订阅的话题将取消，替换为阻抗控制算法
SubscriberNameCmdVel = 'cmd/vel'
PublisherNameControlDrive = 'control/drive'
PublisherNameFeedbackDrive = 'feedback/drive'

# %%


class MethodsClass(object):
    '''
        [README]:
            这里只是几个简单的函数，为了不干扰主体的可读性，将其单独放在一个类里面以供调用
            类似于文章中的一些[注]的效果。
            电机的速度、位置是通过驱动器读取编码器得到的，进一步反馈过来，给阻抗控制算法使用
            但是驱动器反馈过来的数值是以`count`为单位，而阻抗控制算法中的控制量是角度，对应单位是`rad`
            因此需要将单位进行转换，也就是这个类的作用
            主要提供两个函数`rad2count`与`count2rad`函数，可以用于位置、速度的单位转换

        :func rad2count():
        :func count2rad():
    '''
    # 定义`Counts`方便后面对其进行替换为其他电机的参数
    # 在def函数中可以通过`self.Counts`的方式进行调用
    Counts = Maxon_306090.Counts_per_Reduction  # 352256

    def rad2count(self, rad):
        """
            将角度(rad、rad/s)转换成对应的编码器(count、count/s)，考虑减速机构，让最终的输出轴具有指定的数值
            编码器位置 = K * 角位置
            编码器速度 = K * 角速度

            `2*180°` -> `2*pi` -> `Counts_per_Reduction`

            单独定义`self.Counts`可以方便替换，在`code/demo_20210829.ipynb`探究一下class里面定义的变量是否会对class里面的def产生影响
            通过`self`即可以调用在class里面定义的变量

            [注]:
                该函数对于速度与位移是通用的

            :param count: 编码器数值
            :param rad: 角度数值
        """
        count = self.Counts * (rad / (2 * pi))
        return count

    def count2rad(self, count):
        """
        将编码器(count、count/s)转换成对应的角度(rad、rad/s)
        """
        rad = (count * (2 * pi)) / self.Counts
        return rad


class ControlsToMotors(DebugSteam, BagPathClass, MethodsClass):
    # ==================================================
    #                                        Initial_Parameters
    # ==================================================
    def __init__(self):
        self.inits_Node()
        self.inits_Parameter()
        self.inits_Motor()
        self.inits_AlgImpedance()
        self.inits_AlgKalmanFilter()

    def inits_Node(self):
        # Initial Node
        rospy.init_node(NodeName, anonymous=False, log_level=rospy.INFO, disable_signals=False)
    # Advertise Subscriber
        # rospy.Subscriber(SubscriberNameCmdVel, cmd2drive_msg, self.callback_msg)
    # Advertise Publisher
        self.control_pub = rospy.Publisher(PublisherNameControlDrive, ucr_msg, queue_size=1)
        self.feedback_pub = rospy.Publisher(PublisherNameFeedbackDrive, ucr_msg, queue_size=1)
    # Bag
        self.bag_control = self.bag_path(PublisherNameControlDrive)
        self.bag_feedback = self.bag_path(PublisherNameFeedbackDrive)

    def inits_Parameter(self):
        # Sample
        self.rate = rospy.get_param('/control/diff_drive/rate', 10)
        # 5Hz - 163 - 3
        # 7Hz - 211 - 2
        # 10Hz - 311 - 1
    # Msg_Subscriber
        # self.tar_val = 0 # 55511281
        # self.tar_pos = 0 #1024*4*86
    # Msg_Publisher
        self.control_msg = ucr_msg()
        self.frame_control = rospy.get_param('~frame_name', PublisherNameControlDrive)
        self.feedback_msg = ucr_msg()
        self.frame_feedback = rospy.get_param('~frame_name', PublisherNameFeedbackDrive)
        self.amp_cur = 0
        self.amp_vel = 0
        self.amp_pos = 0
    # Parameter

    def inits_Motor(self):
        '''推拉机构
            电机转动：46°，对应钩刺履带摆动14°，这个是最大摆角
            电机转动：58°，对应钩刺履带摆动10°，这个是最大转角
            蜗轮蜗杆传动比：10:1
            则，电机输出轴需要转动圈数：46/360*10 = 1.277(圈)
            则，电机的编码计数：(46/360*10) * (1000*4*23) = 117555(counts)
            额定转速：8330rpm
            减速比：23:1
            编码器：1000
        '''
        # [issue]: 使用速度模式
        # self.Motor_Wing = Motor.MotorClass(PortID=PortID_UCR,
        #                                                                 NodeID=0,
        #                                                                 Mode='Speed',
        #                                                                 vel=0,
        #                                                                 acc=1000000,
        #                                                                 dec=1000000)
        # [issue]: 使用位置模式
        self.Motor_Wing = Motor.MotorClass(PortID=PortID_UCR,  # PortID_Wing,
                                           NodeID=0,
                                           Mode='Position',
                                           profile=0,
                                           pos=0,
                                           vel=0,  # Maxon_305474.Max_Vel,
                                           acc=0, dec=0)

    def inits_AlgImpedance(self):
        '''
            # impedance: 
            [issue]: 
            这里虽然抽象除了算法层，但是ros的动态参数调整貌似没有起作用，下面的4个参数应该同时配置到实例中
            这个后面在改吧

            这几个参数的变量名是直接和算法里面的相关联的
        '''
        self.Alg_Impedance = AlgorithmImpedanceClass()
        self.Alg_Impedance.Button = True
        # self.Alg_Impedance.C = rospy.get_param('~C', 0.25) # 为机构的不确定(摩擦)阻尼系数，实际中可取(0, 0.5)；
        # self.Alg_Impedance.alpha = rospy.get_param('~alpha', 5.0) # > 0，为常数；
        # self.Alg_Impedance.H = rospy.get_param('~H', 5.0) # > 0，为闭环动力学的惯量，可取为常数；
        # self.Alg_Impedance.varepsilon = rospy.get_param('~varepsilon', 0.1) # > 0，为小常数；

    def inits_AlgKalmanFilter(self):
        '''
            Initialise the Kalman Filter to Current
            目前这组参数还可以，用`RS232_KalmanFilter.py`程序控制电机先逐渐增速一组，再逐渐减速一组记录下电流值(详细结果查看`D:\Document\Postgraduate\CAA\prick_mechanism\code\ros\record\20210827`)
            每组速度有保持一定的时间，组之间又会逐渐变化，所以KF之后的数据需要既能看出来线性(贴合单组内的匀速)又要有渐变的过渡(组间的变化)
            Q不宜太小，过小的话确实平滑，但是偏离实际值，或许在一定场合会表现的还可以；
            R不宜过大，与Q过小问题类似；
            P与x相应不太离谱就行，主要影响收敛，即使初始不太靠谱，也还是会很快收敛的；

            :param x: Initial estimate
            :param P: Initial covariance
            :param A: No process innovation
            :param C: Measurement
            :param B: No control input
            :param Q: Process covariance
            :param R: Measurement covariance
        '''
        self.kf_current = SingleStateKalmanFilter(x=0, P=10.0, A=1.0, B=0.0, C=1.0, Q=0.005, R=1.0)
        self.kf_velocity = SingleStateKalmanFilter(x=0, P=10.0, A=1.0, B=0.0, C=1.0, Q=1.0, R=50.0)
        self.kf_velocity_tar = SingleStateKalmanFilter(x=0, P=10.0, A=1.0, B=0.0, C=1.0, Q=1.0, R=50.0)
# ==================================================
#                                           Callback_Msg
# ==================================================

    def callback_msg(self, msg):
        # [issue]: 随着订阅话题替换为阻抗控制算法，这里的回调消息也将取消；
        # 回调消息本身的用途就是将接收的话题数据进行拆分，重新分配给新的变量，使其在本函数中进行处理；
        # 这里也可以进行简单的保留，用来控制阻抗算法
        # self.adjust_left = msg.adjust_left
        # self.enc_value = msg.enc_wing
        # self.tar_val = msg.wing.motor_l
        pass
# ==================================================
#                                            Callback_Func
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

            Alg_Impedance.update([0], [1])
            :param [0]: 机器人的实际位置
            :param [1]: 机器人的实际速度
        """
    # 1. 获取反馈值
        # get feedback from motor
        feedback = self.Motor_Wing.feedback_motor(node_id=0)
        self.amp_cur = feedback['current_amp']
        self.amp_vel = feedback['velocity_amp']
        self.amp_pos = feedback['position_amp']
        # get feedback from other senser
        #
    # 2.调用算法(若未经过算法调整，则直接返回订阅指令)
        # 1. 通过`Kalman Filter`对电流值进行滤波
        self.amp_cur = self.kf_current.step(0, self.amp_cur)
        # tau_e = 30000*amp_cur_kf
        self.amp_vel = self.kf_velocity.step(0, self.amp_vel)
        # 3. 调用阻抗控制算法
        tar_pos, tar_vel, tar_acc = self.Alg_Impedance.update(self.amp_pos, self.amp_vel, tau_e=0)
        self.tar_val = tar_vel
        # 4. 对阻抗控制计算值进行KF滤波，之后再发送给电机执行指令，看看会不会平滑一些
        # tar_vel_kf = self.kf_velocity_tar.step(0, tar_vel)
    # 3. 控制量
        # [issue]: 对于速度模式来说，只需要不断发送新的速度值即可
        # 不过还是应该改成位置模式！需要修改之前的位置模式下的参数，增加最大速度限制，同时将速度指令和位置指令发送给电机
        # 但是位置模式目前存在问题，暂不使用
        # self.Motor_Wing.control_motor_vel(target=self.tar_val, node_id=0)
        self.Motor_Wing.control_motor_pos_vel(position=tar_pos, velocity=tar_vel, acceleration=1000000, node_id=0)
# ==================================================
#                                         Publisher_Msg
# ==================================================

    def update_msg_control(self, stop=False):
        '''
            :param stop: 当该节点意外或故意终止时，将通过`shutdown()`函数对驱动指令进行“停止”。(default: `stop=False`)
        '''
    # Header
        self.control_msg.header.stamp = rospy.Time.now()
        self.control_msg.header.frame_id = self.frame_control
        # self.control_msg.header.seq = self.seq
    # Control Velocity
    # [issue]: 这行是否有必要
        if stop:
            self.tar_val = 0  # stop motor's speed
        self.control_msg.velocity.drive.motor_l = self.tar_val
    # Publish
        self.control_pub.publish(self.control_msg)
    # Bag
        self.bag_control.write(PublisherNameControlDrive, self.control_msg)

    def update_msg_feedback(self, stop=False):
        '''
            :param stop: 当该节点意外或故意终止时，将通过`shutdown()`函数对驱动指令进行“停止”。(default: `stop=False`)
        '''
    # Header
        self.feedback_msg.header.stamp = rospy.Time.now()
        self.feedback_msg.header.frame_id = self.frame_feedback
        # self.feedback_msg.header.seq = self.seq
    # Feedback Position
        if stop:
            self.feedback_msg.current.drive.motor_l = 0
            self.feedback_msg.velocity.drive.motor_l = 0
            self.feedback_msg.position.drive.motor_l = 0
        else:
            self.feedback_msg.current.drive.motor_l = self.amp_cur
            self.feedback_msg.velocity.drive.motor_l = self.amp_vel
            self.feedback_msg.position.drive.motor_l = self.amp_pos
    # Publish
        self.feedback_pub.publish(self.feedback_msg)
    # Bag
        self.bag_feedback.write(PublisherNameFeedbackDrive, self.feedback_msg)

    def update_msg(self, stop=False):
        self.update_msg_control(stop)
        self.update_msg_feedback(stop)

    def bag_close(self):
        self.bag_control.close()
        self.bag_feedback.close()
# ==================================================
#                                             @main
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
        # 这个顺序是不是有问题，在结束程序时候，还要再考虑一下
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
