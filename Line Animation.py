import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
import sys
from scipy import integrate
import scipy
from calculator import *
'''
x_data = []
y_data = []

fig, ax = plt.subplots()
# This sets the frame limit.
ax.set_xlim(0, 105)
ax.set_ylim(0, 105*10)
line, = ax.plot(0, 0)


def animation_frame(i):
    x_data.append(i)
    y_data.append(i * 10)

    line.set_xdata(x_data)
    line.set_ydata(y_data)
    return line,  # Remeber this line

a = []
for x in range(105):
    a.append(x)

animation = FuncAnimation(fig, func=animation_frame, frames=a, interval=10)
plt.show()
'''
