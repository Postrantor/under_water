# -*- coding:utf-8 -*-

# %% import
from math import fabs
from numpy import sin, cos, matrix, diag, absolute, sign, tanh, exp

# %%
Q = diag([10., 10.])
P = diag([1., 1.])
k_0 = 1.1
K_pos = diag([1.8, 1.8, 2.])  # line
# K_pos = diag([1., 1., .002])  #point
# K_pos = diag([2., 2., .5])  #curve
# K_pos = diag([4., 4., 1.])  #circle
# K_pos = diag([5., 5., .002])  #orign 需要检测 rho_varphi
# K_pos = diag([1., 1., 1.5])  #initial_orign
K_head = diag([0, 2])

# Q = diag([10., 10.])
# P = diag([1., 1.])
# k_0 = 1.1
# K_pos = diag([2., 2., .002])
# K_head = diag([0, 2])


# %%
class ControllerPositionClass(object):

    def sgn(self, x):
        # return tanh(x)
        # return sign(x)
        return (x) / (2. + absolute(x))
        # return 1./(1.+exp(-x))

    def matrix_q(self, q_r, q_c):
        q_e = q_c - q_r
        return q_e

    def matrix_S_inv(self, dev, q):
        q_1, q_2, q_3 = q[0, 0], q[1, 0], q[2, 0]
        if dev >= 0:
            sgn = diag([1, 1])
        if dev < 0:
            sgn = diag([1, -1])
        S_inv = matrix([
            [(cos(q_2 - q_3)), (-q_1 * sin(q_2 - q_3)), (0)],
            [(sin(q_2 - q_3)), (q_1 * cos(q_2 - q_3)), (1)],
        ])
        return sgn * S_inv

    def sliding_func(self, S_inv_c, k_0, q_c, q_e, dot_q_e):
        s_q = dot_q_e + K_pos * q_e  # @式(14)
        s_sgn = diag([k_0, (k_0 / q_c[0, 0]), 0]) * \
            self.sgn(q_e) * \
            fabs(s_q[2, 0])  # s_theta
        s = S_inv_c * (s_q + s_sgn)  # @式(17)
        s_temp = S_inv_c * s_sgn
        # d_s_temp = (s_temp - s_temp_prev) / delta_t
        return s, s_temp

    def controller_position(self, q_e, dot_q_r, S_inv_c, S_inv_r, Q, P, s,
                            s_temp, delta_t):
        '''已经积分'''
        u_init =\
            S_inv_c * (dot_q_r - K_pos * q_e) * 2
        # +S_inv_c * (dot_q_r - K * q_e)
        -S_inv_r * dot_q_r * 2
        # -S_inv_r * dot_q_r
        -Q * s * delta_t
        -P * self.sgn(s) * delta_t
        -s_temp  # 这里直接去掉了 delta_t
        return u_init

    def Position(self, q_c, dot_q_c, q_r, dot_q_r, delta_t):
        q_e = self.matrix_q(q_r, q_c)
        dot_q_e = self.matrix_q(dot_q_r, dot_q_c)
        # ---
        S_inv_c = self.matrix_S_inv(self.z_r[0, 0], q_c)
        S_inv_r = self.matrix_S_inv(self.z_r[0, 0], q_r)
        # ---
        s, s_temp = self.sliding_func(S_inv_c, k_0, q_c, q_e, dot_q_e)
        # ---
        u_init = self.controller_position(q_e, dot_q_r, S_inv_c, S_inv_r, Q, P,
                                          s, s_temp, delta_t)
        return u_init


# %%
class ControllerHeadingClass(object):

    def sgn(self, x):
        return tanh(x)
        # return sign(x)
        # return (x)/(2.+absolute(x))
        # return 1./(1.+exp(-x))

    def Heading(self, q_c, q_r, dot_q_c, dot_q_r, delta_t):
        """
        航向控制器：在位置跟踪误差足够小且参考轨迹不移动的情况下保证渐近航向方向跟踪。
        当参考轨迹不改变其位置时，上述位置控制器不能保证航向方向跟踪误差为零，因此需要另一个航向方向控制器。当位置控制器的位置跟踪误差变得足够小并且参考轨迹的位置没有改变时，该控制器需要激活。使用滑动面 @式(34) 代替前面设计的滑模面 @式(17) 或 @式(32)，控制输入 uu 可以类似地从 @式(22) 开始设计为 @式(35)。
        """
        transform = matrix([[0, 0, 0], [0, 0, 1]])
        q_e = transform * (q_c - q_r)
        dot_q_e = transform * (dot_q_c - dot_q_r)

        s = dot_q_e + K_head * q_e  # s = s_q
        print(q_e)
        u_init = \
            -K_head * q_e
        -Q * s * delta_t
        -P * self.sgn(s) * delta_t

        return u_init


# %%
