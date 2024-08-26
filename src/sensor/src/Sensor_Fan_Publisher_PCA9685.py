#! /usr/bin/env python
# -*- coding:utf-8 -*-
'''md
'''

# %% import
# Lib
import rospy
import time
# Math
import math
# Message
from sensor.msg import pca9685_msg
# Hardware
import fan_lib.pca9685 as pca9685_lib
# Tools
from bag_lib.bag_path import BagPathClass

# %% Constant
# NodeInfo
NodeName = 'Sensor_Fan_Publisher'
PublisherNameFan = 'sensor/fan'

# %% Class


class FanPublisherNode(BagPathClass):
    # ==================================================
    #                                            Inital_Parameter
    # ==================================================
    def __init__(self):
        self.inits_node()
        self.inits_parameter()

    def inits_node(self):
        # Initial Node
        rospy.init_node(NodeName, anonymous=False, log_level=rospy.INFO, disable_signals=False)
    # Advertise Publisher
        self.fan_pub = rospy.Publisher(PublisherNameFan, pca9685_msg, queue_size=1)
    # Bag
        self.bag = self.bag_path(PublisherNameFan)

    def inits_parameter(self):
        # Parameter
        self.rate = rospy.get_param('sensor/fan/rate', 1)
        self.frame_name = rospy.get_param('sensor/fan/frame_name', PublisherNameFan)
    # Object
        self.fan = pca9685_lib.PCA9685()
    # Msg_Publisher
        self.fan_msg = pca9685_msg()
# ==================================================
#                                            Callback_Func
# ==================================================

    def get_thermal(self):
        """
        一般在空气中运行的温度是50℃
        """
        file_thermal = "/sys/class/thermal/thermal_zone0/temp"
        file = open(file_thermal)
        self.temp_actual = float(file.read()) / 1000
        file.close()
        return self.temp_actual

    def fan_speed(self):
        """
        最大好像是8000rpm？！这么快的吗？
        :return pwm: int16
        """
        pwm_min = 10
        pwm_max = 100
        temp_min = 0.
        temp_max = 65.
        slope = (pwm_max - pwm_min) / (temp_max - temp_min)
        intercept = pwm_max - slope * temp_max
        if temp_min < self.temp_actual < temp_max:
            self.pwm = int(slope * (self.temp_actual - 20) + intercept)  # 除去一个室温
        else:
            self.pwm = pwm_max
        self.fan.setServoPulse(0, self.pwm)
        return self.pwm

    def update_callback(self):
        self.get_thermal()
        self.fan_speed()
# ==================================================
#                                            Publisher_Msg
# ==================================================

    def update_msg(self):
        # Header
        self.fan_msg.header.stamp = rospy.Time.now()
        self.fan_msg.header.frame_id = self.frame_name
        # self.fan_msg.header.seq = self.seq
        # self.seq += 1
    # Temperature
        self.fan_msg.temperature = self.temp_actual  # = self.get_thermal()
    # Speed
        self.fan_msg.speed = self.pwm  # = self.fan_speed()
    # Publish
        self.fan_pub.publish(self.fan_msg)
    # Bag
        self.bag.write(PublisherNameFan, self.fan_msg)

    def bag_close(self):
        self.bag.close()
# ==================================================
#                                                 @main
# ==================================================

    def spin(self):
        rospy.loginfo('# Start::%s::%s #', NodeName, time.asctime())
        rate = rospy.Rate(self.rate)
        rospy.on_shutdown(self.shutdown_node)
        while not rospy.is_shutdown():
            self.update_callback()
            self.update_msg()
            rate.sleep()
        rospy.spin()

    def shutdown_node(self):
        rospy.loginfo('# Stop::%s::%s #', NodeName, time.asctime())
        # [issue]:
        # 对传感器发布的信息需要清零吗
        # 有些传感器的信息是要作为反馈的，比如imu这个需要再考虑一下
        # 如果需要修改的话，所有的传感器节点都需要修改
        # self.update_msg(stop=True)
        # self.update_callback()
        self.bag_close()
        rospy.sleep(1)

# %%


def main():
    fan_sensor = FanPublisherNode()
    fan_sensor.spin()


if __name__ == '__main__':
    main()
