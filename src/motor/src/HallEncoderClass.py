#! /usr/bin/env python
# -*- coding:UTF-8 -*-

'''
    电机参数：
        电机转速320RPM，编码器线数360线，电机供电电压12V，编码器供电3.3V，编码器区分正负极并且不可以接反。
        减速比：30 : 1
        空载转速：320RPM
        额定负载：0.3Kg·cm
        负载转速：270RPM
        堵转扭力：1.8Kg·cm

    编码器（13极霍尔编码器）：
        VDD和GND是编码器电源正极和负极，接3.3~5V电压；
        A和B是编码器的脉冲信号输出。


        相应变速箱输出轴的CPR：
        CPR = 13 * 30 * 4 = 1560
        即，电机最终轴完成一圈旋转，变速箱输出轴的编码器计数1560次
        编码器单个通道生成一个脉冲对应4个CPR计数值，则：
        PPR = 1560 / 4 = 390

    车轮的旋转角度：
        转角 = （计数值 / CPR）× 360
        则，每度的计数值 = CPR / 360 = 1560 / 360 = 4.33...


    这个要做高速计数的。
    单位时间的脉冲个数就是转速。
    另外根据你通过什么来确定转动方向。看你的是ab相，那么可以总这个来确定方向。但这占用2个输入通道。做一个表就知道了。

    转速:一圈的脉冲个数是确定的。以一秒或者半秒为单位。进行计数。注意转速单位的转化。
    方向:对ab相同时刻进行测量，。满足a正b反，a正b正，a反b正，a反b反。这个顺序是正转的话，反之就是反转。
'''
# %% 
import rospy
import time
import RPi.GPIO as GPIO
from std_msgs.msg import Int64



# %%
class HallEncoderCounter():
# ==================================================
#                                                初始化
# ==================================================
    def __init__(self):
        rospy.init_node('hall_encoder_left')
        # 初始化参数
        self.Counter = 0
        self.flag = 0
        self.Hall_B_Last = 0
        self.Hall_B_Current = 0
        self.rate = 10

        # 指定GPIO引脚规则：BOARD、BCM
        GPIO.setmode(GPIO.BCM)
        # 定义引脚常量
        # self.Hall_A = 12 # Left_A相
        # self.Hall_B = 13 # Left_B相
        # 初始化引脚状态
        GPIO.setup(self.Hall_A, GPIO.IN)
        GPIO.setup(self.Hall_B, GPIO.IN)

    def initial_Pin(self, Hall_A, Hall_B):
        """
        初始化树莓派的引脚，用来定义AB相，和__init__()区分开，是为了方便传递参数
        """
        # 定义引脚常量
        self.Hall_A = Hall_A # Left_A相 = 12
        self.Hall_B = Hall_B # Left_B相 = 13

    def initial_node(self, Publisher):
        # 声明Publisher
        self.wheel_enc_pub = rospy.Publisher(Publisher, Int64, queue_size=10)


    def Hall_Encoder(self):
        # 记录并更新B的状态变化：
        self.Hall_B_Last = GPIO.input(self.Hall_B)
        # 检测A的状态是否发生变化
        while not GPIO.input(self.Hall_A):
            # 若A的状态发生变化则更新B的状态
            self.flag = 1
            self.Hall_B_Current = GPIO.input(self.Hall_B)
        # 更新B的状态
        if self.flag == 1:
            self.flag = 0
            # 若B_Last = 0且B_Current = 1，则为正转
            if (self.Hall_B_Last == 0) and (self.Hall_B_Current == 1):
                self.Counter += 1
            # 若B_Last = 1且B_Current = 0，则为反转
            if (self.Hall_B_Last == 1) and (self.Hall_B_Current == 0):
                self.Counter -= 1
        return self.Counter


# ==================================================
#                                         主函数(main)
# ==================================================
    def update(self):
        # if RF == 'Right':
        #     self.Right()
        # elif RF == 'Left':
        #     self.Left()
        # 将发布频率同步好，是不是就可以省去tmp参数
        tmp = 0    # Rotary Temperary
        # rate = rospy.Rate(self.rate)
        rospy.on_shutdown(self.shutdown)

        while not rospy.is_shutdown():
            Counter = self.Hall_Encoder()
            if tmp != Counter:
                print('Counter = %d' % Counter)
                tmp = self.Counter
                # 发布编码器计数
                self.wheel_enc_pub.publish(Counter)
            # rate.sleep()
        # rospy.spin()

    def shutdown(self):
        GPIO.cleanup()
    


# %%
def main():
    counter_encoder = HallEncoderCounter()
    counter_encoder.update()

# Program start from here
if __name__ == '__main__':
    main()