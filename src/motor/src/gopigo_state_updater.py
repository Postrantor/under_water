#! /usr/bin/env python
# -*- coding:UTF-8 -*-

'''
    /gopigo_state_updater
    根据车轮编码器数据计算实际转动的角速度，返回给/gopigo_controller用于PID控制器
    1. 车轮编码器测量每个车轮的实际转数并估算实际角速度
    2. PID控制器将校正目标转速和实际转速之间的误差
    
    {lwheel_encs  → /gopigo_state_updater → {lwheel_angular_vel_enc  → /gopigo_controller
     rwheel_encs}                                                     rwheel_angular_vel_enc} → /diffdrive_odom
'''
'''
    lwheel_angular_vel_enc: 编码器的角速度
'''
# %%


# Messages

# %%
# 查询GoPiGo机器人的左右轮编码器，发布左右车轮的角速度




import rospy
import roslib
import math
import numpy
from std_msgs.msg import Float32
from std_msgs.msg import Int64
class WheelEncoderPublisher:
    # ==================================================
    #                                                初始化
    # ==================================================
    def __init__(self):
        rospy.init_node('gopigo_state_updater')
    # 订阅/发布编码器速度相关指令
        # 声明Subscriber，用于订阅电机的角速度，判断电机旋转方向
        # wheel_angular_vel_motor：由/gopigo_controller发送给电机的命令，是[0, 100]的PWM值，但是包含了正负号
        # return wheel_dir（旋转方向）
        self.lwheel_angular_vel_motor_sub = rospy.Subscriber('lwheel_angular_vel_motor', Float32, self.lwheel_angular_vel_motor_callback)
        self.rwheel_angular_vel_motor_sub = rospy.Subscriber('rwheel_angular_vel_motor', Float32, self.rwheel_angular_vel_motor_callback)
        # wheel_enc：由hall_encoder_left/right.py读取编码器的数值，将其发送，是[负无穷, 正无穷]的整数
        # return self.lwheel_enc（仅返回编码器的数值）
        self.lwheel_enc_sub = rospy.Subscriber('lwheel_enc', Int64, self.lwheel_enc_callback)
        self.rwheel_enc_sub = rospy.Subscriber('rwheel_enc', Int64, self.rwheel_enc_callback)
        # 声明Publisher，用于发布编码器的角速度
        self.lwheel_angular_vel_enc_pub = rospy.Publisher('lwheel_angular_vel_enc', Float32, queue_size=10)
        self.rwheel_angular_vel_enc_pub = rospy.Publisher('rwheel_angular_vel_enc', Float32, queue_size=10)

    # 读入一些必要的参数
        # 读取车轮半径
        self.R = rospy.get_param('~robot_wheel_radius', .03)
        # 读取编码器的（每圈）刻度数
        self.encoder_tick = rospy.get_param('~hall_encoder_tick', 390)
        # 设定发布频率为10Hz
        self.rate = rospy.get_param('~rate', 10)
        # 过滤一些明显错误的编码器读数，这个参量有用吗？
        self.err_tick_incr = rospy.get_param('~err_tick_incr', 20)

    # 进行一些参数的初始化
        # 找一个hack判定车轮的旋转方向
        self.lwheel_dir = 1
        self.rwheel_dir = 1
        # 初始化编码器参数，使列表长度为5，表示5个时刻！？
        self.time_prev_update = rospy.Time.now()
        # 获取gopigo两个轮子的编码器读数，保留连续接受的5次数值，根据后两次数值计算角速度
        # lwheel_enc数值是进行更新lwheel_encs列表用的，循环对最后一个值更新
        self.lwheel_encs = [0] * 5
        self.rwheel_encs = [0] * 5
        self.lwheel_enc = 0
        self.rwheel_enc = 0


# ==================================================
#                                      回调函数(callback)
# ==================================================
    # 根据由订阅来的(wheel_angular_vel_motor)判断电机的旋转方向
    # return wheel_dir

    def lwheel_angular_vel_motor_callback(self, msg):
        if msg.data >= 0:
            self.lwheel_dir = 1
        else:
            self.lwheel_dir = -1

    def rwheel_angular_vel_motor_callback(self, msg):
        if msg.data >= 0:
            self.rwheel_dir = 1
        else:
            self.rwheel_dir = -1
    # 订阅编码器发布的数值
    # return self.wheel_enc

    def lwheel_enc_callback(self, msg):
        self.lwheel_enc = msg.data

    def rwheel_enc_callback(self, msg):
        self.rwheel_enc = msg.data


# ==================================================
#                        @由编码器的值计算车轮的旋转速度
# input enc_read
# return wheel_angular_vel_enc
# ==================================================
    # 将车轮编码器的变化量转换成弧度值(rad)，用于下面计算车轮的角速度(rad / dt)
    # input wheel_enc_delta = enc_cms, encoder_tick: 编码器一圈的刻度数，由参数服务器提供
    # return rads

    def enc_2_rads(self, enc_cms, encoder_tick):
        # 编码器的变化量占圆周的比例(prop_revolution) = 编码器的变化量(delta) / 车轮一周的刻度数(encoder_tick)
        prop_revolution = float(enc_cms) / (encoder_tick)
        # 编码器转动的距离对应的弧度值(rads) = 比例(prop_revolution) * 圆周的弧度(2*pi)
        rads = prop_revolution * (2 * math.pi)
        # print prop_revolution, rads
        return rads

    # @由编码器的读数，计算车轮的旋转速度
    # input enc_read
    # return wheel_angular_vel_enc
    def update(self):
        # 1.读取编码器的数值
        # # 这两行主要是对读入的编码器数值进行方向判断，然而我们的编码器数值，自己带正负号
        # lwheel_enc = self.lwheel_dir * lwheel_enc * .01  # cm's moved
        # rwheel_enc = self.rwheel_dir * rwheel_enc * .01  # cm's moved
        # 这样每次从第二个位置取，然后再补充，可以进行迭代
        self.lwheel_encs = self.lwheel_encs[1:] + [self.lwheel_enc]
        self.rwheel_encs = self.rwheel_encs[1:] + [self.rwheel_enc]
        # 暂时在终端打印一下
        print self.lwheel_encs, self.rwheel_encs
    # 2.由编码器读数的变化量
        # 确定编码器数值变化的时间差 dt(s)，是最后两次读数的时间差
        time_curr_update = rospy.Time.now()
        dt = (time_curr_update - self.time_prev_update).to_sec()
        # 确定编码器的刻度值的变化量 wheel_enc_delta
        # 两个时刻编码器数值的差
        # - 这两句可以移动到enc_2_rads()函数中，不取abs()就不用单独订阅参数来判断转动方向了
        # 先取abs再做差就消去了变化值的变化方向，只保留了变化的大小
        lwheel_enc_delta = self.lwheel_encs[-1] - self.lwheel_encs[-2]
        rwheel_enc_delta = self.rwheel_encs[-1] - self.rwheel_encs[-2]
        # print lwheel_enc_delta, rwheel_enc_delta, dt
    # 3.计算并发布车轮的角速度enc_cms / dt(rad/s)
        lwheel_angular_vel_enc = self.enc_2_rads(lwheel_enc_delta, self.encoder_tick) / dt
        rwheel_angular_vel_enc = self.enc_2_rads(rwheel_enc_delta, self.encoder_tick) / dt
        self.lwheel_angular_vel_enc_pub.publish(lwheel_angular_vel_enc)
        self.rwheel_angular_vel_enc_pub.publish(rwheel_angular_vel_enc)
        # print self.enc_2_rads(lwheel_enc_delta, self.encoder_tick)
        # print lwheel_angular_vel_enc, rwheel_angular_vel_enc
    # 4.更新当前时间，用于下次计算
        self.time_prev_update = time_curr_update


# %%
# ==================================================
#                                         主函数(main)
# ==================================================
    # 开启/gopigo_state_updater，进行while循环

    def spin(self):
        rospy.loginfo("启动gopigo_state_updater")
        rate = rospy.Rate(self.rate)
        rospy.on_shutdown(self.shutdown)

        while not rospy.is_shutdown():
            self.update()
            rate.sleep()
        rospy.spin()

    # 关闭/gopigo_state_updater前，对所有运动控制指令置零
    def shutdown(self):
        rospy.loginfo("停止gopigo_state_updater")
        # Stop message
        self.lwheel_angular_vel_enc_pub.publish(0)
        self.rwheel_angular_vel_enc_pub.publish(0)
        rospy.sleep(1)


# %%
def main():
    encoder_publisher = WheelEncoderPublisher()
    encoder_publisher.spin()


if __name__ == '__main__':
    main()
