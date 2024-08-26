#! /usr/bin/env python
# -*- coding:utf-8 -*-

# %%订阅一个话题：
'''
    ROS是一个事件驱动的系统，大量使用回调函数。
    一旦一个节点订阅一个话题，每次有消息到达，相应的回调函数就会被调用，并使用接收到的消息作为它的回调参数。
'''


# %%
import rospy
from std_msgs.msg import Int32


# %% 处理接收到消息的回调函数（callback）：
# 打印消息包含的值
def callback(msg):
    print(msg.data)


# %% 初始化节点：
rospy.init_node('topic_subscriber')

# 声明该节点：
# 订阅counter话题，参数包括（话题名称，消息类型，回调函数名称）
# 在后台订阅者（subscriber）讲信息传递给roscore并尝试与话题的发布者直接建立连接
# 若话题不存在，或类型错误，将不会有任何错误提示，节点将只是等待
sub = rospy.Subscriber('counter', Int32, callback)

# 一旦订阅发生，使用rospy.spin()将程序的运行交给ROS
# 该函数只有在节点准备结束的时候才返回，这样可以避免topic_publisher.py那样的高层while循环捷径
# ROS并不是必须要接管程序的主线程
rospy.spin()


# %% 检查一切是否正常
'''
    # 首先确保发布者正在运行，并仍在counter上发布消息；在另一终端启动订阅者节点
    $ rosrun basics topic_subscriber.py
'''
