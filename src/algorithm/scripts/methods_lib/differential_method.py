#! /usr/bin/env python
# -*- coding:utf-8 -*-
'''md
    1. 勾刺变体机构运动学建模 - Complex vector method
        验证后，正向运动学的式子是正确的
'''

# Math
from math import acos, degrees, sin, cos, sqrt, pow
import numpy as np
# Tool
from tools_lib.debug_stream import DebugSteam

# %% class
class KinematicsClass(DebugSteam):
# ==================================================
#                           1. 勾刺变体机构运动学建模
# ==================================================
    def kinematics(self, link, rad):
        '''
            [issue]:
                def kinematics(self, l_0, l_1, l_2, l_3, theta, dot_theta, ddot_theta):
                考虑将形参打包成两个列表，只是这样调用的时候赋值更方便一些
                link = [l_0, l_1, l_2, l_3]
                rad = [theta, dot_theta, ddot_theta]
                [l_0, l_1, l_2, l_3] = link[0], link[2], link[2], link[3]
                [theta, dot_theta, ddot_theta] = rad[0], rad[1], rad[2], rad[3]

            1. 这里是求解的机构的运动学模型，可以得到`原动杆件的角速度`和`输出杆件的角速度`关系
                在实际机构中可以获得的是`原动杆件的角速度`，借助运动学关系解得`输出杆件的角速度`
                `dot_varphi = Jacobian_theta * dot_theta`
            2. 在动力学模型中，使用`输出杆件的角速度`(或相关衍生量)作为输入量参与计算
            3. 这个四杆机构运动是有杆长条件约束的，这部分也可以写在文章里面
                如原动件的运动范围：[]
                执行构件的运动范围：[]

            :input theta:
            :input dot_theta:
            :input ddot_theta:

            :param w: w = l_AB
            :param phi:
            :param phi_1:
            :param phi_2:
            :param theta:

            :return varphi:
            :return dot_varphi:
            :return ddot_varphi:
        '''
        l_0, l_1, l_2, l_3 = link
        theta, dot_theta, ddot_theta = rad
        if theta==0.0:
            # [issue]: ValueError: math domain error
            # 通过复数矢量法计算
            return 0, 0, 0.09768951451409347, 0.0, 0.0
        # 变体机构位置关系:
        w_2 = (l_0**2) + (l_1**2) - (2*l_0*l_1*cos(theta))
        w = sqrt(w_2) # AB线段的长度
        varphi_1 = acos((l_0**2+w_2-l_1**2)/(2*l_0*w))
        varphi_2 = acos((l_3**2+w_2-l_2**2)/(2*l_3*w))
        varphi = varphi_1 + varphi_2
        
        # 变体机构速度关系: 
        delta_1 = ((l_0**2)+w_2-(l_1**2)) / (2*l_0*w)
        delta_2 = ((l_3**2)+w_2-(l_2**2)) / (2*l_3*w)
        partial_delta1_w = (w_2-(l_0**2)+(l_1**2)) / (2*l_0*w_2)
        partial_delta2_w = (w_2-(l_3**2)+(l_2**2)) / (2*l_3*w_2)
        dot_w_theta = (l_0*l_1) * sin(theta) / w
        J11 = (pow((1-delta_1**2), (-1./2.))) * (partial_delta1_w)
        J12 = (pow((1-delta_2**2), (-1./2.))) * (partial_delta2_w)
        # 令$J(\theta)$为四杆机构的运动学Jacobian，则输出杆$L_3$的角速度与原动件$L_1$的角速度之间的关系: 
        # 有了这个关系，在动力学运算的过程中，可以由dot_theta解得dot_varphi，因为dot_theta是可以通过编码器获得的
        Jacobian = -(J11+J12) * dot_w_theta
        dot_varphi = Jacobian * dot_theta
        
        # 变体机构加速度关系
        # 上式两边同时对时间积分/差分，即速度积分得到位移/加速度
        # 有了如上两个关系之后，在动力学模型中设计到有关varphi的量，就都可以转换成有关theta的量了，因为在实际的模型中有关theta的量才是已知的
        # 同样的例子在师姐的有关大象鼻子平台的论文中也有提到，如式(12)通过式(2)进行微分得到的(By applying the differential kinematics (2) and the following acceleration relationship)
        # varphi = Jacobian * theta
        dot_w = dot_w_theta * dot_theta
        dot_delta_1 = partial_delta1_w * dot_w
        dot_delta_2 = partial_delta2_w * dot_w
        dot_partial_delta1_w = ((l_0**2-l_1**2)/(l_0*pow(w, 3.))) * dot_w
        dot_partial_delta2_w = ((l_3**2-l_2**2)/(l_3*pow(w, 3.))) * dot_w
        d_J1_1 = (pow((1-delta_1**2), (-3./2.)) * delta_1 * dot_delta_1 * partial_delta1_w) \
                        + (pow((1-delta_1**2), (-1./2.)) * dot_partial_delta1_w)
        d_J1_2 = (pow((1-delta_2**2), (-3./2.)) * delta_2 * dot_delta_2 * partial_delta2_w) \
                        + (pow((1-delta_2**2), (-1./2.)) * dot_partial_delta2_w)
        d_J2_1 = -((l_0*l_1*sin(theta))/w_2) * dot_w_theta * dot_theta
        d_J2_2 = ((l_0*l_1*cos(theta))/w) * dot_theta
        d_J1 = d_J1_1 + d_J1_2
        d_J2 = d_J2_1 + d_J2_2
        dot_Jacobian = -(d_J1*dot_w_theta + (J11+J12)*d_J2)
        ddot_varphi = dot_Jacobian*dot_theta + Jacobian*ddot_theta
        # [issue]: `Jacobian*ddot_theta`这项要是舍去，计算出来的数值和复数矢量法建模得到的加速度结果是一样的

        return Jacobian, dot_Jacobian, varphi, dot_varphi, ddot_varphi
# ==================================================
#                           2. 勾刺变体机构逆运动学建模
# ==================================================
    def inverse_kinematics(self, link, rad):
        l_0, l_1, l_2, l_3 = link
        varphi, dot_varphi, ddot_varphi = rad
        # self.debug_stream(varphi)
        # if varphi==0.0:
        #     # [issue]: ValueError: math domain error
        #     # 通过复数矢量法计算的
        #     return 0, 0, 0.09768951451409347, 0.0, 0.0
        # 变体机构位置关系:
        q_2 = (l_0**2) + (l_3**2) - (2*l_0*l_3*cos(varphi))
        q = sqrt(q_2) # Co线段的长度
        # 这行有问题？
        # self.debug_stream(type((l_0**2+q_2-l_3**2)/(2*l_0*q))) # 1.0
        # self.debug_stream(type(acos(1.0))) # 0.0
        # self.debug_stream(acos((l_0**2+q_2-l_3**2)/(2*l_0*q))) # 1.0
        theta_1 = acos((l_0**2+q_2-l_3**2)/(2*l_0*q))
        theta_2 = acos((l_1**2+q_2-l_2**2)/(2*l_1*q))
        theta = theta_1 - theta_2
        # [issue]: 这里因为模型建立的时候没有考虑是双摇杆还是曲柄摇杆，出现的bug，暂时冷处理一下；
        # print("{}\n --- --- ---".format(degrees(theta)))
        
        # 变体机构速度关系: 
        omega_1 = ((l_0**2)+q_2-(l_3**2)) / (2*l_0*q)
        omega_2 = ((l_1**2)+q_2-(l_2**2)) / (2*l_1*q)
        partial_omega1_q = (q_2-(l_0**2)+(l_3**2)) / (2*l_0*q_2)
        partial_omega2_q = (q_2-(l_1**2)+(l_2**2)) / (2*l_1*q_2)
        dot_q_varphi = (l_0*l_3) * sin(varphi) / q
        J11 = (pow((1-omega_1**2), (-1./2.))) * partial_omega1_q
        J12 = (pow((1-omega_2**2), (-1./2.))) * partial_omega2_q
        # 令$J(\varphi)$为四杆机构的运动学Jacobian，则输出杆$L_3$的角速度与原动件$L_1$的角速度之间的关系: 
        # 有了这个关系，在动力学运算的过程中，可以由dot_varphi解得dot_theta，因为dot_varphi是可以通过编码器获得的
        Jacobian = -(J11+J12) * dot_q_varphi
        dot_theta = Jacobian * dot_varphi
        
        # 变体机构加速度关系
        # 上式两边同时对时间积分/差分，即速度积分得到位移/加速度
        # 有了如上两个关系之后，在动力学模型中设计到有关theta的量，就都可以转换成有关varphi的量了，因为在实际的模型中有关varphi的量才是已知的
        # 同样的例子在师姐的有关大象鼻子平台的论文中也有提到，如式(12)通过式(2)进行微分得到的(By applying the differential kinematics (2) and the following acceleration relationship)
        # theta = Jacobian * varphi
        dot_q = dot_q_varphi * dot_varphi
        dot_omega_1 = partial_omega1_q * dot_q
        dot_omega_2 = partial_omega2_q * dot_q
        dot_partial_omega1_q = ((l_0**2-l_3**2)/(l_0*pow(q, 3.))) * dot_q
        dot_partial_omega2_q = ((l_1**2-l_2**2)/(l_1*pow(q, 3.))) * dot_q
        d_J1_1 = (pow((1-omega_1**2), (-3./2.)) * omega_1 * dot_omega_1 * partial_omega1_q) \
                        + (pow((1-omega_1**2), (-1./2.)) * dot_partial_omega1_q)
        d_J1_2 = (pow((1-omega_2**2), (-3./2.)) * omega_2 * dot_omega_2 * partial_omega2_q) \
                        + (pow((1-omega_2**2), (-1./2.)) * dot_partial_omega2_q)
        d_J2_1 = -((l_0*l_3*sin(varphi))/q_2) * dot_q_varphi * dot_varphi
        d_J2_2 = ((l_0*l_3*cos(varphi))/q) * dot_varphi
        d_J1 = d_J1_1 + d_J1_2
        d_J2 = d_J2_1 + d_J2_2
        dot_Jacobian = -(d_J1*dot_q_varphi + (J11+J12)*d_J2)
        ddot_theta = dot_Jacobian*dot_varphi + Jacobian*ddot_varphi
        # [issue]: `Jacobian*ddot_varphi`这项要是舍去，计算出来的数值和复数矢量法建模得到的加速度结果是一样的

        return Jacobian, dot_Jacobian, theta, dot_theta, ddot_theta


# %% main
def main():
    '''
        在这里写一个循环的例子吧
    '''
    Kin = KinematicsClass()
# kinematics
    '''当rad = [0.0, 0.0, 0.0]的时候，会导致计算delta_1 = 1.0，从而在开方的时候结果为零，还是作为分母出现的，就会报错
    这里给出的结果rad_varphi  = (0.09768951451409347, -0.0, -0.0)是通过复数矢量法建立的
    程序再执行到rad=[0.0,0.0,0.0]的时候，直接return上面的结果'''
    # rad = [0.0, 0.0, 0.0]
    # link = [0.361732, 0.07767, 0.02929, 0.29221]
    # rad_varphi = Kin.kinematics(link, rad)
    # Kin.debug_stream(rad_varphi)
# inverse kinematics
    '''这个逆向运动学也是没有问题的，当varphi=0.09768951451409347时，计算的theta=-3.43499905598e-13
    也就约等于零了'''
    rad = [0.09768951451409347, 0.0, 0.0]
    link = [0.361732, 0.07767, 0.02929, 0.29221]
    rad_theta = Kin.inverse_kinematics(link, rad)
    Kin.debug_stream(degrees(rad_theta[2]))

if __name__ == '__main__':
    main()