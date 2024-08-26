#!/usr/bin/python  
# -*- coding:utf-8 -*-  

# %% import
import os, time
import rosbag
import getpass

# %% constant
BagPath = 'catkin_ws/bag'

# %% class
class BagPathClass():
    """
    根据期望的存储路径和话题名称，将对应的话题存入指定名称的bag包内
    """
    def bag_time(self):
        '''
        更具当前计算机的时间，为bag包名添加时间戳
        '''
        self.time_full = '{}{}{}{}{}'.format(time.localtime().tm_year, time.localtime().tm_mon, time.localtime().tm_mday, time.localtime().tm_hour, time.localtime().tm_min)
        self.time_day = '{}{}{}'.format(time.localtime().tm_year, time.localtime().tm_mon, time.localtime().tm_mday)
        self.time_min = '{}{}'.format(time.localtime().tm_hour, time.localtime().tm_min)

    def bag_dir(self, publisher_name):
        '''
        根据话题名称拼接路径信息，并创建目录
        '''
        # 路径拼接：获取话题名
        name = publisher_name
        for idx, target_str in enumerate(name):
            if target_str=='/':
                dir_path = name[:idx]
        # 路径拼接：获取用户名
        usr_name = getpass.getuser()
        # 路径拼接
        self.path_bag = '/home' + '/' + usr_name + '/' + BagPath + '/' + str(self.time_day) + '/' + str(self.time_min)
        self.path_topic = self.path_bag + '/' + dir_path
        # 若路径已存在则忽略
        try:
            os.makedirs(self.path_topic)
        except OSError as e:
            # print(e)
            pass # 也可以把这个写在ros日志中
        # [issue]:
        # 这里需要加一个容错，判断是否真的创建了路径，然后再给bag使用
        # 不然的话，bag使用的时候会出错
        # 判断路径参数最后是/还是没有，需要统一
        
    # @main
    def bag_path(self, publisher_name):
        '''
        主函数
        创建bag
        '''
        self.bag_time()
        self.bag_dir(publisher_name)

        path_topic = self.path_bag + '/' + publisher_name
        # print('{}_{}.bag'.format(path, self.time))
        bag = rosbag.Bag('{}_{}.bag'.format(path_topic, self.time_full), 'w')

        # 需要这个返回值，应为一个节点中可能有多个bag，还是需要区分的
        return bag