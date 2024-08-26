#! /usr/bin/env python
# -*- coding:utf-8 -*-
'''md
    [20210902]:
        为了配合实现阻抗控制算法，暂时将推拉机构的电机和钩刺机构结合起来，后面考虑将这个节点封装的更简单一些，可以更方便结合算法
        其实本身已经考虑到这一点了，但是，对于钩刺机构和推拉机构有一个初始位置的调整任务
        这个任务主要写在了手柄处，主要是手柄控制
        [issue]: 尝试接入阻抗控制算法，同时保留通过手柄对位置初始化的功能
            需要做一个状态切换，当手柄某一个按键使能的时候，自动中断阻抗控制；当某一个组合键(不能和初始化功能冲突)使能的时候开启阻抗控制；
            不过这个功能留着后面再实现吧，现在先简单试试
            不行就用单电机了
    [20210328]:
        行程和负极限这两个参数应该合并在一起
    [20210326]:
        启动前需要先清除编码器的计数，不然手柄发送的位置指令是0，会回零位
    [20201122]:
        相对于上一个版本，两个电机的启动确实更加同步了，暂时保留这种方式，如果后期需要单独控制每个电机，这种方式应该也可以
    [README]:
        接收手柄质量，控制钩刺电机(两个)、推拉电机(两个)
'''

# %% import
# Lib
import rospy
import time
# Messages
from std_msgs.msg import Float32
from copley.msg import cmd2switch_msg, ucr_msg
# Hardware
import motor_lib.Motor as Motor
# Algorithm
import algorithm_lib.PID.PID as Pid
# Tools
from tools_lib.debug_stream import DebugSteam
from bag_lib.bag_path import BagPathClass
# %% Constant
# NodeInfo
NodeName = 'Controller_SwitchDrive'
SubscriberNameCmdSwitch = 'cmd/switch'
PublisherNameControlSwitch = 'control/switch'
PublisherNameFeedbackSwitch = 'feedback/switch'
# Serial
from constant_lib.Constant_Serial import *
from constant_lib.Constant_Motor import Maxon_266761, Maxon_305474
# 负极限值
# CcwLimit_Wing = (-Maxon_305474.Stroke/2)
# CcwLimit_Sting = (-Maxon_266761.Stroke/2)
# 调试使用，由2倍改成8倍看看方向
CcwLimit_Wing = (-Maxon_305474.Stroke/10*5)
CcwLimit_Sting = (-Maxon_266761.Stroke/10*2)

# %%
class ControlsToMotors(DebugSteam,BagPathClass):
# ==================================================
#                                          Initial_Parameters
# ==================================================
    def __init__(self):
        self.inits_node()
        self.inits_Parameter()
        self.inits_Motor()
        self.inits_AlgorithmPID()
    def inits_node(self):
    # Initial Node
        rospy.init_node(NodeName, anonymous=False, log_level=rospy.INFO, disable_signals=False)
    # Advertise Subscriber
        rospy.Subscriber(SubscriberNameCmdSwitch, cmd2switch_msg, self.callback_msg)
    # Advertise Publisher
        self.control_pub = rospy.Publisher(PublisherNameControlSwitch, ucr_msg, queue_size=1)
        self.feedback_pub = rospy.Publisher(PublisherNameFeedbackSwitch, ucr_msg, queue_size=1)
    # Bag
        self.bag_control = self.bag_path(PublisherNameControlSwitch)
        self.bag_feedback = self.bag_path(PublisherNameFeedbackSwitch)
    def inits_Parameter(self):
    # Sample
        self.rate = rospy.get_param('/control/switch_drive/rate', 5)
    # Msg_Subscriber
        self.adjust_left = 0
        self.adjust_right = 0
        self.enc_wing = 0
        self.enc_sting = 0
        self.target_wing_l = 0
        self.target_wing_r = 0
        self.target_sting_l = 0
        self.target_sting_r = 0
    # Msg_Publisher
        self.control_msg = ucr_msg()
        self.frame_control = rospy.get_param('~frame_name', PublisherNameControlSwitch)
        self.target_wing_l = 0
        self.target_wing_r = 0
        self.target_sting_l = 0
        self.target_sting_r = 0

        self.feedback_msg = ucr_msg()
        self.frame_feedback = rospy.get_param('~frame_name', PublisherNameFeedbackSwitch)
        self.amp_wing_cur_l = 0
        self.amp_wing_cur_r = 0
        self.amp_sting_cur_l = 0
        self.amp_sting_cur_r = 0
        self.amp_wing_vel_l = 0
        self.amp_wing_vel_r = 0
        self.amp_sting_vel_l = 0
        self.amp_sting_vel_r = 0
        self.amp_wing_pos_l = 0
        self.amp_wing_pos_r = 0
        self.amp_sting_pos_l = 0
        self.amp_sting_pos_r = 0
    def inits_Motor(self):
        '''
            # Hardware
            设置为位置模式，需要同时指定运行的最大速度，以及位置
        '''
        # 推拉机构x2
            # 电机转动：46°，对应钩刺履带摆动14°，这个是最大摆角
            # 电机转动：58°，对应钩刺履带摆动10°，这个是最大转角
            # 蜗轮蜗杆传动比：10:1
            # 则，电机输出轴需要转动圈数：46/360*10 = 1.277(圈)
            # 则，电机的编码计数：(46/360*10) * (1000*4*23) = 117555(counts)
            # 额定转速：8330rpm
            # 减速比：23:1
            # 编码器：1000
        self.Motor_Wing = Motor.MotorClass(PortID=PortID_Wing, NodeID=0, Mode='Position', 
                                                    profile=0, pos=0, vel=Maxon_305474.Max_Vel/5, acc=500000, dec=500000)
        # 钩刺机构x2
            # 19.45°（修改35°），伸出5.5mm，总行程13.71-2mm
            # 则，电机输出轴需要转动圈数：35/360 = 0.0972222222(圈)
            # 则，电机的编码计数：(35/360) * (1000*4*128) = 49777.7777777778(counts)
            # 额定转速：8330rpm
            # 减速比：128:1
            # 编码器：1000
        self.Motor_Sting = Motor.MotorClass(PortID=PortID_Sting, NodeID=0, Mode='Position',
                                                    profile=0, pos=0, vel=Maxon_266761.Max_Vel/5, acc=500000, dec=500000)
    def inits_AlgorithmPID(self):
        '''
            # PID: 
        '''
        self.Pid_Control = Pid.AlgorithmPIDClass()
        self.Pid_Control.pid_on = rospy.get_param('~pid_on', False) # 开启PID算法/False
        self.Pid_Control.Kp = rospy.get_param('~Kp', 0.3)
        self.Pid_Control.Ki = rospy.get_param('~Ki', 1.0)
        self.Pid_Control.Kd = rospy.get_param('~Kd', 1.0)
# ==================================================
#                                           Callback_Msg
# ==================================================
    def callback_msg(self, msg):
        self.adjust_left = msg.adjust_left
        self.adjust_right = msg.adjust_right
        self.enc_wing = msg.enc_wing
        self.enc_sting = msg.enc_sting
        
        self.target_wing_l = msg.wing.motor_l
        self.target_wing_r = msg.wing.motor_r
        self.target_sting_l = msg.sting.motor_l
        self.target_sting_r = msg.sting.motor_r

        # self.update_callback()
        # self.update_msg()
# ==================================================
#                                          Callback_Func
# ==================================================
    # 这里面之后要加入算法
    def update_callback_wing(self):
    # 1. 获取反馈值
        # get feedback from amplifier
        get_all_0 = self.Motor_Wing.feedback_motor(node_id=0)
        self.amp_wing_cur_l = get_all_0['current_amp']
        self.amp_wing_vel_l = get_all_0['velocity_amp']
        self.amp_wing_pos_l = get_all_0['position_amp']
        get_all_1 = self.Motor_Wing.feedback_motor(node_id=1)
        self.amp_wing_cur_r = get_all_1['current_amp']
        self.amp_wing_vel_r = get_all_1['velocity_amp']
        self.amp_wing_pos_r = get_all_1['position_amp']
        # get feedback from other senser
        # 
    # 2. 调用PID算法，若未经过PID，则直接返回订阅指令
    # 3. 控制量
        self.Motor_Wing.control_motor_pos(self.adjust_left, self.enc_wing, CcwLimit_Wing, target=self.target_wing_l, node_id=0)
        self.Motor_Wing.control_motor_pos(self.adjust_right, self.enc_wing, CcwLimit_Wing, target=self.target_wing_r, node_id=1)
    def update_callback_sting(self):
    # 1. 获取反馈值
        # get feedback from motor
        get_all_0 = self.Motor_Sting.feedback_motor(node_id=0)
        self.amp_sting_cur_l = get_all_0['current_amp']
        self.amp_sting_vel_l = get_all_0['velocity_amp']
        self.amp_sting_pos_l = get_all_0['position_amp']
        get_all_1 = self.Motor_Sting.feedback_motor(node_id=1)
        self.amp_sting_cur_r = get_all_1['current_amp']
        self.amp_sting_vel_r = get_all_1['velocity_amp']
        self.amp_sting_pos_r = get_all_1['position_amp']
        # get feedback from other senser
        # 
    # 2.调用PID算法，若未经过PID，则直接返回订阅指令
    # 3. 控制量
        self.Motor_Sting.control_motor_pos(self.adjust_left, self.enc_sting, CcwLimit_Sting, target=self.target_sting_l, node_id=0)
        self.Motor_Sting.control_motor_pos(self.adjust_right, self.enc_sting, CcwLimit_Sting, target=self.target_sting_r, node_id=1)
    def update_callback(self):
        self.update_callback_wing()
        self.update_callback_sting()
# ==================================================
#                                          Publisher_Msg
# ==================================================
    def update_msg_control(self, stop=False):
    # Header
        self.control_msg.header.stamp = rospy.Time.now()
        self.control_msg.header.frame_id = self.frame_control
        # self.control_msg.header.seq = self.seq
    # Switch_Control
        if stop:
            self.control_msg.position.wing.motor_l = 0
            self.control_msg.position.wing.motor_r = 0
            self.control_msg.position.sting.motor_l = 0
            self.control_msg.position.sting.motor_r = 0
            return
        else:
            self.control_msg.position.wing.motor_l = self.target_wing_l
            self.control_msg.position.wing.motor_r = self.target_wing_r
            self.control_msg.position.sting.motor_l = self.target_sting_l
            self.control_msg.position.sting.motor_r = self.target_sting_r
    # Publish
        self.control_pub.publish(self.control_msg)
    # Bag
        self.bag_control.write(PublisherNameControlSwitch, self.control_msg)
    def update_msg_feedback(self, stop=False):
    # Header
        self.feedback_msg.header.stamp = rospy.Time.now()
        self.feedback_msg.header.frame_id = self.frame_feedback
        # self.feedback_msg.header.seq = self.seq
    # Switch Feedback
        if stop:
            self.feedback_msg.current.wing.motor_l = 0
            self.feedback_msg.current.wing.motor_r = 0
            self.feedback_msg.current.sting.motor_l = 0
            self.feedback_msg.current.sting.motor_r = 0
            self.feedback_msg.velocity.wing.motor_l = 0
            self.feedback_msg.velocity.wing.motor_r = 0
            self.feedback_msg.velocity.sting.motor_l = 0
            self.feedback_msg.velocity.sting.motor_r = 0
            self.feedback_msg.position.wing.motor_l = 0
            self.feedback_msg.position.wing.motor_r = 0
            self.feedback_msg.position.sting.motor_l = 0
            self.feedback_msg.position.sting.motor_r = 0
            return
        else:
            self.feedback_msg.current.wing.motor_l = self.amp_wing_cur_l
            self.feedback_msg.current.wing.motor_r = self.amp_wing_cur_r
            self.feedback_msg.current.sting.motor_l = self.amp_sting_cur_l
            self.feedback_msg.current.sting.motor_r = self.amp_sting_cur_r
            self.feedback_msg.velocity.wing.motor_l = self.amp_wing_vel_l
            self.feedback_msg.velocity.wing.motor_r = self.amp_wing_vel_r
            self.feedback_msg.velocity.sting.motor_l = self.amp_sting_vel_l
            self.feedback_msg.velocity.sting.motor_r = self.amp_sting_vel_r
            self.feedback_msg.position.wing.motor_l = self.amp_wing_pos_l
            self.feedback_msg.position.wing.motor_r = self.amp_wing_pos_r
            self.feedback_msg.position.sting.motor_l = self.amp_sting_pos_l
            self.feedback_msg.position.sting.motor_r = self.amp_sting_pos_r
    # Publish
        self.feedback_pub.publish(self.feedback_msg)
    # Bag
        self.bag_feedback.write(PublisherNameFeedbackSwitch, self.feedback_msg)
    def update_msg(self, stop=False):
        self.update_msg_control(stop)
        self.update_msg_feedback(stop=False)
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
        self.update_msg(stop=True)
        # [issue]:
        # 还要加东西，使得节点结束后，电机也立刻停止
        self.bag_close()
        rospy.sleep(1)

# %%
def main():
    controls_to_motors = ControlsToMotors()
    controls_to_motors.spin()

if __name__ == '__main__':
    main()