import matplotlib.pyplot as plt
import numpy as np
from scipy import integrate
import scipy
from calculator import *
from matplotlib.animation import FuncAnimation
import sys

def f(t, r, args):
    g, m1, m2 = args
    return [r[1], (g*r[0]/(math.sqrt(r[0]**2+r[2]**2)))*(m2 - m1), r[3], (g*r[2]/(math.sqrt(r[0]**2+r[2]**2)))*(m2 - m1)]

g, m1, m2 = 6.67408 *10 ** -11, 2.0, 2.0
args = (g, m1, m2)
t = np.linspace(0, 80, 10000)
y0 = [-1.0, 1.0, 1.0, 0.0]

r = integrate.ode(f)
r.set_integrator('lsoda')
r.set_initial_value(y0, t[0])
r.set_f_params(args)


dt = t[1] - t[0]
idx = 0
y = np.zeros((len(t), len(y0)))
while r.successful() and r.t < t[-1]:
    y[idx,:] = r.y
    r.integrate(r.t+dt)
    idx += 1


plt.show()

' we are in mixed wood plane'
' describe two or 3 thing that , maple, oak,  '



