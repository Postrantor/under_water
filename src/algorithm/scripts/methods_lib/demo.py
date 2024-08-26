import numpy as np
from pylab import ylim, title, ylabel, xlabel
import matplotlib.pyplot as plt
from kalman import SingleStateKalmanFilter
from moving_average import MovingAverageFilter

# Create some random temperature data
measurements = np.asarray([60, 90, 50, 50, 30, 90, 90, 50, 70, 60, 40, 70, 70, 60, 70, 20, 90, 70, 50, 60, 80, 80, 80, 40, 80, 50, 50, 70, 40, 50, 60. - 10, 70, 60, 30, 10, 40, 40, 80, 70, 50, 80, 20, 80, 70, 50, 50, 90, 60])

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
