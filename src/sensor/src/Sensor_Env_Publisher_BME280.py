#! /usr/bin/env python
# -*- coding:utf-8 -*-
'''md
    # 20201125
        修改了下载的库文件，改为一个类，可以调用
        并修改返回类型为元组，方便赋值
'''
# %% import
# Lib
import rospy
import time
# Math
import math
# Message
from sensor.msg import bme280_msg
# Hardware
import environmental_lib.bme280 as bme280_lib
# Tools
from bag_lib.bag_path import BagPathClass
# %% Constant
# NodeInfo
NodeName = 'Sensor_Env_Publisher'
PublisherNameEnv = 'sensor/env/data_raw'

# %% Class


class EnvPublisherNode(BagPathClass):
    # ==================================================
    #                                             Initial_Parameter
    # ==================================================
    def __init__(self):
        self.inits_node()
        self.inits_parameter()

    def inits_node(self):
        rospy.init_node(NodeName, anonymous=False, log_level=rospy.INFO, disable_signals=False)
    # Advertise Publisher
        self.env_pub = rospy.Publisher(PublisherNameEnv, bme280_msg, queue_size=1)
    # Bag
        self.bag = self.bag_path(PublisherNameEnv)

    def inits_parameter(self):
        # Object
        self.env = bme280_lib.BME280()
    # Msg_publisher
        self.env_msg = bme280_msg()
    # Parameter
        self.rate = rospy.get_param('/sensor/env/rate', 2)
        self.frame_name = rospy.get_param('/sensor/env/frame_name', PublisherNameEnv)
# ==================================================
#                                           Callback_Func
# ==================================================

    def update_callback(self):
        # Data
        self.get_all = self.env.readBME280All()
    # Temperature
        self.temperature = self.get_all['temp']
    # Air Pressure
        self.pressure = self.get_all['psr']
    # Humidity
        self.humidity = self.get_all['hum']
# ==================================================
#                                           Update_Msg
# ==================================================

    def update_msg(self):
        # Header
        self.env_msg.header.stamp = rospy.Time.now()
        self.env_msg.header.frame_id = self.frame_name
        # self.env_msg.header.seq = self.seq
        # self.seq += 1
    # Temperature
        self.env_msg.temperature = self.temperature
    # Air Pressure
        self.env_msg.pressure = self.pressure
    # Humidity
        self.env_msg.humidity = self.humidity
    # Publish
        self.env_pub.publish(self.env_msg)
    # Bag
        self.bag.write(PublisherNameEnv, self.env_msg)

    def bag_close(self):
        self.bag.close()
# ==================================================
#                                              @main
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
        self.bag_close()
        rospy.sleep(1)

# %%


def main():
    env_sensor = EnvPublisherNode()
    env_sensor.spin()


if __name__ == '__main__':
    main()
