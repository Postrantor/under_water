#! /usr/bin/env python
# -*- coding:utf-8 -*-
'''md
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
'''
# %% import
from os import write
import rosbag
import rosmsg
import time
import yaml
import getpass
import csv
# msg
from copley.msg import ucr_msg
# tool
from tools_lib.debug_stream import DebugSteam

# %% class
class ReadBag(DebugSteam):
    def print_topic(self):
        '''
        path
        header
        row
        '''
        # 拼接路径
        usr_name = getpass.getuser()
        path_01 = "202191/1518/Impedance/wing_2021911518"
        path_bag = "/home/{}/catkin_ws/bag/{}.bag".format(usr_name, path_01)
        # 获取bag中的话题信息
        bag_info = rosbag.Bag(path_bag, mode='r')
        info_dict = yaml.load(bag_info._get_yaml_info(), Loader=yaml.FullLoader)
            # {'end': 1630480726.396359, 'compression': 'none', 'topics': [{'topic': 'Impedance/wing', 'type': 'copley/ucr_msg', 'frequency': 10.4162, 'messages': 85}], 'messages': 85, 'start': 1630480718.009544, 'version': 2.0, 'types': [{'type': 'copley/ucr_msg', 'md5': '697cf9df9ce516a16d261952c472d294'}], 'indexed': True, 'path': '/home/ubuntu/catkin_ws/bag/202191/1518/Impedance/wing_2021911518.bag', 'duration': 8.386815, 'size': 21026}
        # 打印bag中的话题信息
        bag_messages = bag_info.read_messages(topics=[info_dict['topics'][0]['topic']])
        path_csv = '/home/ubuntu/catkin_ws/csv/topic_02.csv'
        bag_csv = open(path_csv,'w')
        try:
            writer = csv.writer(bag_csv)
            writer.writerow(['seq','secs','vel_l','vel_r'])
            for topic, msg, t in bag_messages:
                secs_nsecs = float("{}.{}".format(msg.header.stamp.secs, msg.header.stamp.nsecs)) - info_dict['start']
                writer.writerow([msg.header.seq, 
                                            secs_nsecs, 
                                            msg.velocity.drive.motor_l, 
                                            msg.velocity.drive.motor_r,])
        except rosbag.bag.ROSBagFormatException as error:
            error
        finally:
            bag_info.close()
            bag_csv.close()
# %%
def main():
    read_bag = ReadBag()
    read_bag.print_topic()
if __name__ == '__main__':
    main()