import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
from mpl_toolkits.mplot3d import Axes3D
import scipy

# This is defining some constant
sigma = 8
rho = 28
beta = 1.6

# This define the lorenz equations
def lorenz_equation(xyz, t,rho, sigma, beta):
    x,y,z = xyz
    return [sigma*( y-x), x*(rho -z), x*y - beta*z]

xyz0 = [1.0,1.0,1.0]
t = np.linspace(0,100,10000)# This gives something to feed it into the odeint function. second one tells the end vaule
sol = integrate.odeint(lorenz_equation, xyz0, t, args=(rho, sigma, beta))# This is solving the differential equation

# This would plot the function
fig = plt.figure()
ax = fig.add_subplot(111,projection ='3d')

ax.plot(sol[:,0],sol[:,1],sol[:,2], c='b', alpha = 0.9)
ax.set_xlabel("Your X axis name")
ax.set_ylabel("Your y axis name")
ax.set_zlabel("Your Z Axis name")
plt.show()

