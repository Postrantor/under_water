#! /usr/bin/env python
# -*- coding:utf-8 -*-
'''md
    [20210329]:
        创建joy2start_msg消息用来接收手柄上的按键控制电机的通电功能
    [20210328]:
        这个节点还是需要的，后期完善一下，移植到copley功能包内
        通过手柄上的一个按键来控制电机的通电断电
        在某些时候也可以用来紧急断电用
'''

# %% import
# Lib
import rospy
import time
import RPi.GPIO as RPi_GPIO
# Math
import math
# Message
from copley.msg import cmd2start_msg
# Hardware
# Tools
from bag_lib.bag_path import BagPathClass

# %% Constant
# NodeInfo
NodeName = 'Controller_StartDrive'
SubscriberNameCmdStart = 'cmd/start'
# Defain GPIO
Relay = 5  # 使用第5引脚控制继电器

# %% Class


class ControlsToMotors(BagPathClass):
    '''
        通过手柄上的一个按键来控制电机的通电断电， 在某些时候也可以用来紧急断电用
    '''
# ==================================================
#                                           Initial_Parameters
# ==================================================

    def __init__(self):
        self.inits_node()
        self.inits_parameter()

    def inits_node(self):
        # Initial Node
        rospy.init_node(NodeName, anonymous=False, log_level=rospy.INFO, disable_signals=False)
    # Advertise Subscriber
        rospy.Subscriber(SubscriberNameCmdStart, cmd2start_msg, self.callback_msg)
    # Advertise Publisher
        # 获取RPi引脚状态的方法
        # self.joy_pub = rospy.Publisher('joy_start', joy2start_msg, queue_size=1)
    # Bag
        self.bag = self.bag_path(SubscriberNameCmdStart)

    def inits_parameter(self):
        # Sample
        # self.rate = rospy.get_param('~rate', 10)
        # Msg_Subscriber
        self.rpi_host = 0
        self.copley_motor = 0
    # Msg_Publisher
        # self.control_msg =
        # self.frame_name = rospy.get_param('~frame_name', 'control_start')

        # self.feedback_msg =
        # self.frame_name = rospy.get_param('~frame_name', 'feedback_start')
    # GPIO
        RPi_GPIO.setmode(RPi_GPIO.BCM)  # mode = GPIO.getmode()
        RPi_GPIO.setwarnings(False)
        RPi_GPIO.setup(Relay, RPi_GPIO.OUT, initial=False)
# ==================================================
#                                             Callback_Msg
# ==================================================

    def callback_msg(self, msg):
        '''
        '''
        self.rpi_host = msg.rpi_host
        self.copley_motor = msg.copley_motor

        self.update_callback()
        # self.update_msg()
# ==================================================
#                                            Callback_Func
# ==================================================

    def gpio_relay(self):
        """
            set GPIO引脚
                输入: RPi_GPIO.IN
                输出: RPi_GPIO.OUT
                默认值: initial=False # State can be 0 / GPIO.LOW / False or 1 / GPIO.HIGH / True.
        """
        if self.copley_motor:
            RPi_GPIO.output(Relay, True)
            print('通电')
        else:
            RPi_GPIO.output(Relay, False)
            print('断电')

    def update_callback(self):
        self.gpio_relay()

    def bag_close(self):
        self.bag.close()
# ==================================================
#                                          Publisher_Msg
# ==================================================

    def update_msg(self, stop=False):
        # Header
        self.start_msg.header.stamp = rospy.Time.now()
        self.start_msg.header.frame_id = self.frame_name
        # self.start_msg.header.seq = self.seq
    # Start
        if stop:
            self.start_msg.angular.z = 0
            self.start_msg.linear.x = 0
        else:
            self.start_msg.angular.z = self.angular_z
            self.start_msg.linear.x = self.linear_x
    # Publish
        self.joy_pub.publish(self.start_msg)
        # self.seq += 1
    # Bag
        self.bag.write(SubscriberNameCmdStart, self.start_msg)
# ==================================================
#                                               @main
# ==================================================

    def spin(self):
        rospy.loginfo('# Start::%s::%s #', NodeName, time.asctime())
        rospy.on_shutdown(self.shutdown_node)
        rospy.spin()

    def shutdown_node(self):
        rospy.loginfo('# Stop::%s::%s #', NodeName, time.asctime())
        self.update_msg(stop=True)
        RPi_GPIO.cleanup(Relay)  # clears the pin numbering system in use.
        # self.bag_close()

# %%


def main():
    start_publisher = ControlsToMotors()
    start_publisher.spin()


if __name__ == '__main__':
    main()
