import matplotlib.pyplot as plt
import numpy as np
from scipy import integrate
import scipy
from calculator import *
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D
import sys

calculator = Calculator()
def f(t, y, args):
    m1 ,m2, g, l1, l2 = args
    return [y[1],(-g*(2*m1+m2)*np.sin(y[0])-m2*g*np.sin(y[0]-2*y[2])-2*np.sin(y[0]-y[2])*m2*(y[3]**2*l2 +y[1]**2*l2*np.cos(y[0]-y[2])))/(l1*(2*m1+m2-m2*np.cos(2*y[0]-2*y[2]))),y[3],( 2*np.sin(y[0]-y[2])*(y[1]**2*l1*(m1+m2)+g*(m1+m2)*np.cos(y[0])+y[3]**2*l2*m2*np.cos(y[0]-y[2])))/(l2*(2*m1+m2-m2*np.cos(2*y[0]-2*y[2])))]

m1,l1, g = 1.0, 1.0, 9.8
m2,l2 = 1.0, 1.0
y0 = [calculator.dtr(98),0,calculator.dtr(28),0]
def solve(m1, m2 ,g, l1, l2, y0):
    args = (m1,m2, g,l1,l2)
    y0 = y0

    t = np.linspace(0, 5, 10000)

    r = integrate.ode(f)
    r.set_integrator('lsoda')
    r.set_initial_value(y0, t[0])
    r.set_f_params(args)


    dt = t[1] - t[0]
    y = np.zeros((len(t), len(y0)))
    idx = 0
    while r.successful() and r.t < t[-1]:
        y[idx, :] = r.y
        r.integrate(r.t + dt)
        idx += 1
    return y

# This things calculate the trajectory of the pendulum
y = solve(m1, m2,g, l1, l2, y0)
theta_1, theta_2 = y[:, 0], y[:, 2]

x1 = l1*np.sin(theta_1)
y1 = -l1 * np.cos(theta_1)
x2 = x1 + l2 * np.sin(theta_2)
y2 = y1 - l2 * np.cos(theta_2)

fig = plt.figure()
ax = fig.add_subplot(111,projection ='3d')

#This is where you store your data

ax.plot(x2,y2,np.linspace(0, 5, 10000), c='r', marker = 'o')
ax.set_xlabel("X axis Of Pendulum")
ax.set_ylabel("Y axis name")
ax.set_zlabel("Time")
plt.plot(x2,y2)
plt.show()


'''
fig, ax = plt.subplots()
ax.set_xlim(-2, 2) # This sets the x axis limit
ax.set_ylim(-2, 0.5) # This sets the y axis limit
line, = ax.plot(x2[0], y2[0])



anx = []
any = []
def animation(i):
    anx.append(x2[i])
    any.append(y2[i])

    line.set_xdata(anx)
    line.set_ydata(any)
    return line,

a = []
for x in range(len(x1)):
    a.append(x)

ax.grid()
animation = FuncAnimation(fig, animation, frames=a, interval=10)
plt.show()
'''
