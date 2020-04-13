#Complex Sinus function  with coloring based to imaginary part
# Based on this comment http://stackoverflow.com/a/6543777
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.gca(projection='3d')
X = np.arange(-2*3.14, 2*3.14, 0.1)
Y = np.arange(-2, 2, 0.1)
X, Y = np.meshgrid(X, Y)
R=np.sin(X + 1j*Y)
Z=R.real
T=R.imag
N = np.abs(T/T.max())  # normalize 0..1
plt.title(' $\mathrm{f(z)=sin(z)}$')
plt.xlabel(' $\mathrm{Re(z)}$')
plt.ylabel(' $\mathrm{Im(z)}$')
surf = ax.plot_surface(
    X, Y, Z, rstride=1, cstride=1,
    facecolors=cm.jet(N),
    linewidth=0, antialiased=True, shade=False)
# Colorbar see http://stackoverflow.com/a/6601210
m = cm.ScalarMappable(cmap=cm.jet, norm=surf.norm)
m.set_array(T)
p=plt.colorbar(m)
p.set_label(' $\mathrm{Im(f(z))}$')

fig.set_size_inches(14,7) #http://stackoverflow.com/questions/332289/how-do-you-change-the-size-of-figures-drawn-with-matplotlib
plt.show() # if you run it as a python script
