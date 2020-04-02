import matplotlib.pyplot as plt
import numpy as np
from scipy import integrate

def f(t, y):
    return [y[1], 2*np.sin(3*t)-10*y[0]-2*y[1]]

t = np.linspace(0, 10, 1000)
y0 = [1, 0]

r = integrate.ode(f)
r.set_integrator('lsoda')
r.set_initial_value(y0, t[0])

# This would store the vaule
dt = t[1] - t[0]
idx = 0
y = np.zeros((len(t), len(y0)))
while r.successful() and r.t < t[-1]:
    y[idx,:] = r.y
    r.integrate(r.t+dt)
    idx += 1

plt.plot(t,y[:,1])
plt.show()
