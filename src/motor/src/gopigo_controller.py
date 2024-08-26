#! /usr/bin/python
# -*- coding:UTF-8 -*-

'''
    /gopigo_controller
    将由编码器读数转换而来的角速度用于PID控制器来校正误差（目标角速度 - 测量角速度）
    /diffdrive_controller
                    ↓
   {lwheel_tangent_vel_target  → /gopigo_controller → {lwheel_angular_vel_motor
    rwheel_tangent_vel_target}                                              rwheel_angular_vel_motor}
                                                                        ↑
                                                    {lwheel_angular_vel_enc
                                                    rwheel_angular_vel_enc}
'''
'''
    wheel_angular_vel_target: 电机的角速度控制命令
    wheel_angular_vel_control: PID算法校正后电机的角速度控制命令
    lwheel_angular_vel_motor: 发布电机的控制指令
'''

# %%
# Messages


# %%
# 定义引脚常量
import rospy
import roslib
import RPi.GPIO as GPIO
from std_msgs.msg import Float32
L298N_IN1_left = 23
L298N_IN2_left = 24
L298N_IN3_right = 21
L298N_IN4_right = 22
L298N_ENAB = 25

L298N_IN3_right = 21
L298N_IN4_right = 22


# 指定GPIO引脚编号规则
GPIO.setmode(GPIO.BCM)
# 设置GPIO引脚的输入（GPIO.IN）/输出（GPIO.OUT）/默认值（initial=GPIO.HIGH）
GPIO.setup(L298N_IN1_left, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(L298N_IN2_left, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(L298N_IN3_right, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(L298N_IN4_right, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(L298N_ENAB, GPIO.OUT, initial=GPIO.HIGH)

# 创建一个 pwm 实例，需要两个参数：
# 第一个是 GPIO 引脚号，该引脚（L298N_ENAB）与 A Enable 相连；
# 第二个是频率(HZ)，影响电机的响应速度
pwm = GPIO.PWM(L298N_ENAB, 80)
#  以输出 75%占空比(duty cycle)开始，影响电机的转速
pwm.start(75)


# %%
# 向GoPiGo电机发出命令以达到目标速度
# 使用PID比较基于编码器读数的误差
class ControlsToMotors:
    # ==================================================
    #                                                初始化
    # ==================================================
    def __init__(self):
        rospy.init_node('gopigo_controller')
    # 从参数服务器获取数据
        # 车轮半径的参数
        self.R = rospy.get_param('~robot_wheel_radius', 0.02)
        # 开启PID算法
        self.pid_on = rospy.get_param('~pid_on', True)
        # 获取PID参数，并设置采样频率50Hz
        self.rate = rospy.get_param('~rate', 50)
        self.Kp = rospy.get_param('~Kp', 1.0)
        self.Ki = rospy.get_param('~Ki', 1.0)
        self.Kd = rospy.get_param('~Kd', 1.0)
        # 定义电机的转速以及相应命令值关系：[最大转速，最小转速] -> [100(50rad/s), 20(10rad/s)]
        # 定义电机的最大转速：当motor_cmd = 100时，轮子转速为50rad/s
        # 定义电机的最小转速：当motor_cmd = 20时，轮子转速为10rad/s
        self.motor_max_angular_vel = rospy.get_param('~motor_max_angular_vel', 50)
        self.motor_min_angular_vel = rospy.get_param('~motor_min_angular_vel', 10)
        self.motor_cmd_max = rospy.get_param('~motor_cmd_max', 100)
        self.motor_cmd_min = rospy.get_param('~motor_cmd_min', 20)

    # Publisher: 发布机器人运动控制命令
        # 暂时注释掉该段，因为涉及到gopigo包
        # self.gopigo_on = rospy.get_param('~gopigo_on', True)
        # if self.gopigo_on:
        #     import gopigo3 as gopigo
        #     # 注册一个退出函数，在解释器正常终止时自动执行，一般用来做一些资源清理的操作
        #     # 所以，这个是用来在到达目标位置的时候停止机器人的吗？
        #     # 考虑一下，将该语句替换成发布的速度为0，可是之前在/diffdrive_controller中已经添加了一个发布速度为零的功能
        #     import atexit
        #     atexit.register(gopigo.stop)
        # 1.声明一个Publisher，发布电机的角速度控制命令，由发布的Twist消息转换成的运动速度，同样都仅仅是指令
        self.lwheel_angular_vel_target_pub = rospy.Publisher('lwheel_angular_vel_target', Float32, queue_size=10)
        self.rwheel_angular_vel_target_pub = rospy.Publisher('rwheel_angular_vel_target', Float32, queue_size=10)
        # 2.声明一个Publisher，发布PID算法校正后电机的角速度控制命令，即经过lwheel_angular_vel_enc校正后的速度控制命令
        self.lwheel_angular_vel_control_pub = rospy.Publisher('lwheel_angular_vel_control', Float32, queue_size=10)
        self.rwheel_angular_vel_control_pub = rospy.Publisher('rwheel_angular_vel_control', Float32, queue_size=10)
        # 3.声明一个Publisher，发布电机的控制指令，将速度控制指令映射为[0, 100]的PWM值（这个是带了正负号的）
        self.lwheel_angular_vel_motor_pub = rospy.Publisher('lwheel_angular_vel_motor', Float32, queue_size=10)
        self.rwheel_angular_vel_motor_pub = rospy.Publisher('rwheel_angular_vel_motor', Float32, queue_size=10)

    # Subscriber: 订阅运动控制相关信息
        # 1.订阅/diffdrive_controller发布的移动速度指令，转换成电机的控制指令
        # lwheel_tangent_vel_target -> lwheel_angular_vel_motor
        # rwheel_tangent_vel_target -> rwheel_angular_vel_motor
        self.lwheel_tangent_vel_target_sub = rospy.Subscriber('lwheel_tangent_vel_target', Float32, self.lwheel_tangent_vel_target_callback)
        self.rwheel_tangent_vel_target_sub = rospy.Subscriber('rwheel_tangent_vel_target', Float32, self.rwheel_tangent_vel_target_callback)
        # 2.订阅由编码器计算的实际速度，由/gopigo_state_updater发布，用于PID控制
        self.lwheel_angular_vel_enc_sub = rospy.Subscriber('lwheel_angular_vel_enc', Float32, self.lwheel_angular_vel_enc_callback)
        self.rwheel_angular_vel_enc_sub = rospy.Subscriber('rwheel_angular_vel_enc', Float32, self.rwheel_angular_vel_enc_callback)

    # 对一些关键参数进行初始化，即赋值为零
        # Tangential velocity target
        # 这个赋值有意义吗？这个参量不是已经在回调函数中定义了吗？
        # 先从订阅的话题中读入数据，再把它赋值为零？
        self.lwheel_tangent_vel_target = 0
        self.rwheel_tangent_vel_target = 0
        # Angular velocity target
        self.lwheel_angular_vel_target = 0
        self.rwheel_angular_vel_target = 0
        # Angular velocity encoder readings
        # 这个是从gopigo_state_updater -> gopigo_controller
        self.lwheel_angular_vel_enc = 0
        self.rwheel_angular_vel_enc = 0
        # 定义PID控制参数，需要两套参数吗？
        self.lwheel_pid = {}
        self.rwheel_pid = {}


# ==================================================
#                                       回调函数(callback)
# ==================================================
    # 从回调函数 -> 车轮转速(wheel_tangent_vel_target = msg.data)
    # 这个左右两个轮子的数据是否可以合并到一个函数里面来订阅，这个分开太麻烦了
    # 另外，这个回调函数仅仅是读入订阅的数据，太亏了吧，考虑把上面的赋值为零的处理合并进来


    def lwheel_tangent_vel_target_callback(self, msg):
        self.lwheel_tangent_vel_target = msg.data

    def rwheel_tangent_vel_target_callback(self, msg):
        self.rwheel_tangent_vel_target = msg.data
    # 从回调函数 -> 编码器读数(wheel_angular_vel_enc = msg.data)

    def lwheel_angular_vel_enc_callback(self, msg):
        self.lwheel_angular_vel_enc = msg.data

    def rwheel_angular_vel_enc_callback(self, msg):
        self.rwheel_angular_vel_enc = msg.data


# ==================================================
#                          1.电机的控制指令的相关计算
# ==================================================
    # 车轮的切线速度 -> 车轮的角速度(angular velocity target)，在/diffdrive_odom中有相反的变换
    # return angular_vel
    # - 这个地方就是/diffdrive_controller中的update()没有处理完，可以放到/diff中，其他地方没有引用这个中间数据


    def tangentvel_2_angularvel(self, tangent_vel):
        # v = wr
        # v - tangential velocity (m/s)
        # w - angular velocity (rad/s)
        # r - radius of wheel (m)
        angular_vel = tangent_vel / self.R
        return angular_vel

    # PID控制器
    # input wheel_pid, wheel_vel_target, wheel_enc
    # reutrn target_new = target + control_signal
        # 需要好好看看这个target，为什么可以和编码器的读数直接运算
    def pid_control(self, wheel_pid, target, state):
        # 初始化PID参数：时间、微分、积分、前项差分、差分
        if len(wheel_pid) == 0:
            wheel_pid.update({'time_prev': rospy.Time.now(), 'derivative': 0, 'integral': [0] * 10, 'error_prev': 0, 'error_curr': 0})
    # 计算 dt = time_curr - time_prev
        wheel_pid['time_curr'] = rospy.Time.now()
        wheel_pid['dt'] = (wheel_pid['time_curr'] - wheel_pid['time_prev']).to_sec()
        if wheel_pid['dt'] == 0:  # 这个判断是干吗用的？
            return 0
    # 计算P、I、D
        wheel_pid['error_curr'] = target - state  # wheel_vel_target - wheel_enc
        wheel_pid['error_prev'] = wheel_pid['error_curr']
        wheel_pid['integral'] = wheel_pid['integral'][1:] + [(wheel_pid['error_curr'] * wheel_pid['dt'])]
        wheel_pid['derivative'] = (wheel_pid['error_curr'] - wheel_pid['error_prev']) / wheel_pid['dt']
        control_signal = (self.Kp * wheel_pid['error_curr'] + self.Ki * sum(wheel_pid['integral']) + self.Kd * wheel_pid['derivative'])
        # 确保符号，计算的PID控制信号(control_signal)的符号没有翻转(does not flip sign)
        target_new = target + control_signal
        if target > 0 and target_new < 0:
            target_new = target
        if target < 0 and target_new > 0:
            target_new = target
        if (target == 0):  # Not moving
            target_new = 0
            return target_new  # 执行到`return`语句之后会退出函数，之后的语句不再执行
    # 更新一下时间，返回目标速度
        wheel_pid['time_prev'] = wheel_pid['time_curr']
        return target_new


# ==================================================
#           2.转换为电机的控制指令(Convert to motor commands)
# ==================================================
# 1.将计算的角速度(wheel_angular_vel_target) -> 电机控制指令(wheel_angular_vel_motor)[0, 100]
    # input wheel_angular_vel_target
    # return wheel_angular_vel_motor([0, 100])


    def angularvel_2_motorcmd(self, angular_vel_target):
        if angular_vel_target == 0:
            # 程序执行到return之后就会跳出
            return 0
        # 建立目标速度到电机命令的映射关系
            # 1.存在最小电机命令速度(motor_cmd_min)，低于该速度电机根本不会移动
            # 2.存在最大电机命令速度(motor_cmd_max)，超过该速度电机不会进一步加快
        slope = (self.motor_cmd_max - self.motor_cmd_min) / (self.motor_max_angular_vel - self.motor_min_angular_vel)
        intercept = self.motor_cmd_max - slope * self.motor_max_angular_vel
        # 电机正向旋转
        if angular_vel_target > 0:
            motor_cmd = slope * angular_vel_target + intercept
            if motor_cmd > self.motor_cmd_max:
                motor_cmd = self.motor_cmd_max
            if motor_cmd < self.motor_cmd_min:
                motor_cmd = self.motor_cmd_min
        # 电机反向旋转
        else:
            motor_cmd = slope * abs(angular_vel_target) + intercept
            if motor_cmd > self.motor_cmd_max:
                motor_cmd = self.motor_cmd_max
            if motor_cmd < self.motor_cmd_min:
                motor_cmd = self.motor_cmd_min
            motor_cmd = -motor_cmd
        return motor_cmd

# 2.发送电机的控制指令 -> 电机(PWM)
    # motorcmd_2_robot()主要功能是将int[0, 100] -> PWM发送给电机，由wheel_update()进行调用
    def motorcmd_2_robot(self, wheel='left', motor_command=0):
        pwm.ChangeDutyCycle(int(abs(motor_command)))
        if wheel == 'left':  # 左轮
            if motor_command > 0:  # 正转
                GPIO.output(L298N_IN1_left, GPIO.HIGH)
                GPIO.output(L298N_IN2_left, GPIO.LOW)
                print '左轮 - 正转'
            elif motor_command < 0:  # 反转
                GPIO.output(L298N_IN1_left, GPIO.LOW)
                GPIO.output(L298N_IN2_left, GPIO.HIGH)
                print '左轮 - 反转'
            else:
                GPIO.output(L298N_IN1_left, GPIO.LOW)
                GPIO.output(L298N_IN2_left, GPIO.LOW)
                print '停止'
        if wheel == 'right':  # 右轮
            if motor_command > 0:  # 正转
                GPIO.output(L298N_IN3_right, GPIO.HIGH)
                GPIO.output(L298N_IN4_right, GPIO.LOW)
                print '右轮 - 正转'
            elif motor_command < 0:  # 反转
                GPIO.output(L298N_IN3_right, GPIO.LOW)
                GPIO.output(L298N_IN4_right, GPIO.HIGH)
                print '右轮 - 反转'
            else:
                GPIO.output(L298N_IN3_right, GPIO.HIGH)
                GPIO.output(L298N_IN4_right, GPIO.LOW)
                print '停止'


# ==================================================
#        0.更新并发布电机的控制指令(Update motor commands)
# ==================================================
# 更新并发布电机的控制指令：左轮
    # 左轮和右轮是否可以合并，写一个通用的方法调用，虽然没有节省太多，但是还是有必要的


    def lwheel_update(self):
        # 1.计算并发布目标的角速度(target angular velocity)，根据运动控制命令转换的
        self.lwheel_angular_vel_target = self.tangentvel_2_angularvel(self.lwheel_tangent_vel_target)
        self.lwheel_angular_vel_target_pub.publish(self.lwheel_angular_vel_target)
    # 1.调用PID控制器结合订阅的编码器读数来调整目标的角速度，并将控制速度发布出去
        if self.pid_on:
            self.lwheel_angular_vel_target = self.pid_control(self.lwheel_pid, self.lwheel_angular_vel_target, self.lwheel_angular_vel_enc)
        self.lwheel_angular_vel_control_pub.publish(self.lwheel_angular_vel_target)
    # 2.将速度控制指令 -> 电机控制指令，即[0, 100]的整数(int)
        # return motor_cmd
        lwheel_motor_cmd = self.angularvel_2_motorcmd(self.lwheel_angular_vel_target)
        self.lwheel_angular_vel_motor_pub.publish(lwheel_motor_cmd)
    # 2.发送电机的控制指令 -> 电机(PWM)  ，即去掉正负号后发送给占空比
        self.motorcmd_2_robot('left', lwheel_motor_cmd)

# 更新并发布电机的控制指令：右轮
    def rwheel_update(self):
        # 1.计算并发布电机的角速度(target angular velocity)
        self.rwheel_angular_vel_target = self.tangentvel_2_angularvel(self.rwheel_tangent_vel_target)
        self.rwheel_angular_vel_target_pub.publish(self.rwheel_angular_vel_target)
    # 1.通过PID控制器结合订阅的编码器读数来调整目标的角速度，并将控制速度发布出去
        if self.pid_on:
            self.rwheel_angular_vel_target = self.pid_control(self.rwheel_pid, self.rwheel_angular_vel_target, self.rwheel_angular_vel_enc)
        self.rwheel_angular_vel_control_pub.publish(self.rwheel_angular_vel_target)
    # 2.将计算的角速度(angular velocity targets) -> 电机控制指令
        # return motor_cmd
        rwheel_motor_cmd = self.angularvel_2_motorcmd(self.rwheel_angular_vel_target)
        self.rwheel_angular_vel_motor_pub.publish(rwheel_motor_cmd)
    # 2.发送电机的控制指令 -> 电机(PWM)
        self.motorcmd_2_robot('right', rwheel_motor_cmd)


# %%
# ==================================================
#                                         主函数(main)
# ==================================================
    # 开启gopigo_controller，进行while循环
    # 当短时间内没有运动控制指令时，停止机器人


    def spin(self):
        rospy.loginfo("开启gopigo_controller")
        rate = rospy.Rate(self.rate)
        # 关闭节点时，对运动控制指令进行清零，调用self.shutdown()函数
        rospy.on_shutdown(self.shutdown)
        # rospy.is_shutdown()和rospy.spin()重复了，考虑去掉后者？！
        while not rospy.is_shutdown():
            self.rwheel_update()
            self.lwheel_update()
            rate.sleep()
        rospy.spin()

    # 关闭gopigo_controller前，对所有运动控制指令置零
    def shutdown(self):
        rospy.loginfo("停止gopigo_controller")
        self.lwheel_angular_vel_target_pub.publish(0)
        self.rwheel_angular_vel_target_pub.publish(0)
        self.lwheel_angular_vel_control_pub.publish(0)
        self.rwheel_angular_vel_control_pub.publish(0)
        self.lwheel_angular_vel_motor_pub.publish(0)
        self.rwheel_angular_vel_motor_pub.publish(0)
        rospy.sleep(1)


# %%
def main():
    controls_to_motors = ControlsToMotors()
    controls_to_motors.spin()


if __name__ == '__main__':
    main()
