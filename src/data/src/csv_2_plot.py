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
import numpy as np
import matplotlib.pyplot as plt
# msg
from copley.msg import ucr_msg
# tool
from tools_lib.debug_stream import DebugSteam
from tools_lib.make_directory import mk_dir

# %% class
class PlotBag(DebugSteam):
    def plot_topic(self, path_csv):
        bag_csv = open(path_csv,'r')
        try:
            data = np.loadtxt(bag_csv, dtype=float, delimiter=",", skiprows=1, usecols=(1,2))
            # [numpy读取csv文件](https://blog.csdn.net/u012413551/article/details/87890989)
            cols_01 = data[:,0]
            cols_02 = data[:,1]
            self.debug_stream(cols_01, cols_02)
            plt.plot(cols_01, cols_02)
        finally:
            bag_csv.close()
    def spin(self):
        file_path_csv = "/home/{}/catkin_ws/csv/202191/1518/Impedance/".format(getpass.getuser())
        file_name = "wing_2021911518"
        path_csv = "{}{}.csv".format(file_path_csv, file_name)

        self.plot_topic(path_csv)

# %%
def main():
    plot_bag = PlotBag()
    plot_bag.spin()
if __name__ == '__main__':
    main()