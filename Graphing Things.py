import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 10000)
y1 = x**2 + 3*x + 10

plt.plot(x, y1, color = 'blue', label = 'y(x)')
plt.show()

