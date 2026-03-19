import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d


## Single Points
plt.style.use('dark_background') ## I put this in because I prefer darkmode
'''
other styles = default, classic, Solarize_Light2, bmh, fast, fivethirtyeight, ggplot, greyscale, petroff10,... etc...

'''
ax = plt.axes(projection="3d")
x_data = np.random.randint(0, 100, (500, ))
y_data = np.random.randint(0, 100, (500, ))
z_data = np.random.randint(0, 100, (500, ))

ax.scatter(x_data, y_data, z_data)

plt.show()

