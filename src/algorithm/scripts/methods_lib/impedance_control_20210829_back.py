#! C:\Users\trantor\anaconda3\envs\trantor_py38\python.exe
# -*- coding:utf-8 -*-
'''md
    [Backup]:
        接下来要恢复阻抗控制的运动学，在这里备份一下，避免修改出现错误
    [20210829]:
        恢复运动学控制
    [20210817]:
        1. 针对控制电机，需要加一些限制措施，避免出现越过极限的情况
        2. 使用control()函数取代odeint()函数
    [20210728]:
        可以针对不同的四杆机构进行阻抗控制的仿真，横向对比那种机构比较好；
        同时，可以针对一种类型的机构优化杆长，使得控制更好；
        不过这些东西整体上来说都是优化的事情呀
    [20210726]: Backup
        [该版本仅作为备份使用]
        目前文章已经初具规模了，摘要、介绍、建模、算法已经有点样子了，接下来对数值仿真部分进行修正；
        1. 增加不变阻抗控制；
        2. 完善时变阻抗控制；
            1. 对参数的选取目前还很粗略；
            2. 数值收敛的还比较慢，相比FYN的文章，不到2s就已经收敛稳定，当前大约要5s；
        3. 增加输出的变量，绘制其他变量的图形；
        4. 规范图像的格式；
    [20210717]:
        目前已经在开始写文章了，代码着手进行全面的补充、优化
        1. 整理目前杂乱的结构
        2. 添加定阻抗控制
        √3. 完善仿真图形的输出，自动保存到相关目录
    [20210702]:
        程序已经可以执行，可以产生图像，但是数据还不对，需要调整参数
        接下来会精简一部分注释，所以特意留一下该版本
    [20210615]: 仿真为主
        前一阵子备考六级来着，也不知道结果咋样，心里没谱
        考虑一下，还是暂时先完全模仿师姐的阻抗控制论文，做一篇仿真的出来
        要是结合实验进行验证的话，不确定因素太多：
        1. 实验平台本身的机械结构有问题，钩刺机构本身的刚度不够、钩刺本身的刚度也有问题
        2. 关于阻抗控制算法中的刚度参数等时变参数，需要根据实验平台来确定，即控制律的好坏取决于建模的精度
            就这一点来说，不太靠谱；可以使用自适应结合，来减弱建模精度对控制效果的影响；

        总的来说：
        1. 模仿师姐的文章，做一篇定阻抗 + 变阻抗的数值仿真文章出来
        2. 在上一篇文章的基础上，结合自适应控制算法做一篇文章出来
        3. 在第一篇文章的基础上，结合滑模控制算法做一篇文章出来
        4. 在实验平台上验证阻抗控制算法
        5. 在实验平台上验证自适应控制算法
        6. 在实验平台上验证滑模控制算法
        7. 做吸附力有关的受力分析的文章
    [20210602]:
        1. 书写基本的算法架构，暂时先不用在ROS端调用
    [REDME]:
        NumPy的一些使用：https://zhuanlan.zhihu.com/p/32242331

        该函数作为一个库，放在RPi端，用于控制电机的
        使用阻抗控制算法，用于控制勾刺机构的运动

        闭环控制的设计：
            1. 设计控制律$\tau_{\varphi}(t)$，使得变体机构原动力学模型(2)的闭环动力学(3)具有期望的稳定动态特性；
            2. 时变刚度$K(t)$应满足给定攀爬运动任务要求；
            3. 时变阻尼$D(t)$应使得当外力矩$\tau_{e}=0$时，闭环动力学系统(3)的误差状态变量$\bar\varphi$是全局渐近稳定的，即$\lim_{t \rightarrow \infty} \bar{\varphi}=0$；
            4. 当外力矩$\tau_{e} \neq 0$时，闭环动力学系统(3)的误差状态变量$\bar{\varphi}$是全局稳定的$({\dot{\bar{\varphi}}=0}, {\ddot{\bar{\varphi}}=0})$，即${K(t)}{\bar\varphi}={\tau_{e}}$成立；

        闭环控制需要达到的效果：
            1. 设定连杆$L_3$的角位置名义给定值为$\varphi^{d}$；
            2. 给定连杆$L_3$的输出刚度为$K(t)$；
            3. 设计阻尼$D(t)$，使得在外力矩$\tau_{e}$作用下，连杆$L_3$的实际角位置应满足关系${K(t)}{\bar\varphi}={\tau_{e}}$，
                即K(t)\left(\varphi^{d}-\varphi\right)=\tau_{e}

        cd D:\Document\Postgraduate\CAA\variable_impedance_control_of_the_prick_mechanism\code\
        clear; python .\impedance_control.py
'''

# %% import
# Lib
import rospy
import time
# Math
import numpy as np
from math import degrees, radians, sin, cos, atan, sqrt, exp, pi
# Scripts
from methods_lib.differential_method import KinematicsClass as DiffKinematicsClass

# %% constant
# m_l3和tau_e之间有4倍的关系，在这个比例关系下，可以达到期望的接触力，即tau_varphi = tau_e
l_0 = 0.361732 # unit: m # 连杆$L_{i}$的长度
l_1 = 0.07767
l_2 = 0.02929
l_3 = 0.29221
m_l3 = 2.443 # unit: Kg # 连杆$L_3$的质量
gravity = 9.8 # unit: m/s^2 # 重力加速度
# tau_e = 1.24 # 1.237 # 2.443/4 # unit: N·m # 外力矩 # 定阻抗
tau_e = 1.24 # 2.443/4 # unit: N·m # 外力矩 # 变阻抗
beta = radians(45) # unit: rad # $\beta$为机器人本体的俯仰角；

# %% class
class AlgorithmImpedanceClass(DiffKinematicsClass):
# ==================================================
#                                         Initial_Parameters
# ==================================================
    def __init__(self):
        self.inits_control()
        self.inits_desired()
        self.inits_parameters()
    def inits_desired(self):
        """
        :param varphi: 最小值是0.0977 rad
        """
    # initial params
        init_var = np.array([0.0977, 0.0]) # varphi, dot_varphi
    # desired params
        theta_d = radians(40) # unit: rad # [-1.65, 42.66, 53.37]
        dot_theta_d = 0 # unit: rad/s #
        ddot_theta_d = 0 # unit: rad/s^2 #
    # kinematic
        __, __, self.varphi_d, self.dot_varphi_d, self.ddot_varphi_d = self.kinematics(l_0, l_1, l_2, l_3, theta_d, dot_theta_d, ddot_theta_d)
    def inits_parameters(self):
        self.N_beta = (1./2.) * (m_l3*gravity) * (l_3) * (sin(beta)) # $N(\beta)$: 连杆$L_3$关于铰链$B$的有效重力矩；
        self.M = (1./3.) * (m_l3) * (l_3**2) # $M$: 假设连杆$L_3$为均质杆，绕$B$点的转动惯量；
        self.C = 0.25 # $C$为机构的不确定(摩擦)阻尼系数，实际中可取(0, 0.5)；
        self.alpha = 5.0 # > 0，为常数；
        self.H = 5.0 # > 0，为闭环动力学的惯量，可取为常数；
        self.varepsilon = 0.1 # > 0，为小常数；
    def inits_control(self):
        """
            [Python 字典(Dictionary) | 菜鸟教程](https://www.runoob.com/python/python-dictionary.html)
            dict.update(dict2) # 把字典dict2的键/值对更新到dict里

            :param impedance:
        """
        self.Button = False # 开启Impedance算法
        self.impedance = {}
# ==================================================
#                                           Dynamic_Modeling
# ==================================================
    def dynamics(self, tau_varphi):
        '''
            $J^{\mathrm{T}} \tau_{\varphi}=\tau_{e} \text { 或 } \tau_{\varphi}=J^{-\mathrm{T}} \tau_{e}$
            这个应该是用来画图用的，当给定tau_e时，经过动力学转换得到等价的tau_varphi
            从这里得到的tau_varphi与控制律计算得到的tau_varphi放在同一张图里
        '''
        J_neg_T = np.linalg.inv(self.Jacobian_theta) # 雅克比矩阵求逆
        J_T = self.Jacobian_theta
        # tau_varphi = J_neg_T * tau_e
        tau_e = J_T * tau_varphi
        # 在师姐的论文中，也同样要求解出动力学关系的雅克比矩阵；
        # 在计算刚度矩阵的时候，这个量是要根据外力确定的，即外接接触力的状态来调整自身得到刚度；
        # 然而，外力并不容易测量得到(有力传感器的除外)，即通过上面的动力学关系，将外力转化到驱动力上，进而解得刚度系数矩阵
        return tau_e
    def inverse_dynamics(self, y, dt, varphi_d, dot_varphi_d, ddot_varphi_d):
        """
            假设连杆$L_{3}$的质量和惯量远远大于连杆$L_{1}$和$L_{2}$的质量和惯量，因此连杆$L_{1}$和$L_{2}$的质量和惯量忽略。假设连杆$L_{3}$绕$B$点的转动惯量为$M$，连杆$L_{3}$的质量为$m$，机构的摩擦阻尼系数为$C$，连杆$L_{3}$关于铰链$B$的有效重力矩为$N(\beta)$，其中$\beta$为机器人本体的俯仰角。则该四杆机构的动力学模型可表示为：
            $M \ddot{\varphi}+C \dot{\varphi}+N(\beta)=\tau_{\varphi}+\tau_{e}$
            # 以求解二阶微分方程的思路：
                1. 第一点：
                    根据初始条件带入控制律之后可以得到tau_varphi，即驱动力矩；
                    将tau_vaphi带入系统的真实动力学模型，反解出varphi、dot_varphi、ddot_varphi；
                    在一切条件 + 初始条件下，系统表现出来的varphi、dot_varphi、ddot_varphi；
                    这些参数就是在控制律的调整下，从初始条件发生的变化；
                2. 第二点：
                    这里将varphi参数视为关于t的函数，不然不知道怎么解微分方程；
                    这里带入t进行运算的时候，应该是用的d_t？那么d_t应该是发生bar_varphi的时间，可是这样计算出来的是增量还是绝对量？
                    那在第一点中带入的初始条件是增量还是绝对量呢？
                3. 第三点：
                    假设tau_e != 0时，根据bar_varphi是全局稳定，有bar_dot_varphi = 0、bar_ddot_varphi = 0。可得dot_varphi = dot_varphi_d、ddot_varphi = ddot_varphi_d；
                    将dot_varphi、ddot_varphi带入下面的式子，联立可以解得C1、C2
                    `line_solve = linsolve([-C1*sqrt(-C/M)*exp(-t*sqrt(-C/M)) + C2*sqrt(-C/M)*exp(t*sqrt(-C/M)) - dot_varphi_d, C1*(-C/M)*exp(-t*sqrt(-C/M)) + C2*(-C/M)*exp(t*sqrt(-C/M)) - ddot_varphi_d], (C1, C2))`
            
            # 以状态空间方程的思路(详见`example_ode45.py`)
                Examples
                The second order differential equation for the angle `theta` of a
                pendulum acted on by gravity with friction can be written::
                    `theta''(t) + b*theta'(t) + c*sin(theta(t)) = 0`
                where `b` and `c` are positive constants, and a prime (') denotes a
                derivative. To solve this equation with `odeint`, we must first convert
                it to a system of first order equations. By defining the angular
                velocity ``omega(t) = theta'(t)``, we obtain the system::
                    `theta'(t) = omega(t)`
                    `omega'(t) = -b*omega(t) - c*sin(theta(t))`
                这就是个状态空间方程：
                    `dot_x1 = x2`
                    `dot_x2 = -b*x2 - c*sin(x1)`
                    ```python
                    def pend(y, t, b, c):
                        # 状态空间方程：
                        theta, omega = y # x1, x2
                        dot_y_t = [omega, -b*omega - c*np.sin(theta)] # dot_x1, dot_x2(ddot_x1)
                        return dot_y_t

                    solve = odeint(pend, y0, t, args=(b, c))
                    ```
        """
        varphi = y[0]
        dot_varphi = y[1]
    # bar_varphi
        bar_varphi = varphi_d - varphi
        bar_dot_varphi = dot_varphi_d - dot_varphi
    # invariant impedance parameters
        tau_varphi = self.invariant_impedance(
                                beta = beta, 
                                bar_varphi = bar_varphi, 
                                bar_dot_varphi = bar_dot_varphi, 
                                dot_varphi = dot_varphi, 
                                ddot_varphi_d = ddot_varphi_d)
    # variable impedance parameters
        # tau_varphi, M, C, N_beta = self.variable_impedance(
        #                         time = t, 
        #                         beta = beta, 
        #                         bar_varphi = bar_varphi, 
        #                         bar_dot_varphi = bar_dot_varphi, 
        #                         dot_varphi = dot_varphi, 
        #                         ddot_varphi_d = ddot_varphi_d)
    # State Space Equation
        dot_varphi = dot_varphi
        # [issue]:
        # 这个方程是从勾刺机构的动力学模型反解出$ddot_varphi$
        # 其现实意义是，实验对象的动力学反应。所以这个应该替换成从真实的机器人上的数据吗？
        # 应该并不是！
        ddot_varphi = ((tau_varphi+tau_e) - (self.C*dot_varphi) - (self.N_beta)) / self.M
        # dot_state_var = [dot_varphi, ddot_varphi]
        varphi = dot_varphi * dt
        dot_varphi = ddot_varphi * dt

        return varphi, dot_varphi
# ==================================================
#                       Invariant_Impedance_Controller
# ==================================================
    def invariant_impedance(self, beta, bar_varphi, bar_dot_varphi, dot_varphi, ddot_varphi_d):
        """
            参数含义：
                1. $\tau_{e}$：外力矩，在仿真中施加的外力、干扰，是需要定义的，可以给sin函数；
                2. $\varphi^{d}$：角位置的名义给定值，由控制系统的上位机中发送出去的指令，期望角位置的稳定值；
                3. ${\bar{\varphi}}$：角位置误差的定义，${\bar{\varphi}} = {\varphi^{d}} - {\varphi}$；
                4. $K$：刚度，应满足给定攀爬运动任务要求；
                5. $D$：阻尼，使得闭环动力学系统稳定；
        """
        K_t = 60.0 # > 0，为刚度。只会影响收敛速度
        D_t = self.alpha*self.H + self.varepsilon # 为时变阻尼，为什么取阻尼为常数？
    # 时变阻抗闭环控制器：tau_varphi
        # 方法一：消去tau_e
        # tau_varphi = M*ddot_varphi + C*dot_varphi + N_beta - H*bar_ddot_varphi - D_t*bar_dot_varphi - K_t*bar_varphi
        # 方法二：消去ddot_varphi
        eq_1 = ddot_varphi_d - (1./self.H)*(tau_e - D_t*bar_dot_varphi - K_t*bar_varphi)
        tau_varphi = self.M*(eq_1) + self.C*(dot_varphi) + self.N_beta - tau_e
    # PD
        # tau_varphi = 50*bar_varphi + 25*bar_dot_varphi

        return tau_varphi
# ==================================================
#                       Time-varying_Impedance_Controller
# ==================================================
    def variable_impedance(self, time, beta, bar_varphi, bar_dot_varphi, dot_varphi, ddot_varphi_d):
        """
            参数含义：
                6. $K(t)$：时变刚度，应满足给定攀爬运动任务要求；
                7. $D(t)$：时变阻尼，使得闭环动力学系统稳定；
            即闭环控制问题变为：
                1. 设计控制律$\tau_{\varphi}=\tau_{\varphi}(t)$，使得变体机构原动力学模型(2)的闭环动力学(3)具有期望的稳定动态特性；
                    这里之所以称之为`闭环动力学`是因为在式(3)中采用的输入量是差值，即$\bar{\varphi}$等
                2. 时变刚度$K(t)$应满足给定攀爬运动任务要求；
                    刚度矩阵应该根据机器人攀爬的环境而设计，比如，将要攀爬的是一个坡度变化的表面，那么这个刚度矩阵要怎么设计；在FYN的论文中，刚度矩阵是给定的条件范围内的式子，这个式子仅仅是满足稳定性条件，并没有根据实验对象、实验平台而设计；也正是因为这个理由，所以才选择先进行数值仿真，之后在进行实验平台的验证； 
                3. 时变阻尼$D(t)$应使得：
                    1. 当外力矩$\tau_{e}=0$时，闭环动力学系统(3)的误差状态变量$\bar\varphi$是全局渐近稳定的，即$\lim_{t \rightarrow \infty} \bar{\varphi}=0$；
                    2. 当外力矩$\tau_{e} \neq 0$时，闭环动力学系统(3)的误差状态变量$\bar{\varphi}$是全局稳定的$({\dot{\bar{\varphi}}=0}, {\ddot{\bar{\varphi}}=0})$，即${K(t)}{\bar\varphi}={\tau_{e}}$成立。
        """
        M = (1./3.) * (m_l3) * (l_3**2) # $M$: 假设连杆$L_3$为均质杆，绕$B$点的转动惯量；
        C = 0.25 # $C$为机构的不确定(摩擦)阻尼系数，实际中可取(0, 0.5)；这个就是要考虑参数优化了呗！
        N_beta = (1./2.) * (m_l3*gravity) * (l_3) * (sin(beta)) # $N(\beta)$: 连杆$L_3$关于铰链$B$的有效重力矩；
        # K_t > 0，为时变刚度，连续(即$\|\dot{K}(t)\|$有界)有界
        K_t = 7.0 * sin(2*time) + 35.0
        # $\alpha$、$\varepsilon$与$H$是一起调整的，需要使$D(t)$满足一定的数值才可以
        alpha = 5.0 # > 0，为常数；
        H = 5.0 # > 0，为闭环动力学的惯量，可取为常数；
        varepsilon = 0.1 # > 0，为小常数；
        D_t = alpha*H + varepsilon # 为时变阻尼，为什么取阻尼为常数？数值调大可以让波动平缓一些，也会让曲线上升变缓
    # 时变阻抗闭环控制器：tau_varphi
        # tau_e = 1.0 * sin(time) + 0.5
        eq_1 = ddot_varphi_d - (1./H)*(tau_e - D_t*bar_dot_varphi - K_t*bar_varphi)
        tau_varphi = M*(eq_1) + C*(dot_varphi) + N_beta - tau_e
    # PD
        # tau_varphi = 50*bar_varphi + 25*bar_dot_varphi

        return tau_varphi, M, C, N_beta
# ==================================================
#                                     Impedance Controller
# 相较于仿真算法增加了该函数，但是本质上来说是取代了odeint()
# ==================================================
    def control(self, impedance, varphi, dot_varphi):
    # initial param
        if len(impedance) == 0:
            impedance.update({'t_pre': rospy.Time.now(), 
                                                'varphi': varphi, 
                                                'dot_varphi': dot_varphi})
    # dt = t_cur - t_pre
        impedance['t_cur'] = rospy.Time.now()
        impedance['dt'] = (impedance['t_cur'] - impedance['t_pre']).to_sec()
        # if impedance['dt'] == 0:
        #     return 0
    # calc control value
        # print("y={}, dt={}, varphi_d={}, dot_varphi_d={}, ddot_varphi_d={}".format(
        #             [varphi, dot_varphi], 
        #             impedance['dt'],
        #             self.varphi_d,
        #             self.dot_varphi_d,
        #             self.ddot_varphi_d))
        # y=[0.1511163481899077, 0.0], dt=7.7963e-05, varphi_d=0.249509666063, dot_varphi_d=0.0, ddot_varphi_d=0.0
        varphi, dot_varphi = self.inverse_dynamics(
                                            y=[impedance['varphi'], impedance['dot_varphi']], 
                                            dt=impedance['dt'], 
                                            varphi_d=self.varphi_d, 
                                            dot_varphi_d=self.dot_varphi_d, 
                                            ddot_varphi_d=self.ddot_varphi_d)
    # update
        impedance['t_pre'] = impedance['t_cur']
        impedance['varphi'] += varphi
        impedance['dot_varphi'] += dot_varphi

        return varphi, dot_varphi
# ==================================================
#                                               Update
# ==================================================
    def update(self, theta, dot_theta):
        '''
            :param [0]: 机器人的实际位置
            :param [1]: 机器人的实际速度

            :param self.impedance: 初始化算法参数
        '''
        print("01 theta={}, dot_theta={}".format(theta, dot_theta))
        if self.Button:
        # kinematic
            __, __, varphi, dot_varphi, __ = self.kinematics(l_0, l_1, l_2, l_3, theta, dot_theta, ddot_theta=0)
            print("02 varphi={}, dot_varphi={}".format(varphi, dot_varphi))
        # dervatives
            varphi, dot_varphi = self.control(self.impedance, varphi, dot_varphi)
            print("03 varphi={}, dot_varphi={}".format(varphi, dot_varphi))
            print("03_1 self.impedance={}".format(self.impedance))
        # inv kinematic
            __, __, theta, dot_theta, __ = self.inverse_kinematics(l_0, l_1, l_2, l_3, varphi, dot_varphi, ddot_varphi=0)
            print("04 theta={}, dot_theta={}".format(theta, dot_theta))

        return theta, dot_theta

# %% main
def main():
    print('AlgorithmImpedanceClass')

if __name__ == '__main__':
    main()