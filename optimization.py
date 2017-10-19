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


if __name__ == "__main__":
    Xguess = 2.0
    min_result = spo.minimize(f, Xguess, method="SLSQP", options={'disp': True})
    print("Minima found at:")
    print("X = {}, Y = {}".format(min_result.x, min_result.fun))
    
    # Plot function values, mark minima
    Xplot = np.linspace(0.5, 2.5, 21)
    Yplot = f(Xplot)
    plt.plot(Xplot, Yplot)
    plt.title("Minima of an objective function")
    plt.show()
