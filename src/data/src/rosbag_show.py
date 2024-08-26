#! /usr/bin/env python
# -*- coding:utf-8 -*-
'''md
    [20210902]:
        1. 该函数的前身是`rosbag_read.py`
        2. 之后就用这个函数来读取bag包中的数据并绘制简图
        3. 复杂的绘图使用csv_2_plot.py
    [20210901]:
        将读取的数据以列表的形式存储起来，考虑存储为csv文件的形式
        通过如下命令可以直接将指定的话题以CSV的格式存储起来
        `rostopic echo -b wing_2021911518.bag -p /Impedance/wing/velocity/drive > topic_1.csv`
        - [使用rostopic echo将rosbag文件转换成csv](https://blog.csdn.net/cliukai/article/details/94554350)
        - [rostopic - ROS Wiki](http://wiki.ros.org/rostopic)
    [20210414]:
        yaml.FullLoader出现问题
        `pip install --ignore-installed PyYAML`
    [README]:
        参考roswiki上有关rosbag的API

        可以通过共享文件的方式，处理数据，主要是可以使用`rosbag`
        `~/ShareFold/Postgraduate/CAA/prick_mechanism/code/_file/202194/机器人/1010_直接驱动`
'''
# %% import
import rosbag
import rosmsg
import time
import yaml
import getpass
import csv
import numpy as np
import matplotlib.pyplot as plt
# msg
from copley.msg import ucr_msg
# tool
from tools_lib.debug_stream import DebugSteam
from tools_lib.make_directory import mk_dir
# Algorithm
from methods_lib.kalman_filter import SingleStateKalmanFilter

# %% class
class ReadBag(DebugSteam):
    def __init__(self):
        self.inits_AlgKalmanFilter()
        self.msg_header_seq = []
        self.secs_nsecs = []
        self.msg_current = []
        self.msg_current_kf = []
        self.msg_position = []
        self.msg_velocity = []
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
        self.kf_current = SingleStateKalmanFilter(x=0, P=10.0, A=1.0, B=0.0, C=1.0, Q=0.5, R=1.0)
        # self.kf_velocity = SingleStateKalmanFilter(x=0, P=10.0, A=1.0, B=0.0, C=1.0, Q=1.0, R=50.0)
        # self.kf_velocity_tar = SingleStateKalmanFilter(x=0, P=10.0, A=1.0, B=0.0, C=1.0, Q=1.0, R=50.0)
    def bag_path(self):
        file_path_bag = "/home/{}/catkin_ws/bag/202195/1010/feedback/".format(getpass.getuser())
        file_path_csv = "/home/{}/catkin_ws/bag/202195/1010/feedback/".format(getpass.getuser())
        file_name = "impedance_drive_2021951010"
        path_bag = "{}{}.bag".format(file_path_bag, file_name)
        path_csv = "{}{}.csv".format(file_path_csv, file_name)
        mk_dir(file_path_csv)
        return {'bag':path_bag, 'csv':path_csv}
    def topic2csv(self, header, path_csv, path_bag):
        '''
            path_bag
            path_csv: '/home/ubuntu/catkin_ws/csv/topic_02.csv'
            header: ['seq','secs','vel_l','vel_r']
            row: [msg.header.seq, 
                    secs_nsecs, 
                    msg.velocity.drive.motor_l, 
                    msg.velocity.drive.motor_r,]
        '''
        bag_info = rosbag.Bag(path_bag, mode='r')
        info_dict = yaml.load(bag_info._get_yaml_info(), Loader=yaml.FullLoader)
            # {'end': 1630480726.396359, 'compression': 'none', 'topics': [{'topic': 'Impedance/wing', 'type': 'copley/ucr_msg', 'frequency': 10.4162, 'messages': 85}], 'messages': 85, 'start': 1630480718.009544, 'version': 2.0, 'types': [{'type': 'copley/ucr_msg', 'md5': '697cf9df9ce516a16d261952c472d294'}], 'indexed': True, 'path': '/home/ubuntu/catkin_ws/bag/202191/1518/Impedance/wing_2021911518.bag', 'duration': 8.386815, 'size': 21026}
        bag_messages = bag_info.read_messages(topics=[info_dict['topics'][0]['topic']])
        bag_csv = open(path_csv,'w')
        try:
            writer = csv.writer(bag_csv)
            writer.writerow(header)
            for topic, msg, t in bag_messages:
                secs_nsecs = float("{}.{}".format(msg.header.stamp.secs, msg.header.stamp.nsecs)) - info_dict['start']
                # 
                self.msg_header_seq.append(msg.header.seq)
                self.secs_nsecs.append(secs_nsecs)
                self.msg_current.append(msg.current.wing.motor_l)
                current_kf = self.kf_current.step(0, msg.current.wing.motor_l)
                self.msg_current_kf.append(current_kf)
                self.msg_position.append(msg.position.wing.motor_l)
                self.msg_velocity.append(msg.velocity.wing.motor_l)
                row = [msg.header.seq, 
                            secs_nsecs, 
                            msg.current.wing.motor_l, 
                            current_kf, 
                            msg.position.wing.motor_l, 
                            msg.velocity.wing.motor_l,]
                writer.writerow(row)
        except rosbag.bag.ROSBagFormatException as error:
            error
        finally:
            bag_info.close()
            bag_csv.close()
    def topic2plot(self):
        msg_header_seq = np.array(self.msg_header_seq)
        secs_nsecs = np.array(self.secs_nsecs)
        msg_current = np.array(self.msg_current)
        msg_current_kf = np.array(self.msg_current_kf)
        msg_position = np.array(self.msg_position)
        msg_velocity = np.array(self.msg_velocity)
        coeff = 1.0
        plt.figure(0, figsize=(20*coeff, 6.18*coeff))
        plt.plot(np.arange(0,len(msg_header_seq),1), msg_current, 'r', linewidth=1)
        plt.plot(np.arange(0,len(msg_header_seq),1), msg_current_kf, 'b', linewidth=1)
        labels = [r'$current$',r'$current_kf$']
        plt.legend(labels)
        plt.figure(1, figsize=(20*coeff, 6.18*coeff))
        plt.plot(np.arange(0,len(msg_header_seq),1), msg_position, 'g', linewidth=1)
        plt.plot(np.arange(0,len(msg_header_seq),1), msg_velocity, 'b', linewidth=1)
        labels = [r'$position$',r'$velocity$']
        plt.legend(labels)
        plt.show()
    def spin(self):
        path = self.bag_path()
        header = ['seq','secs','current','current_kf','position','velocity']
        self.topic2csv(header, path['csv'], path['bag'])
        self.topic2plot()

# %%
def main():
    read_bag = ReadBag()
    read_bag.spin()
if __name__ == '__main__':
    main()
# %%
