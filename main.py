import matplotlib.pyplot as plt
import numpy as np
import math
from fourier_rows import fourier_rows
from matplotlib.animation import FuncAnimation


def function(x):
    return 4 * x ** 5 - 3 * x **3 + x ** 2 + 5


def init():
    line.set_data([], [])
    return line,


def animate(i):
    ydata = []
    for x in xdata:
        ydata.append(fourier_rows(function, xdata[0], xdata[-1], int(i), x))

    line.set_data(xdata, truey)
    fourier.set_data(xdata, ydata)

    return line,


xdata = np.arange(-math.pi,  math.pi, 0.05)

truey = []
for x in xdata:
    truey.append(function(x))

fig = plt.figure()
ax = plt.axes(xlim=(xdata[0], xdata[-1]), ylim=(min(*truey) * 1.1, max(*truey) * 1.1))
fourier, = ax.plot([], [], lw=3)
line, = ax.plot([], [], lw=3)

anim = FuncAnimation(fig, animate, init_func=init, frames=15, interval=80, blit=True)

anim.save('sine_wave.gif', 'pillow')
