#! /usr/bin/env python
# -*- coding:utf-8 -*-
'''README
[README]:
'''

# %% import
# Lib
import rospy, tf, time
# Math
import math
import numpy as np
# Messages
from std_msgs.msg import Float32
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Point, Quaternion, Twist
from copley.msg import ucr_msg
# Tools
from bag_lib.bag_path import BagPathClass

# %% constant
import constant_lib

NodeName = 'Odom_Trajectory'
SubscriberControlDrive = 'control/drive'
SubscriberDesireDrive = 'desire/drive'
PublisherOdom = 'odom'


# %% class
class OdomPublisher(BagPathClass):
    ''''''

    # ==================================================
    #                     Initial_Parameters
    # ==================================================
    def __init__(self):
        self.inits_node()
        self.inits_parameter()

    def inits_node(self):
        # Initial Node
        rospy.init_node(NodeName,
                        anonymous=False,
                        log_level=rospy.INFO,
                        disable_signals=False)
        # Advertise Subscriber
        # 做两条轨迹，一个是control，一个是desire
        rospy.Subscriber(SubscriberControlDrive, ucr_msg,
                         self.control_drive_callback)
        rospy.Subscriber(SubscriberDesireDrive, ucr_msg,
                         self.desire_drive_callback)
        # Advertise Publisher
        self.odom_pub = rospy.Publisher(PublisherOdom, Odometry, queue_size=10)

    def inits_parameter(self):
        # Sample
        self.rate = rospy.get_param('/odom/rate', 20)
        # TF transform
        # TransformBroadcaster is a convenient way to send transformation updates on the "/tf" message topic.
        self.tf_broadcaster = tf.TransformBroadcaster()
        # Msg_Subscriber
        # Msg_Publisher
        # /odom不仅能表征三维空间下的任意姿态，还可以表示结果的不确定度，从而实现地上跑的、空中飞的、水里游的机器人的各种操作
        self.odom_msg = Odometry()
        self.frame_id = rospy.get_param('~frame_id', '/odom')  # 坐标系id
        # self.child_frame_id = rospy.get_param('~child_frame_id', '/base_link') # 子坐标系id
        self.child_frame_id = rospy.get_param('~child_frame_id',
                                              '/imu')  # 子坐标系id
        # self.feedback_angular_vel_enc_l = 0  # 车轮编码器的速度
        # self.feedback_angular_vel_enc_r = 0
        self.pose = {'x': 0, 'y': 0, 'th': 0}  # 机器人的位置信息
        # Time
        self.time_prev_update = rospy.Time.now()  # 机器人的时间状态

    # ==================================================
    #                     Callback_Func
    # ==================================================
    # :return: x, y, theta, v, w
    def pose_next(self, tangent_vel_l, tangent_vel_r):
        '''
        :return: x, y, theta, v, w
        '''
        velocity_l = tangent_vel_l
        velocity_r = tangent_vel_r
        # initial parameters: 机器人的位置信息、时间变化
        x = self.pose['x']
        y = self.pose['y']
        theta = self.pose['th']
        time_curr_update = rospy.Time.now()
        dt = (time_curr_update - self.time_prev_update).to_sec()
        self.time_prev_update = time_curr_update
        # if straight
        if velocity_r == velocity_l:
            v = (velocity_l + velocity_r) / 2.0
            w = 0  # w_c = 0
            x = x + v * dt * np.cos(theta)
            y = y + v * dt * np.sin(theta)
            # θ' = θ 直行，所以回转角度不变 (为零)
        # if turn(计算瞬时的回转中心)
        else:
            v = (velocity_l + velocity_r) / 2.0
            w = (velocity_r - velocity_l) / self.L
            R = (self.L / 2.0) * (velocity_l + velocity_r) / (velocity_r -
                                                              velocity_l)
            translation = np.matrix([[x - R * np.sin(theta)],
                                     [y + R * np.cos(theta)], [w * dt]])
            icc_pt = np.matrix([[R * np.sin(theta)], [-R * np.cos(theta)],
                                [theta]])
            rotation = np.matrix([[np.cos(w * dt), -np.sin(w * dt), 0],
                                  [np.sin(w * dt),
                                   np.cos(w * dt), 0], [0, 0, 1]])
            pose_next = rotation * icc_pt + translation
            # 计算位置坐标
            x = pose_next[0, 0]
            y = pose_next[1, 0]
            theta = pose_next[2, 0]

        return {'x': x, 'y': y, 'th': theta, 'v': v, 'w': w}

    # :return: x, y, theta
    def pose_update(self):
        # 1. Convert to linear velocity
        feedback_tangent_vel_enc_l = self.angularvel_2_tangentvel(
            (8050 * 1024 * 4 / 60), self.desire_angular_vel_enc_l)
        feedback_tangent_vel_enc_r = self.angularvel_2_tangentvel(
            (8050 * 1024 * 4 / 60), self.desire_angular_vel_enc_r)
        # 2. Calculate location information
        pose_next = self.pose_next(feedback_tangent_vel_enc_l,
                                   feedback_tangent_vel_enc_r)
        # 3. Publish location information by Twist() type message
        # [issue]:
        # 这个可能暂时没有用，确实计算出来了v、w，但是与返回值的pose消息中的x、y、theta是重复的
        # 这里可以选择保留发布twist，但是也没太大作用
        # cmd_vel_enc = Twist()
        # cmd_vel_enc.linear.x = pose_next['v']
        # cmd_vel_enc.angular.z = pose_next['w']
        # self.cmd_vel_enc_pub.publish(cmd_vel_enc)
        return pose_next

    # ==================================================
    #                      Publisher_Msg
    # ==================================================
    def pub_odometry(self, pose):
        # Header
        self.odom_msg.header.frame_id = self.frame_id
        self.odom_msg.child_frame_id = self.child_frame_id
        self.odom_msg.header.stamp = self.time_prev_update
        # position: 只有x、y是有用的
        self.odom_msg.pose.pose.position = Point(pose['x'], pose['y'], 0)
        # orientation: 需要构造一个合法的四元数来表征一个三维空间的旋转
        self.odom_msg.pose.pose.orientation = Quaternion(
            *tf.transformations.quaternion_from_euler(0, 0, pose['th']))
        # Publish
        self.odom_pub.publish(self.odom_msg)

    def pub_tf(self, pose):
        self.tf_broadcaster.sendTransform(
            (pose['x'], pose['y'], 0),
            tf.transformations.quaternion_from_euler(0, 0, pose['th']),
            self.time_prev_update,
            self.frame_id,
            self.child_frame_id,
        )

    def update_msg(self):
        self.pose = self.pose_update()
        self.pose['th'] = math.atan2(
            math.sin(self.pose['th']),
            math.cos(self.pose['th']))  # 重写theta，使其保持在[-pi, pi]
        # 1.构造并发布Odometry消息
        self.pub_odometry(self.pose)
        # 2.构造并广播TF消息
        self.pub_tf(self.pose)

    # ==================================================
    #                          @main
    # ==================================================
    def spin(self):
        rospy.loginfo('# Start::%s::%s #', NodeName, time.asctime())
        rate = rospy.Rate(self.rate)
        rospy.on_shutdown(self.shutdown)
        while not rospy.is_shutdown():
            self.update_msg()
            rate.sleep()
        rospy.spin()

    def shutdown(self):
        rospy.loginfo('# Stop::%s::%s #', NodeName, time.asctime())
        # self.bag_close()
        rospy.sleep(1)


# %%
def main():
    odom_publisher = OdomPublisher()
    odom_publisher.spin()


if __name__ == '__main__':
    main()