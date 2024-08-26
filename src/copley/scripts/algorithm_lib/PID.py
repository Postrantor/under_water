#! /usr/bin/env python
# -*- coding:utf-8 -*-
'''md
    这个就是作为一个库，主要是针对电机
    这里会调用驱动的函数，被主函数调用，就像接线一样
'''

# %% import
# Lib
import rospy
# Hardware

# %% class
class AlgorithmPIDClass():
    '''
        Algorithm PID
    '''
# ==================================================
#                                                Initial
# ==================================================
    def __init__(self):
        self.inits_parameter_pid()

    def inits_parameter_pid(self):
        """
        docstring
        """
        self.pid_on = False # 开启PID算法/False/Ture
        self.Kp = 1.0
        self.Ki = 1.0
        self.Kd = 1.0
        # 定义PID控制参数，考虑合并为一套参数
        self.wheel_pid = {}
# ==================================================
#                                             1.PID Controller
# Input: wheel_pid, wheel_target, wheel_enc
# Reutrn: target_new = target + control_signal
# ==================================================
    def control(self, wheel_pid, target, state):
        # initial PID param: time_prev, derivative, integral, error_prev, error_curr
        if len(wheel_pid) == 0:
            wheel_pid.update({'time_prev': rospy.Time.now(), 'derivative': 0, 'integral': [0]*10, 'error_prev': 0, 'error_curr': 0})
        # dt = time_curr - time_prev
        wheel_pid['time_curr'] = rospy.Time.now()
        wheel_pid['dt'] = (wheel_pid['time_curr'] - wheel_pid['time_prev']).to_sec()
        if wheel_pid['dt'] == 0:
            return 0
        # calc Kp, Ki, Kd
        wheel_pid['error_curr'] = target - state # wheel_target - wheel_enc
        wheel_pid['error_prev'] = wheel_pid['error_curr']
        wheel_pid['integral'] = wheel_pid['integral'][1:] + [(wheel_pid['error_curr']*wheel_pid['dt'])]
        wheel_pid['derivative'] = (wheel_pid['error_curr'] - wheel_pid['error_prev']) / wheel_pid['dt']
        control_signal = (self.Kp*wheel_pid['error_curr'] + self.Ki*sum(wheel_pid['integral']) + self.Kd*wheel_pid['derivative'])
        # control_signal does not flip sign
        target_new = target + control_signal
        if target > 0 and target_new < 0:
            target_new = target
        if target < 0 and target_new > 0:
            target_new = target
        if (target == 0):  # Not moving
            target_new = 0
            return target_new
        # update time
        wheel_pid['time_prev'] = wheel_pid['time_curr']
        return target_new
# ==================================================
#                                       Update_Algorithm
# ==================================================
# 调用PID控制器结合订阅的编码器读数来调整目标的角速度，并将控制速度发布出去
    def update(self, wheel_vel_target, wheel_vel_enc):
        if self.pid_on:
            wheel_vel_target = self.control(self.wheel_pid, wheel_vel_target, wheel_vel_enc)

        return wheel_vel_target

# %%
def main():
    print('Algorith PID')

if __name__ == '__main__':
    main()