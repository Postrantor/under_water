#! /usr/bin/env python
# -*- coding:utf-8 -*-
'''md
    # Node
        /startdrive_command
        将由/cmd_vel话题订阅到的消息发送给Host主机进行计算
        cmd_vel → /switchdrive_command → {lwheel_tangent_vel_target
                                                                    rwheel_tangent_vel_target}
    # S/P
        Subscriber:
            /cmd_vel: 从PS3手柄（或其他控制装置）接受控制指令，消息格式为Twist
        Publisher:
            /wheel_tangent_vel_target: 根据正向运动学将Twist消息转换成机器两轮的切向线速度
'''

# %% import
# Lib
import rospy
import roslib
import time
# Math
import math
# Messages
from std_msgs.msg import Int16, Float32
from geometry_msgs.msg import Quaternion, Twist
from sensor_msgs.msg import Imu, MagneticField
# from package.msg import function_msg
# Hardware
# import package.src.hardware.hardware_lib as hardware_lib

# %% constant
NodeName = 'Package_Function'

# %% class
class PackageFunctions():
    '''
        docstring
    '''
# ==================================================
#                                            Inital_Parameter
# ==================================================
    def __init__(self):
        self.inits_node()
        self.inits_parameter()
    def inits_node(self):
    # Initial Node
        rospy.init_node('Sensor_Fan_Publisher', anonymous=False, log_level=rospy.INFO, disable_signals=False)
    # Advertise Subscriber
        self.package1_sub = rospy.Subscriber('cmd_start', function1_msg, self.callback_msg)
    # Advertise Publisher
        self.package2_pub = rospy.Publisher('fan', function2_msg, queue_size=1)
    def inits_parameter(self):
    # Object
        self.fan = hardware_lib.PCA9685()
    # Msg
        self.fan_msg = function_msg()
    # Parameter
        self.rate = rospy.get_param('~rate', 1)
        self.frame_name = rospy.get_param('~frame_name', 'sensor_fan')
# ==================================================
#                                            Callback_Msg
# ==================================================
    def callback_msg(self, msg):
        self.data_1 = msg.data1
        self.data_2 = msg.data2
# ==================================================
#                                            Callback_Func
# ==================================================
    def update_callback(self):
        self.data_1 = self.data_1
        self.data_2 = self.data_2
# ==================================================
#                                            Publisher_Msg
# ==================================================
    def update_msg(self):
    # Header
        self.function_msg.header.stamp = rospy.Time.now()
        self.function_msg.header.frame_id = self.frame_name
        # self.fan_msg.header.seq = self.seq
        # self.seq += 1
    # Function
        self.function_msg.data1 = self.data_1
        self.function_msg.data2 = self.data_2
    # Publish
        self.fan_pub.publish(self.fan_msg)
# ==================================================
#                                                 @main
# ==================================================
    def spin(self):
        rospy.loginfo('# Start::%s::%s #', NodeName, rospy.Time.now())
        rate = rospy.Rate(self.rate)
        rospy.on_shutdown(self.shutdown_node)
        while not rospy.is_shutdown():
            self.update_callback()
            self.update_msg()
            rate.sleep()
        rospy.spin()

    def shutdown_node(self):
        rospy.loginfo('# Stop::%s::%s #', NodeName, rospy.Time.now())
        
# %% 
def main():
    Package = PackageFunctions()
    Package.spin()

if __name__ == '__main__':
    main()