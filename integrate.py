#!/usr/bin/env python

from random import uniform as rand
from scipy.integrate import quad as integrate
from scipy.optimize import minimize_scalar
from math import pi
from math import sin
import matplotlib.pyplot as plt


def tempFunc(x):
    return 2*x**2 + 3*x + 1


def integrate_mc(f, bounds, n):

    # obtain domain of the integral
    a = min(bounds)
    b = max(bounds)

    # determine the minimum and maximum value of the function
    c = minimize_scalar(f, bounds=bounds, method='bounded').fun
    d = -minimize_scalar(lambda x: -f(x), bounds=bounds, method='bounded').fun

    # calculate the area of the bounding box
    A = (b-a) * (d-c)

    # variable to store points within the curve
    count = 0

    # loop for the number of samples
    for i in range(n):

        # get random pint
        x = rand(a, b)
        y = rand(c, d)

        # if the point is under the curve and positive add one
        if (y > 0 and f(x) > y):
            count += 1
        # if the point is above the curve and less than zero, remove one as it is "negative" area
        elif (y < 0 and f(x) < y):
            count -= 1

    # area ratio
    p = count/n

    # rectangle area times area ratio
    return A*p


def plotError(f, bounds, n):

    # calculate the exact definite integral
    exact = integrate(f, min(bounds), max(bounds))[0]

    # create an array of the exact value to plot
    exact = [exact for i in range(1, n)]

    # generate an array of approximate integrals with increasing sample size
    approx = [integrate_mc(f, bounds, i) for i in range(1, n)]

    # plot the approximate and exact results
    plt.plot([i for i in range(1, n)], approx)
    plt.plot([i for i in range(1, n)], exact)

    # plot details
    plt.legend(['Monte Carlo', 'Exact Solution'])
    plt.title('Integral Approximation of 2*x^2 + 3*x + 1 from 0 to 10')
    plt.xlabel('Number of estimations')
    plt.ylabel('Area Under the Curve')

    # show the plot
    plt.show()
    
    


if __name__ == "__main__":
    
    bounds = [0, 10]
    
##    print("HW:", integrate_mc(tempFunc, bounds, 10000))
##    print("Built in:", integrate(tempFunc, bounds[0], bounds[1]))
    plotError(tempFunc, bounds, 500)
