import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d


plt.style.use('dark_background') ## I put this in because I prefer darkmode

ax = plt.axes(projection="3d")

x_data = np.arange(0, 50, 0.1)
y_data = np.arange(0, 50, 0.1)

X, Y = np.meshgrid(x_data, y_data)

Z = X * Y

ax.plot_surface(X, Y, Z)
plt.show()

sine = plt.axes(projection="3d")

x = np.arange(-5, 5, 0.1)
y = np.arange(-5, 5, 0.1)

XX, YY = np.meshgrid(x, y)

ZZ = np.sin(XX) * np.cos(YY)

sine.plot_surface(XX, YY, ZZ, cmap = "vanimo")

# sine.view_init(azim=0, elev = 90) '''This shows default perspective as top down'''

plt.show()