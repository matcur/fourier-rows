import scipy.integrate as integrate
import math


def a0(fun, start_period, end_period, l):
    return fourier_coefficient(fun, start_period, end_period, 0, lambda x: -1, l)


def an(fun, start_period, end_period, n, l):
    return fourier_coefficient(fun, start_period, end_period, n, math.cos, l)


def bn(fun, start_period, end_period, n, l):
    return fourier_coefficient(fun, start_period, end_period, n, math.sin, l)


def fourier_coefficient(fun, start_period, end_period, n, trig, l):
    return 1 / l * integrate.quad(
        lambda _x: fun(_x) * trig(_x * n * math.pi / l), start_period, end_period
    )[0]


def fourier_row(n, x, an, bn, l):
    return an * math.cos(n * x * math.pi / l) + bn * math.sin(n * x * math.pi / l)


def fourier_rows(fun, start_period, end_period, n, x):
    l = (end_period - start_period) / 2
    _a0 = a0(fun, start_period, end_period, l) / 2
    rows = 0

    _an = lambda _n: an(fun, start_period, end_period, _n, l)
    _bn = lambda _n: bn(fun, start_period, end_period, _n, l)

    for i in range(n):
        rows += fourier_row(i, x, _an(i), _bn(i), l)

    return _a0 + rows