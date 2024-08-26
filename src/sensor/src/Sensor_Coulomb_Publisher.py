#! /usr/bin/env python
# -*- coding:utf-8 -*-
'''md
# 20201201
    读取库仑计的数值
'''
# %% import
# Lib
import rospy
import time
# Math
import math
# Message
from sensor.msg import coulomb_msg
# Hardware
import coulomb_lib.coulomb as coulomb_lib
# Tools
from bag_lib.bag_path import BagPathClass

# %% Constant
# NodeInfo
NodeName = 'Sensor_Coulomb_Publisher'
PublisherNameCoulomb = 'sensor/coulomb/data_raw'

# %%Class


class CoulombPublisherNode(BagPathClass):
    # ==================================================
    #                                                Initial_Parameters
    # ==================================================
    def __init__(self):
        self.inits_node()
        self.inits_parameter()

    def inits_node(self):
        rospy.init_node(NodeName, anonymous=False, log_level=rospy.INFO, disable_signals=False)
    # Advertise Publisher
        self.cob_pub = rospy.Publisher(PublisherNameCoulomb, coulomb_msg, queue_size=1)
    # Bag
        self.bag = self.bag_path(PublisherNameCoulomb)

    def inits_parameter(self):
        # Object
        self.cob = coulomb_lib.CoulombClass()
    # Msg_publisher
        self.cob_msg = coulomb_msg()
    # Parameter
        self.rate = rospy.get_param('/sensor/coulomb/rate', 5)  # 这个读取的频率受串口设置的timeout影响
        self.frame_name = rospy.get_param('/sensor/coulomb/frame_name', PublisherNameCoulomb)
# ==================================================
#                                                Callback_Func
# ==================================================

    def update_callback(self):
        self.cob.update()
    # Watt
        self.voltage = self.cob.voltage()
        self.current = self.cob.current()
        self.resistance = self.cob.resistance()
        self.watt = self.cob.watt()
    # Power
        power = self.cob.power()
        self.remaining = power['remaining']
        self.consumed = power['consumed']
        self.capacity = power['capacity']
        self.percentage = power['percentage']
# ==================================================
#                                              Update_Msg
# ==================================================

    def update_msg(self):
        # Header
        self.cob_msg.header.stamp = rospy.Time.now()
        self.cob_msg.header.frame_id = self.frame_name
        # self.cob_msg.header.seq = self.seq
        # self.seq += 1
    # Watt
        self.cob_msg.watt.voltage = self.voltage
        self.cob_msg.watt.current = self.current
        self.cob_msg.watt.resistance = self.resistance
        self.cob_msg.watt.watt = self.watt
    # Power
        self.cob_msg.power.remaining = self.remaining
        self.cob_msg.power.consumed = self.consumed
        self.cob_msg.power.capacity = self.capacity
        self.cob_msg.power.percentage = self.percentage
    # Publish
        self.cob_pub.publish(self.cob_msg)
    # Bag
        self.bag.write(PublisherNameCoulomb, self.cob_msg)

    def bag_close(self):
        self.bag.close()
# ==================================================
#                                                  @main
# ==================================================

    def spin(self):
        rospy.loginfo('# Start::%s::%s #', NodeName, time.asctime())
        rate = rospy.Rate(self.rate)
        while not rospy.is_shutdown():
            self.update_callback()
            self.update_msg()
            rate.sleep()
        # [issue]:
        # 对于传感器这类节点，需要从硬件获取数据的
        # 如果提前关闭bag，之后还是调用了一步lib文件，就会产生`raise ValueError('I/O operation on closed bag')`
        # 将on_shutdown()放置在while之后进行，执行顺序就会反过来，也不会抛出异常
        rospy.on_shutdown(self.shutdown_node)
        rospy.spin()

    def shutdown_node(self):
        rospy.loginfo('# Stop::%s::%s #', NodeName, time.asctime())
        self.bag_close()
        rospy.sleep(1)

# %%


def main():
    cob_sensor = CoulombPublisherNode()
    cob_sensor.spin()


if __name__ == '__main__':
    main()
