import matplotlib.pyplot as plt
import numpy as np
from bueze import bueze
from matplotlib.animation import FuncAnimation


class Point:
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def multiple(self, k):
        return Point(self.x * k, self.y * k)

    def add(self, other):
        return Point(self.x + other.x, self.y + other.y)


def function(x):
    return 4 * x ** 5 - 3 * x ** 3 + x ** 2 + 5


def init():
    line.set_data([], [])
    return line,


def animate(i):
    p0 = Point(0, 0)
    p1 = Point(1, 3 + i / 10)
    p2 = Point(3, -3)
    p3 = Point(4, 0)
    points = [p0, p1, p2, p3]
    ydata = []

    truey = []
    for point1 in points:
        truey.append(point1.y)

    linex = []
    liney = []
    for point1 in points:
        linex.append(point1.x)
        liney.append(point1.y)

    for x in xdata:
        ydata.append(bueze(points, x, xdata[-1]).y)

    x = xdata[int(len(xdata) * i / 50)]
    point.set_offsets([x, bueze(points, x, xdata[-1]).y])
    fourier.set_data(xdata, ydata)

    return point,


xdata = np.arange(0, 4.05, 0.05)

fig = plt.figure()
ax = plt.axes(xlim=(xdata[0], xdata[-1]), ylim=(-2, 10))
ax.grid()
fourier, = ax.plot([], [], lw=3)
line, = ax.plot([], [], lw=3)
point = ax.scatter(1, 2, c='r')

anim = FuncAnimation(fig, animate, init_func=init, frames=50, interval=20, blit=True)

anim.save('sine_wave.gif', 'pillow')
