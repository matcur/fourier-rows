from matplotlib import pyplot as plt
import numpy as np


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def multiply(self, k):
        return Point(self.x * k, self.y * k)

    def sum(self, other):
        return Point(self.x + other.x, self.y + other.y)


def lerp(p0, p1, t):
    return p0.multiply(1 - t).sum(p1.multiply(t))


def bezie(points, t):
    if len(points) == 1:
        return points[0]

    lerps = []
    for i in range(0, len(points) - 1):
        lerps.append(lerp(points[i], points[i + 1], t))

    return bezie(lerps, t)


a1 = Point(0, -5)
a2 = Point(2, 5)
a3 = Point(4, -5)
a4 = Point(6, 5)
points = [a1, a2, a3, a4]

ts = np.arange(0, 1.01, 0.01)
xdata = []
ydata = []
for t in ts:
    point = bezie(points, t)
    ydata.append(point.y)
    xdata.append(point.x)

fig = plt.figure()
ax = fig.add_subplot()
ax.plot(xdata, ydata)
for point in points:
    ax.scatter(point.x, point.y)

plt.show()
