#!/usr/bin/env python

from numpy import linspace
from random import randint
from scipy.optimize import minimize_scalar
import matplotlib.pyplot as plt

from math import sin
from math import cos




def tempFunc(a):

    return (a**3 - 10*a**2 - 9*a + 100)/(sin(a)+2)

def bad(a):

    return sin(a)

def good(a):

    return a**2


def optimize_step(f, bounds, n):

    # create array of steps
    step = linspace(min(bounds), max(bounds), n)

    # initialize variables
    val = 0
    x = 0

    # run though the steps
    for i in step:
        temp = f(i)

        # check if new max is found
        if temp > val:
            val = temp
            x = i

    # return the max value and its associated x value
    return x#, val


def optimize_random(f, bounds, n):

    # create array of steps (random number of steps)
    step = linspace(min(bounds), max(bounds), randint(0, n))

    # initialize variables
    val = 0
    x = 0

    # run though the steps
    for i in step:
        temp = f(i)

        # check if new max is found
        if temp > val:
            val = temp
            x = i

    # return the max value and its associated x value
    return x#, val


def test(f, bounds, n):

    # calculate the max value with the built in function
    builtIn = minimize_scalar(lambda x: -f(x), bounds=bounds, method='bounded').x

    # create an array of the value
    builtIn = [builtIn for i in range(n)]

    # generate an array of approximate values for step and random approach
    step = [optimize_step(f, bounds, x) for x in range(n)]
    randy = [optimize_random(f, bounds, x) for x in range(n)]

    # plot the results
    plt.plot([i for i in range(n)], builtIn)
    plt.plot([i for i in range(n)], step)
    plt.plot([i for i in range(n)], randy)

    # plot details
    plt.legend(['Built In', 'Step', 'Random'])
    plt.title('Optimization Tests')
    plt.xlabel('Number of Tests')
    plt.ylabel('x value of max f(x)')

    # show plot
    plt.show()


if __name__ == '__main__':

    bou = [-10, 10]
    res = 100


    test(tempFunc, bou, res)
    test(bad, bou, res)
    test(good, bou, res)
