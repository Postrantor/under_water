#! /usr/bin/env python
# -*- coding:utf-8 -*-
'''md
    [20210827]:
    [README]:
        [How to do real time data processing using Python Kalman Filter and Average moving filter - YouTube](https://www.youtube.com/watch?v=VBfqrTOL6z0)
        [lblackhall/pyconau2016: Code for my talk at PyconAU 2016](https://github.com/lblackhall/pyconau2016)
        --- --- ---
        This code complements the talk "Working with Real Time Data Streams for IoT Devices"
        given by Lachlan Blackhall at PyCONAU 2016 in Melbourne Australia.
        A basic implementation of both a moving average filter and a Kalman filter are contained
        and the demonstration can be run by executing filtering_demo.py
        --- --- ---
        该程序的执行效果与`DR_CAN`的后验估计值一样
'''

# %% class


class SingleStateKalmanFilter(object):

    def __init__(self, x, P, A, B, C, Q, R):
        self.current_state_estimate = x  # Current state estimate
        self.current_prob_estimate = P  # Current probability of state estimate
        self.A = A  # Process dynamics
        self.B = B  # Control dynamics
        self.C = C  # Measurement dynamics
        self.Q = Q  # Process covariance
        self.R = R  # Measurement covariance

    def current_state(self):
        return self.current_state_estimate

    def step(self, control_input, measurement):
        # Prediction step
        predicted_state_estimate = self.A * self.current_state_estimate + self.B * control_input
        predicted_prob_estimate = (self.A * self.current_prob_estimate) * self.A + self.Q

        # Observation step
        innovation = measurement - self.C * predicted_state_estimate
        innovation_covariance = self.C * predicted_prob_estimate * self.C + self.R

        # Update step
        kalman_gain = predicted_prob_estimate * self.C * 1 / float(innovation_covariance)
        self.current_state_estimate = predicted_state_estimate + kalman_gain * innovation

        # eye(n) = nxn identity matrix.
        self.current_prob_estimate = (1 - kalman_gain * self.C) * predicted_prob_estimate

        return self.current_state_estimate
        # 将 current_state()函数合并到此


'''
    import numpy as np
    from pylab import ylim, title, ylabel, xlabel
    import matplotlib.pyplot as plt
    from kalman import SingleStateKalmanFilter
    from moving_average import MovingAverageFilter

    # Create some random temperature data
    measurements = np.asarray([60, 90, 50, 50, 30, 90, 90, 50, 70, 60, 40, 70, 70, 60, 70, 20, 90, 70, 50, 60, 80, 80, 80, 40, 80, 50, 50, 70, 40, 50, 60. -10, 70, 60, 30, 10, 40, 40, 80, 70, 50, 80, 20, 80, 70, 50, 50, 90, 60])

    # Initialise the Kalman Filter
    A = 1.0  # No process innovation
    C = 1.0  # Measurement
    B = 0.0  # No control input
    Q = 0.001  # Process covariance
    R = 10.0  # Measurement covariance
    x = measurements[0]  # Initial estimate
    P = 1.0  # Initial covariance

    kalman_filter = SingleStateKalmanFilter(A, B, C, x, P, Q, R)

    # Initialise two moving average filters with different window lengths
    ma5_filter = MovingAverageFilter(5)
    ma50_filter = MovingAverageFilter(50)

    # Empty lists for capturing filter estimates
    kalman_filter_estimates = []
    ma5_filter_estimates = []
    ma50_filter_estimates = []

    # Simulate the data arriving sequentially
    for data in measurements:
        ma5_filter.step(data)
        ma5_filter_estimates.append(ma5_filter.current_state())

        ma50_filter.step(data)
        ma50_filter_estimates.append(ma50_filter.current_state())

        kalman_filter.step(0, data)
        kalman_filter_estimates.append(kalman_filter.current_state())


    # Plot the Data for Presentation
    plt.figure(figsize=(20, 5))
    plt.plot(measurements, 'r', linewidth=2.0)
    # plt.plot(ma5_filter_estimates, 'b', linewidth=2.0)
    # plt.plot(ma50_filter_estimates, 'g', linewidth=2.0)
    plt.plot(kalman_filter_estimates, 'k', linewidth=2.0)
    labels = ["measurements", "ma5_filter_estimates", "ma50_filter_estimates", "kalman_filter_estimates"]
    plt.legend(labels=labels)

    # Show the plot
    plt.show()
'''
