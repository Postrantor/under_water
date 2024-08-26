# -*- coding:utf-8 -*-

# %% import
import time, os
# Math
# import pandas as pd
import numpy as np
from numpy import absolute, sin, cos, matrix, pi
# Scripts
from controller_sliding import ControllerPositionClass, ControllerHeadingClass
from trajectory import TrajectoryClass

# %% Param
delta_t = 1. / 20.  # 0.001  # 时间间隔
iteration = 400  # 迭代
density = 50  # 图像点的密度
pos_type = 'orign'  # 'line', 'point', 'curve', 'circle', 'orign', 'initial_orign', 'posture_circle_actual'
save2csv = True
save2figure = False


# %% 轨迹跟踪仿真流程
class Trajectory_Tracking_SMC(ControllerPositionClass, ControllerHeadingClass,
                              TrajectoryClass):
    ''''''

    def __init__(self):
        self.postrure_select(pos_type)
        #
        self.q_c_prev = self.q_c
        self.q_r_prev = self.q_r

    # %%
    def trajectory(self, z, q_prev, delta_t):
        '''
        :param S_q:
        :param z:
        '''
        rho = q_prev[0, 0]
        phi = q_prev[1, 0]
        theta = q_prev[2, 0]
        S_q = matrix([
            [cos(phi - theta), 0],
            [-(1 / rho) * sin(phi - theta), 0],
            [0, 1],
        ])  #@式(12)
        dot_q = S_q * z
        q = q_prev + dot_q * delta_t
        return q, dot_q

    def controller(self, q_c, dot_q_c, q_r, dot_q_r, delta_t):
        '''
        还需要补一个姿态控制器，在机器人停止运动的时候校正姿态
        '''
        u_init = self.Position(q_c, dot_q_c, q_r, dot_q_r, delta_t)
        self.z_c = self.z_r + u_init  # @式(21)
        if self.z_c[0, 0] > .6: self.z_c[0, 0] = .6
        if self.z_c[0, 0] <= -.6: self.z_c[0, 0] = -.6

    # %%
    def update(self, q_c, q_r):
        self.q_c_prev = q_c
        self.q_r_prev = q_r

    def coordinate(self, rho, theta):
        return (rho * cos(theta)), (rho * sin(theta))

    def data_array(self, q_c, q_r):
        x_r, y_r = self.coordinate(q_r[0, 0], q_r[1, 0])
        x_c, y_c = self.coordinate(q_c[0, 0], q_c[1, 0])

    # %%
    def spin(self):
        for num in range(iteration):
            q_c, dot_q_c = self.trajectory(self.z_c, self.q_c_prev, delta_t)
            q_r, dot_q_r = self.trajectory(self.z_r, self.q_r_prev, delta_t)
            self.controller(q_c, dot_q_c, q_r, dot_q_r, delta_t)
            self.update(q_c, q_r)

            # self.data_array(q_c, q_r)


# %% main
def main():
    trajectory = Trajectory_Tracking_SMC()
    trajectory.spin()


if __name__ == "__main__":
    main()
