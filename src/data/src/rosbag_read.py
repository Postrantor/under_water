#! /usr/bin/env python
# -*- coding:utf-8 -*-
'''md
    参考roswiki上有关rosbag的API
    [20210414]:
        [issue]:
        yaml.FullLoader出现问题
        `pip install --ignore-installed PyYAML`
'''
# %% import
import rosbag
import time
import yaml
import getpass

# %% 拼接路径
usr_name = getpass.getuser()
time_day = '{}{}{}'.format(time.localtime().tm_year, time.localtime().tm_mon, time.localtime().tm_mday)
time_min = '2059'
topic_name = 'sensor/coulomb'
bag_name = 'data_raw_20214202059'
path_bag = '/home' + '/' + usr_name + '/' + 'catkin_ws/bag' + '/' + str(time_day) + '/' + str(time_min) + '/' + str(topic_name) + '/' + str(bag_name) + '.bag'

# %% 获取bag中的话题信息
bag_info = rosbag.Bag(path_bag)
info_dict = yaml.load(bag_info._get_yaml_info(), Loader=yaml.FullLoader)
topics = [info_dict['topics'][0]['topic']]
print(topics, type(topics))

# %% 打印bag中的话题信息
for topic, msg, t in bag_info.read_messages(topics=topics): # ['chatter', 'numbers']
    '''
        - topic: the topic of the message
        - msg: the message
        - t: time of message. The time is represented as a rospy Time object (t.secs, t.nsecs)
    '''
    print(topic, msg, t)
    bag_info.close()

# %%
