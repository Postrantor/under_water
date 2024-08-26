#! /usr/bin/env python
# -*- coding:utf-8 -*-
'''md
[20201125]:
    1. 发布水深传感器的数据，基本上调试好了，加入了头信息
    2. 修改了下载的ms5837的库函数，原来的函数在调用的时候，需要先初始化在检查是否可读，如果初始化失败或者不可读则退出程序
        将这两个函数直接默认执行了，即放在了类的初始化里面
    3. 修改了读取淡水深度和盐水深度的函数，原程序是声明一个全局变量传参给这个函数，修改后，直接将全局变量传入这个函数的参数，省了一步
'''
# %%
# Lib
import rospy
import time
# Math
import math
# Message
from sensor.msg import ms5837_msg
# Hardware
import ms5837_lib


class DepthPublisherNode:
    # ==================================================
    #                                                Initial
    # ==================================================
    def __init__(self):
        self.inits_node()
        self.inits_object()

    def inits_node(self):
        rospy.init_node('Sensor_Depth_Publisher')
    # Advertise Publisher
        self.depth_pub = rospy.Publisher('depth', ms5837_msg, queue_size=10)
    # Parameter
        self.rate = rospy.get_param('~rate', 10)
    # Header
        self.frame_name = 'sensor_depth'
        # self.seq = 0

    def inits_object(self):
        # Object
        self.depth = ms5837_lib.MS5837_30BA()  # Default I2C bus is 1 (Raspberry Pi 3)
        # sensor = ms5837.MS5837_30BA(0) # Specify I2C bus
        # sensor = ms5837.MS5837_02BA()
        # sensor = ms5837.MS5837_02BA(0)
        # sensor = ms5837.MS5837(model=ms5837.MS5837_MODEL_30BA, bus=0) # Specify model and bus
    # Covariance
        # self.depth_msg.orientation_covariance[0] = -1
        # self.depth_msg.angular_velocity_covariance[0] = -1
        # self.depth_msg.linear_acceleration_covariance[0] = -1


# ==================================================
#                                                Publish Node
# ==================================================

    def update_depth(self):
        self.depth.read()
        self.depth_msg = ms5837_msg()
    # Header
        self.depth_msg.header.stamp = rospy.Time.now()
        self.depth_msg.header.frame_id = self.frame_name
        # self.depth_msg.header.seq = self.seq
        # self.seq += 1
    # Pressure
        self.depth_msg.psr_atm = self.depth.pressure(ms5837_lib.UNITS_atm)  # Default is mbar (no arguments)
        self.depth_msg.psr_psi = self.depth.pressure(ms5837_lib.UNITS_psi)  # Request psi
        self.depth_msg.psr_Torr = self.depth.pressure(ms5837_lib.UNITS_Torr)
    # Temperature
        self.depth_msg.temp_C = self.depth.temperature(ms5837_lib.UNITS_Centigrade)  # Default is degrees C (no arguments)
        self.depth_msg.temp_F = self.depth.temperature(ms5837_lib.UNITS_Farenheit)  # Request Farenheit
        self.depth_msg.temp_K = self.depth.temperature(ms5837_lib.UNITS_Kelvin)
    # Depth
        self.depth_msg.depth_fresh = self.depth.depth(ms5837_lib.DENSITY_FRESHWATER)
        self.depth_msg.depth_salt = self.depth.depth(ms5837_lib.DENSITY_SALTWATER)
    # Altitude
        self.depth_msg.altitude = self.depth.altitude()
    # Publish
        self.depth_pub.publish(self.depth_msg)


# ==================================================
#                                           Main
# ==================================================

    def spin(self):
        rospy.loginfo('# Start Sensor_Depth_Publisher #')
        rate = rospy.Rate(self.rate)
        rospy.on_shutdown(self.shutdown_node)
        while not rospy.is_shutdown():
            self.update_depth()
            rate.sleep()
        rospy.spin()

    def shutdown_node(self):
        rospy.loginfo('# Stop Sensor_Depth_Publisher #')


# %%
def main():
    depth_publisher = DepthPublisherNode()
    depth_publisher.spin()


if __name__ == '__main__':
    main()
