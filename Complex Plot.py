import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D
import cmath

inputs = []
x1 = []  # Real Value input
y1 = []  # Real Value Output
add = np.linspace(-10,10, 10)

# This would make complex an list of complex numbers
for x in add:
    for i in add:
        inputs.append(complex(x,i))

for x in inputs:
    x1.append(x.real)
    y1.append(x.imag *1j)

x_array = np.array(x1)
y_array = np.array(y1)
X1,Y1 = np.meshgrid(x_array,y_array)# This is a must

# The complex function
Z = np.sin(X1+Y1) # This is the input function

# This would be plotting the thing
fig, axes = plt.subplots(figsize=(5,5), subplot_kw={'projection':'3d'})# Defineing the subplots

norm = mpl.colors.Normalize(-abs(Z.imag).max(), abs(Z.imag).max())# This would setup the colour Normalize
p = axes.plot_surface(X1,Y1.imag,Z.real,antialiased=False, norm=norm, cmap=mpl.cm.Reds) #

axes.set_title("Complex Plot of X^2 + 1")
axes.set_xlabel("Real Value Input ")
axes.set_ylabel("Imagery Value Input")
axes.set_zlabel("Real Value Output ")

cb = fig.colorbar(p, ax=axes)
cb.set_label("Imagery Value Output")


plt.show()
'''
import time

a = time.time()
x = np.linspace(0,100, 1000)
y = np.sqrt(x)
z = np.sqrt(x)


X,Y = np.meshgrid(x,y) # Making an meshgrid
Z = np.sqrt(Y) # Making another 
b = time.time()

fig, ax = plt.subplots(figsize=(6,5))

norm = mpl.colors.Normalize(-abs(Z).max(), abs(Z).max())
p = ax.pcolor(X,Y,Z,norm=norm,cmap=mpl.cm.bwr)
ax.axis('tight')
ax.set_xlabel("X")
ax.set_ylabel("Y")
cb = fig.colorbar(p, ax=ax)
cb.set_label("Z")
plt.show()
'''