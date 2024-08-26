# -*- coding:utf-8 -*-
'''README
[README]:
    Table 2: initial conditions on velocities and posture of reference and mobile robot
'''
# %% import
# Math
from numpy import matrix, pi


# %% trajectory
class TrajectoryClass(object):
    '''
    The reference trajectory is generated using the reference model (12), depending on the reference velocities v_{r} and \omega_{r}, and the initial errors of position and heading direction are assumed to exist as several scenarios in Table II. Here, the reference trajectories of each scenario are:
        1) a straight line;
        2) a point outside the origin;
        3) a curve;
        4) a circle;
        5) a path toward the origin; and
        6) a straight line with initial robot position at origin.
    '''
    def postrure_select(self, pos='line'):
        '''参考轨迹'''
        if pos == 'line':
            self.posture_line()
        if pos == 'point':
            self.posture_point()
        if pos == 'curve':
            self.posture_curve()
        if pos == 'circle':
            self.posture_circle()
        if pos == 'posture_circle_actual':
            self.posture_circle_actual()
        if pos == 'orign':
            self.posture_orign()
        if pos == 'initial_orign':
            self.posture_initial_orign()

    def state_variable(self, q, z):
        q = matrix([
            [q[0]],
            [q[1]],
            [q[2]],
        ])
        z = matrix([
            [z[0]],
            [z[1]],
        ])
        return q, z

    def posture_line(self):
        '''
        1) a straight line;
        '''
        q_c = [1.5, pi / 2, pi / 4]
        z_c = [0., 0.]
        q_r = [1., pi / 4, pi / 4]
        z_r = [.2, 0.]
        self.q_c, self.z_c = self.state_variable(q_c, z_c)
        self.q_r, self.z_r = self.state_variable(q_r, z_r)

    def posture_point(self):
        '''
        2) a point outside the origin; 
        '''
        q_c = [37.3, 2.38, -0.38]
        z_c = [0., 0.]
        q_r = [20., 0, pi / 2]
        z_r = [0., 0.]
        self.q_c, self.z_c = self.state_variable(q_c, z_c)
        self.q_r, self.z_r = self.state_variable(q_r, z_r)

    def posture_curve(self):
        '''
        3) a curve; 
        '''
        q_c = [7.3, 2.38, -0.38]
        z_c = [0., 0.]
        self.q_c, self.z_c = self.state_variable(q_c, z_c)
        q_r = [1., pi / 4, pi / 2]
        z_r = [5., -0.1]
        self.q_r, self.z_r = self.state_variable(q_r, z_r)

    def posture_circle_actual(self):
        '''
        4) a circle;
        '''
        q_c = [35, pi / 4, -pi / 4]
        z_c = [0., 0.]
        q_r = [35., pi / 4, -pi / 4]
        z_r = [12./20., 0.8/20.]
        self.q_c, self.z_c = self.state_variable(q_c, z_c)
        self.q_r, self.z_r = self.state_variable(q_r, z_r)

    def posture_circle(self):
        '''
        4) a circle;
        '''
        q_c = [37.3, 2.38, -0.38]
        z_c = [0., 0.]
        q_r = [35., pi / 4, -pi / 4]
        z_r = [12., 0.8]
        self.q_c, self.z_c = self.state_variable(q_c, z_c)
        self.q_r, self.z_r = self.state_variable(q_r, z_r)

    def posture_orign(self):
        '''
        5) a path toward the origin; and 
        '''
        q_c = [17.3, 2.38, -0.38]
        z_c = [0., 0.]
        self.q_c, self.z_c = self.state_variable(q_c, z_c)
        q_r = [30., pi / 4, pi / 4]
        z_r = [-5., 0.]
        self.q_r, self.z_r = self.state_variable(q_r, z_r)

    def posture_initial_orign(self):
        '''
        6) a straight line with initial robot position at origin.
        '''
        q_c = [0.1, 0.1, 0.1]  # 文章中为零
        z_c = [0., 0.]
        self.q_c, self.z_c = self.state_variable(q_c, z_c)
        q_r = [25., pi / 2, 0.]
        z_r = [4., 0.]
        self.q_r, self.z_r = self.state_variable(q_r, z_r)
