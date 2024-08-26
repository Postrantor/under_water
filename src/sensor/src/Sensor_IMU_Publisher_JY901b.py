#! /usr/bin/env python
# -*- coding:utf-8 -*-
'''md
    [20210421]:
        1. 这两个还是有参考价值的
            [Madgwick IMU Filter_baochong7032的博客-CSDN博客](https://blog.csdn.net/baochong7032/article/details/101892241)
            [imu_filter_madgwick - ROS Wiki](http://wiki.ros.org/imu_filter_madgwick?distro=noetic)
        2. 考虑完全看懂这个滤波的论文，改写程序为python，或者看懂学会cpp
            加入rosbag，至少现在是能用
    [README]:
        `rosrun imu_filter_madgwick imu_filter_node _useag:=false imu/data:=sensor/imu/data imu/data_raw:=sensor/imu/data_r
aw`
        `sudo apt install i2c-tools`
        `sudo i2cdetect -y 1`
        `sudo chmod a+rw /dev/i2c-1`
'''
# %% import
# Lib
import rospy
import time
# Math
import math
# Message
from sensor_msgs.msg import Imu, MagneticField
# Hardware
import imu_lib.jy901b as jy901b_lib
# Tools
from bag_lib.bag_path import BagPathClass

# %% Constant
# NodeInfo
NodeName = 'Sensor_IMU_Publisher'
PublisherNameIMU = 'sensor/imu/data_raw'
PublisherNameMag = 'sensor/imu/mag'

# %% Class
class ImuPublisherNode(BagPathClass):
# ==================================================
#                                                初始化
# ==================================================
    def __init__(self):
        self.inits_node()
        self.inits_parameter()
    def inits_node(self):
    # Initial Node
        rospy.init_node('Sensor_IMU_Publisher', anonymous=False, log_level=rospy.INFO, disable_signals=False)
    # Advertise Publisher
        self.imu_pub = rospy.Publisher(PublisherNameIMU, Imu, queue_size=10)
        self.mag_pub = rospy.Publisher(PublisherNameMag, MagneticField, queue_size=10)
    # Bag
        self.bag_imu = self.bag_path(PublisherNameIMU)
        self.bag_mag = self.bag_path(PublisherNameMag)
    def inits_parameter(self):
    # Sample
        # [issue]:
        # 这个需要配合硬件调整，还没完成
        self.rate = rospy.get_param('~rate', 100)
    # Object
        self.imu = jy901b_lib.JY901B()
    # Msg_Publisher
        self.imu_msg = Imu()
        self.mag_msg = MagneticField()
    # Covariance
        # self.imu_msg.orientation_covariance[0] = -1
        # self.imu_msg.angular_velocity_covariance[0] = -1
        # self.imu_msg.linear_acceleration_covariance[0] = -1
        # self.seq = 0
    # Parameter
        # Static transform between sensor and fixed frame: x, y, z, roll, pitch, yaw
        # <rosparam param='static_transform'>[0, 0, 0, 0, 0, 0]</rosparam>
        self.static_transform = rospy.get_param('/sensor/imu/static_transform', [0, 0, 0, 0, 0, 0])
        self.fixed_frame = rospy.get_param('/sensor/imu/fixed_frame', 'odom')
        self.frame_name = rospy.get_param('/sensor/imu/frame_name', 'imu')
# ==================================================
#                                             Callback_Func
# ==================================================
    def update_callback_imu(self):
        """
        docstring
        """
    # Angular Velocity(角速度)
        self.get_gyro = self.imu.get_gyro_data()
        # 从MPU6050上读到的陀螺仪数据的单位是：°/s，而ROS中处理的数据单位是：rad/s，故需要先`原始数据 / 180 * pi`
        # 之后，采集静置一段时间的陀螺仪三轴数据，计算均值作为偏差，即：
            # %   x_mean = -0.275967189131500
            # %   y_mean = -0.091677493946224
            # %   z_mean = -0.060957140016007
        # self.imu_msg.angular_velocity.x = self.get_gyro['x'] / 180 * math.pi + 0.275967189131500
        # self.imu_msg.angular_velocity.y = self.get_gyro['y'] / 180 * math.pi + 0.091677493946224
        # self.imu_msg.angular_velocity.z = self.get_gyro['z'] / 180 * math.pi + 0.060957140016007
        self.angular_vel_x = self.get_gyro['x'] / 180 * math.pi
        self.angular_vel_y = self.get_gyro['y'] / 180 * math.pi
        self.angular_vel_z = self.get_gyro['z'] / 180 * math.pi
        # self.angular_vel_cov[0] = self.gyro_data['x'] * self.gyro_data['x']
        # self.angular_vel_cov[4] = self.gyro_data['y'] * self.gyro_data['y']
        # self.angular_vel_cov[8] = self.gyro_data['z'] * self.gyro_data['z']
    # Linear Acceleration(线加速度)
        self.get_accel = self.imu.get_accel_data()
        self.linear_acc_x = self.get_accel['x']
        self.linear_acc_y = self.get_accel['y']
        self.linear_acc_z = self.get_accel['z']
        # self.linear_acc_cov[0] = self.accel_data['x'] * self.accel_data['x']
        # self.linear_acc_cov[4] = self.accel_data['y'] * self.accel_data['y']
        # self.linear_acc_cov[8] = self.accel_data['z'] * self.accel_data['z']
    # Orientation(四元数是一种姿态的表达方式，与欧拉角相比规避了“万向节锁”的问题)
        self.orientation_x = 0
        self.orientation_y = 0
        self.orientation_z = 0
        self.orientation_w = 0
        # self.orientation_cov[0] = self.imu_msg.orientation.x * self.imu_msg.orientation.x
        # self.orientation_cov[4] = self.imu_msg.orientation.y * self.imu_msg.orientation.y
        # self.orientation_cov[8] = self.imu_msg.orientation.z * self.imu_msg.orientation.z
    def update_callback_mag(self):
        """
        docstring
        """
        self.magnetic_field_x = 0
        self.magnetic_field_y = 0
        self.magnetic_field_z = 0
    def update_callback(self):
        self.update_callback_imu()
        self.update_callback_mag()
# ==================================================
#                                             Publisher_Msg
# ==================================================
    # 根据重力加速度在各个方向上的分量便能求解出物体的姿态，但是水平方向偏航角与重力加速度垂直无法求得
    # 奇怪的是，磁力计的数据给零，效果比不给要好很多
    def update_msg_imu(self):
    # Header
        self.imu_msg.header.stamp = rospy.Time.now()
        self.imu_msg.header.frame_id = self.frame_name
        # self.imu_msg.header.seq = self.seq
    # Angular Velocity(角速度)
        self.imu_msg.angular_velocity.x = self.angular_vel_x
        self.imu_msg.angular_velocity.y = self.angular_vel_y
        self.imu_msg.angular_velocity.z = self.angular_vel_z
        # self.imu_msg.angular_velocity_covariance[0] = self.angular_vel_cov[0]
        # self.imu_msg.angular_velocity_covariance[4] = self.angular_vel_cov[4]
        # self.imu_msg.angular_velocity_covariance[8] = self.angular_vel_cov[8]
    # Linear Acceleration(线加速度)
        self.imu_msg.linear_acceleration.x = self.linear_acc_x
        self.imu_msg.linear_acceleration.y = self.linear_acc_y
        self.imu_msg.linear_acceleration.z = self.linear_acc_z
        # self.imu_msg.linear_acceleration_covariance[0] = self.linear_acc_cov[0]
        # self.imu_msg.linear_acceleration_covariance[4] = self.linear_acc_cov[4]
        # self.imu_msg.linear_acceleration_covariance[8] = self.linear_acc_cov[8]
    # Orientation(四元数是一种姿态的表达方式，与欧拉角相比规避了“万向节锁”的问题)
        self.imu_msg.orientation.x = self.orientation_x
        self.imu_msg.orientation.y = self.orientation_y
        self.imu_msg.orientation.z = self.orientation_z
        self.imu_msg.orientation.w = self.orientation_w
        # self.imu_msg.orientation_covariance[0] = self.orientation_cov[0]
        # self.imu_msg.orientation_covariance[4] = self.orientation_cov[4]
        # self.imu_msg.orientation_covariance[8] = self.orientation_cov[8]
    # Publish
        self.imu_pub.publish(self.imu_msg)
        # self.seq += 1
    # Bag
        self.bag_imu.write(PublisherNameIMU, self.imu_msg)
    def update_msg_mag(self):
    # Header
        self.mag_msg.header.stamp = rospy.Time.now()
        self.mag_msg.header.frame_id = self.frame_name
        # self.mag_msg.header.seq = self.seq
        # self.seq += 1
    # Mag Data
        self.mag_msg.magnetic_field.x = self.magnetic_field_x
        self.mag_msg.magnetic_field.y = self.magnetic_field_y
        self.mag_msg.magnetic_field.z = self.magnetic_field_z
    # Publish
        self.mag_pub.publish(self.mag_msg)
    # Bag
        self.bag_mag.write(PublisherNameMag, self.mag_msg)
    def update_msg(self):
        self.update_msg_imu()
        self.update_msg_mag()
    def bag_close(self):
        self.bag_imu.close()
        self.bag_mag.close()
# ==================================================
#                                              @main
# ==================================================
    def spin(self):
        rospy.loginfo('# Start::%s::%s #', NodeName, time.asctime())
        rate = rospy.Rate(self.rate)
        while not rospy.is_shutdown():
            self.update_callback()
            self.update_msg()
            rate.sleep()
        rospy.on_shutdown(self.shutdown_node)
        rospy.spin()
    def shutdown_node(self):
        rospy.loginfo('# Stop::%s::%s #', NodeName, time.asctime())
        self.bag_close()
        rospy.sleep(1)

# %%
def main():
    imu_sensor = ImuPublisherNode()
    imu_sensor.spin()

if __name__ == '__main__':
    main()