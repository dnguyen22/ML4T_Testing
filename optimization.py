"""Minimize an objective function, using  SciPy"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as spo


def f(X):
    """Given a scalar X, return some value (a real number)."""
    Y = (X - 1.5)**2 + 0.5
    print("X = {}, Y ={}".format(X, Y))  # Used for tracing
    return Y


def error(line, data):
    """Compute error between given line model and observed data.
    
    Parameters
    ----------
    line: tuple/list/array (C0, C1) where C0 is slope and C1 is Y-intercept
    data: 2D array where each row is a point (x,y)
    
    Returns error as a single real value.
    """
    # Metric: Sum of squared Y axis differences
    err = np.sum((data[:, 1] - (line[0] * data[:, 0] + line[1])) ** 2)
    return err
    
    
def fit_line(data, error_func):
    """Fit a line to given data, using a supplied error function.
    
    Parameters
    ----------
    data: 2D array where each row is a point (X0, Y)
    error_func: function that computes the error between a line and observed data
    
    Returns line that minimizes the error function.
    """
    # Generate initial guess for line model
    l = np.float32([0, np.mean(data[:,1])])  # Slope = 0, intercept = mean(y-values)
    
    # Plot initial guess (optional)
    x_ends = np.float32([-5, 5])
    plt.plot(x_ends, l[0] * x_ends + l[1], 'm--', linewidth=2.0, label='Initial guess')
    
    # Call optimizer to minimize error function
    result = spo.minimize(error_func, l, args=(data,), method='SLSQP', options={'disp': True})
    return result.x
    
    
if __name__ == "__main__":
    # Define original line
    l_orig = np.float32([4, 2])
    print("Original line: C0 = {}, C1 = {}".format(l_orig[0], l_orig[1]))
    Xorig = np.linspace(0, 10, 21)
    Yorig = l_orig[0] * Xorig + l_orig[1]
    plt.plot(Xorig, Yorig, 'b-', linewidth=2.0, label="Original line")
    
    # Generate noisy data points
    noise_sigma = 3.0
    noise = np.random.normal(0, noise_sigma, Yorig.shape)
    data = np.asarray([Xorig, Yorig + noise]).T
    plt.plot(data[:,0], data[:,1], 'go', label="Data points")
    
    # Try to fit aline to this dat
    l_fit = fit_line(data, error)
    print("Fitted line: C0 = {}, C1 = {}".format(l_fit[0], l_fit[1]))
    plt.plot(data[:, 0], l_fit[0] * data[:, 0] + l_fit[1], 'r--', linewidth=2.0, label='Fitted line')
    
    # Add a legend and show plot
    plt.title("Fit line")
    plt.legend()
    plt.show()
    
    """
    Xguess = 2.0
    min_result = spo.minimize(f, Xguess, method="SLSQP", options={'disp': True})
    print("Minima found at:")
    print("X = {}, Y = {}".format(min_result.x, min_result.fun))
    
    # Plot function values, mark minima
    Xplot = np.linspace(0.5, 2.5, 21)
    Yplot = f(Xplot)
    plt.plot(Xplot, Yplot)
    plt.plot(min_result.x, min_result.fun, 'ro')
    plt.title("Minima of an objective function")
    plt.show()
    """
