#! /usr/bin/env python
# -*- coding:utf-8 -*-

# ‘shebang’:告诉操作系统这是一个python程序，应该被传递给python解释器
# 运行该文件需要先试用chmod添加运行权限：‘$ chmod u+x topic_publisher.py’


'''
    # 什么是话题
    话题，表示一个定义了类型的消息流。
    采用publish/subscribe的通信机制，其中如何在通信之前建立连接均由底层通讯机制处理。
    节点在发送数据到话题之前，需要：
        1. advertise（声明）话题名称和消息类型（同一话题的消息类型需相同）
        2. publish数据到该话题
        3. 订阅者向roscore发送请求，订阅该话题
        4. 该话题上所有消息都会被转发到订阅者
'''


# ’import rospy‘出现在每一个ROS Python节点中，负责导入所有会用到的基础功能
import rospy

# 导入使用的消息的定义
# 这里使用32位整数，在ROS标准消息包‘std_msgs’中有定义
# 从‘<包名>.msg’导入，这是定义存储的地方
# 因为使用了一个来自其他包的消息，需要告诉ROS的构建系统，即，在'package.xml'文件中添加一个依赖（dependency）：'<depend package="std_msgs"/>'
# 这个依赖项可以告诉ROS去哪里找到消息的定义，保证节点正常运行
from std_msgs.msg import Int32



# %% 声明一个counter话题，并且许可其他节点订阅：
# 初始化节点
rospy.init_node('topic_publisher')

# 由'Publisher'声明该节点
# 即，赋予该话题一个名字（counter），并说明该话题上发布的消息类型（Int32）
# queue_size=10参数告诉rospy只缓冲一个消息。一旦发送节点发送的速率超过接收节点接收的速率，rospy就会将queue_size之外的消息扔掉
# 在后台，发布者（publisher）将会与‘roscore’建立连接并往上发送一些消息。当另一个节点尝试订阅counter话题的时候，‘roscore’将共享它的订阅者、分享者列表。然后该节点就能使用这个列表在发布者之间以及每个话题的订阅者之间建立直接的连接。
# 使用latched参数将其标记为锁存话题，即，订阅者在完成订阅之后将会自动获取到话题上发布的最后一个消息
# pub = rospy.Publisher('map', nav_msgs/OccupancyGrid, latched=Ture)
pub = rospy.Publisher('counter', Int32, queue_size=10)



# %% 对声明的counter话题上发布消息，设定频率为2Hz：
# 首先设置速率，单位是Hz，表示发布消息的速度
rate = rospy.Rate(2)

count = 0
# 如果节点已经准备好被关闭了，则'is_shutdown()'返回一个True，反之则返回False，以此来决定是否退出while循环
while not rospy.is_shutdown():
    # 在while循环中，发布计数器当前的值，然后将计数器的值+1
    # 之后睡眠一会儿，‘rate.sleep()’的调用会让程序休眠一段时间，从而保证while循环体的执行频率是设定好的2Hz
    pub.publish(count)
    count += 1
    rate.sleep()



# %% 使用’rostopic‘检查已经发布的节点相关信息：
    '''
    # 查看rostopic支持的参数类型：-h
        $ rostopic -h
    
    # diaplay bandwidth used by topic
    # 显示消息使用的带宽
        $ rostopic bw
    
    # print messages to screen
    # 查看话题发布的消息，
    # counter为对应话题；
    # -n 5为只打印5条消息，缺省则一直打印
        $rostopic echo counter -n 5
    
    # find topics by type
    # 发现发布某种类型消息的所有话题，需要同时给出包名（std_msgs）和消息类型（Int32）
        $ rostopic find std_msgs/Int32
    
    # display publishing rate of topic
    # 显示消息发布的速率，由ctrl+c终止
        $ rostopic hz
    
    # print information about active topic
    # 查看已经被声明的话题，且返回发布者运行所在的主机（hostname）
        $ rostopic info counter
    
    # list active topics
    # 查看当前系统中有哪些可用的话题
        $ rostopic list
    
    # publish data to topic
    # 发布消息到一个话题上
    # 发布100000到counter话题上
        $ rostopic pub counter std_msgs/Int32 100000
    
    # print topic type
    # 
        $ rostopic type
        >>std_msgs/Int32
    '''