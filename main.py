import matplotlib.pyplot as plt
import numpy
import numpy as np
import scipy.integrate as integrate
import math


def function(x):
    return x**3 - 2 * x**2 + 1


def a0(fun, start_period, end_period):
    return fourier_coefficient(fun, start_period, end_period, 0, lambda x: -1)


def an(fun, start_period, end_period, n):
    return fourier_coefficient(fun, start_period, end_period, n, math.cos)


def bn(fun, start_period, end_period, n):
    return fourier_coefficient(fun, start_period, end_period, n, math.sin)


def fourier_coefficient(fun, start_period, end_period, n, trig):
    return 1 / math.pi * integrate.quad(
        lambda _x: fun(_x) * trig(_x * n), start_period, end_period
    )[0]


def fourier_row(n, x, an, bn):
    return an * math.cos(n * x) + bn * math.sin(n * x)


def fourier_rows(fun, start_period, end_period, n, x):
    _a0 = a0(fun, start_period, end_period) / 2
    rows = 0

    _an = lambda _n: an(fun, start_period, end_period, _n)
    _bn = lambda _n: bn(fun, start_period, end_period, _n)

    for i in range(n):
        rows += fourier_row(i, x, _an(i), _bn(i))

    return _a0 + rows


xdata = numpy.arange(-math.pi, math.pi, 0.1)
ydata = []

for x in xdata:
    ydata.append(fourier_rows(function, -math.pi, math.pi, 9, x))

truey = []
for x in xdata:
    truey.append(function(x))

plt.plot(xdata, ydata)
plt.plot(xdata, truey)
plt.show()

print(ydata)
