#! /usr/bin/env python
# -*- coding:utf-8 -*-
'''md
    # 20201125
        1. 发布水深传感器的数据，基本上调试好了，加入了头信息
        2. 修改了下载的ms5837的库函数，原来的函数在调用的时候，需要先初始化在检查是否可读，如果初始化失败或者不可读则退出程序
            将这两个函数直接默认执行了，即放在了类的初始化里面
        3. 修改了读取淡水深度和盐水深度的函数，原程序是声明一个全局变量传参给这个函数，修改后，直接将全局变量传入这个函数的参数，省了一步
'''
# %% import
# Lib
import rospy
import time
# Math
import math
import numpy as np
# Message
from sensor.msg import ms5837_msg
# Hardware
import depth_lib.ms5837 as ms5837_lib
# Tools
from bag_lib.bag_path import BagPathClass
# %% Constant
# NodeInfo
NodeName = 'Sensor_Depth_Publisher'
PublisherNameDepth = 'sensor/depth'

# %% class
class DepthPublisherNode(BagPathClass):
# ==================================================
#                                                Initial_Parameters
# ==================================================
    def __init__(self):
        self.inits_node()
        self.inits_parameter()
    def inits_node(self):
    # Initial Node
        rospy.init_node(NodeName, anonymous=False, log_level=rospy.INFO, disable_signals=False)
    # Advertise Publisher
        self.depth_pub = rospy.Publisher(PublisherNameDepth, ms5837_msg, queue_size=10)
    # Bag
        self.bag = self.bag_path(PublisherNameDepth)
    def inits_parameter(self):
    # Sample
        self.rate = rospy.get_param('/sensor/depth/rate', 5)
    # Object
        self.depth = ms5837_lib.MS5837_30BA()
        # self.depth = ms5837_lib.MS5837_02BA()
        #self.depth = ms5837_lib.MS5837(model=ms5837_lib.MS5837_MODEL_30BA, bus=0) # Specify model and bus
    # Msg_Publisher
        self.depth_msg = ms5837_msg()
        self.frame_name = rospy.get_param('/sensor/depth/frame_name', PublisherNameDepth)
# ==================================================
#                                         Algorithm_Smooth 
# ==================================================
    # 等同于MATLAB中的smooth函数，但是平滑窗口必须为奇数。
    # yy = smooth(y) smooths the data in the column vector y ..
    # The first few elements of yy are given by
    # yy(1) = y(1)
    # yy(2) = (y(1) + y(2) + y(3))/3
    # yy(3) = (y(1) + y(2) + y(3) + y(4) + y(5))/5
    # yy(4) = (y(2) + y(3) + y(4) + y(5) + y(6))/5
    # ...
    def smooth(self, a, WSZ):
        # a:原始数据，NumPy 1-D array containing the data to be smoothed
        # 必须是1-D的，如果不是，请使用 np.ravel()或者np.squeeze()转化 
        # WSZ: smoothing window size needs, which must be odd number,
        # as in the original MATLAB implementation
        out0 = np.convolve(a,np.ones(WSZ,dtype=float),'valid')/WSZ
        r = np.arange(1,WSZ-1,2)
        start = np.cumsum(a[:WSZ-1])[::2]/r
        stop = (np.cumsum(a[:-WSZ:-1])[::2]/r)[::-1]
        
        return np.concatenate(( start , out0, stop ))
    # another one，边缘处理的不好
    """
    def movingaverage(data, window_size):
        window = np.ones(int(window_size))/float(window_size)
        return np.convolve(data, window, 'same')
    """
    # another one，速度更快
    # 输出结果 不与原始数据等长，假设原数据为m，平滑步长为t，则输出数据为m-t+1
    """
    def movingaverage(data, window_size):
        cumsum_vec = np.cumsum(np.insert(data, 0, 0)) 
        ma_vec = (cumsum_vec[window_size:] - cumsum_vec[:-window_size]) / window_size
        return ma_vec
    """
# ==================================================
#                                              Callback_Func
# ==================================================
    def update_callback(self):
        self.depth.read()
    # Pressure
        self.depth_mbar = self.depth.pressure(ms5837_lib.UNITS_mbar) # Default is mbar (no arguments)
        self.depth_atm = self.depth.pressure(ms5837_lib.UNITS_atm) # Request atm
        self.depth_Pa = self.depth.pressure(ms5837_lib.UNITS_Pa) # Request Pa
    # Temperature
        self.depth_Centigrade = self.depth.temperature(ms5837_lib.UNITS_Centigrade) # Default is degrees C (no arguments)
        self.depth_Farenheit = self.depth.temperature(ms5837_lib.UNITS_Farenheit) # Request Farenheit
        self.depth_Kelvin = self.depth.temperature(ms5837_lib.UNITS_Kelvin)
    # Depth
        self.depth_FreshWater = self.depth.depth(ms5837_lib.DENSITY_FRESHWATER)
        # 下面这个就是暂时借用一下，输出一个数据，用温度做了一阶的补偿
        self.depth_SaltWater = self.depth.depth(ms5837_lib.DENSITY_SALTWATER)
    # Altitude
        self.depth_msg.altitude = self.depth.altitude()
# ==================================================
#                                           Update_Msg
# ==================================================
    def update_msg(self):
    # Header
        self.depth_msg.header.stamp = rospy.Time.now()
        self.depth_msg.header.frame_id = self.frame_name
        # self.depth_msg.header.seq = self.seq
        # self.seq += 1
    # Pressure
        self.depth_msg.psr_mbar = self.depth_mbar
        self.depth_msg.psr_atm = self.depth_atm
        self.depth_msg.psr_Pa = self.depth_Pa
    # Temperature
        self.depth_msg.temp_C = self.depth_Centigrade
        self.depth_msg.temp_F = self.depth_Farenheit
        self.depth_msg.temp_K = self.depth_Kelvin
    # Depth
        self.depth_msg.depth_fresh = self.depth_FreshWater
        self.depth_msg.depth_salt = self.depth_SaltWater
    # Altitude
        self.depth_msg.altitude = self.depth_altitude
    # Publish
        self.depth_pub.publish(self.depth_msg)
    # Bag
        self.bag.write(PublisherNameDepth, self.depth_msg)
    def bag_close(self):
        self.bag.close()
# ==================================================
#                                           @main
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
    depth_sensor = DepthPublisherNode()
    depth_sensor.spin()

if __name__ == '__main__':
    main()