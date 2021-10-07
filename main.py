import matplotlib.pyplot as plt
import numpy as np
import math
from fourier_rows import fourier_rows
from bueze import bueze, Point
from matplotlib.animation import FuncAnimation


def function(x):
    return 4 * x ** 5 - 3 * x ** 3 + x ** 2 + 5


def init():
    line.set_data([], [])
    return line,


def animate(i):
    p0 = Point(0, 0)
    p1 = Point(1, 3 + i / 10)
    p2 = Point(3 - i / 20, 3 - i / 10)
    p3 = Point(4, 0)
    points = [p0, p1, p2, p3]
    ydata = []

    truey = []
    for point in points:
        truey.append(point.y)

    linex = []
    liney = []
    for point in points:
        linex.append(point.x)
        liney.append(point.y)

    for x in xdata:
        ydata.append(bueze(points, x, xdata[-1]).y)

    fourier.set_data(xdata, ydata)

    return line,


xdata = np.arange(0, 4.05, 0.05)

fig = plt.figure()
ax = plt.axes(xlim=(xdata[0], xdata[-1]), ylim=(-2, 10))
fourier, = ax.plot([], [], lw=3)
line, = ax.plot([], [], lw=3)

anim = FuncAnimation(fig, animate, init_func=init, frames=50, interval=20, blit=True)

anim.save('sine_wave.gif', 'pillow')
