import matplotlib.pyplot as plt
import numpy as np


def lerp(p1, p2, t):
    return p1.multiple(1 - t).add(p2.multiple(t))


def lerps(points, t):
    deep_points = []
    for i in range(0, len(points) - 1):
        deep_points.append(lerp(points[i], points[i + 1], t))

    if len(deep_points) == 1:
        return deep_points[0]

    return lerps(deep_points, t)


def bueze(points, x, xmax):
    t = x / xmax

    return lerps(points, t)
