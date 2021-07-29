import matplotlib.pyplot as plt
import numpy as np
import math
from fourier_rows import fourier_rows


def function(x):
    return 3 * x**3 - 2 * x**2 + 1


xdata = np.arange(-math.pi,  math.pi, 0.05)
ydata = []
for x in xdata:
    ydata.append(fourier_rows(function, xdata[0], xdata[-1], 9, x))

truey = []
for x in xdata:
    truey.append(function(x))

plt.plot(xdata, ydata)
plt.plot(xdata, truey)
plt.grid()
plt.show()

print(ydata)
