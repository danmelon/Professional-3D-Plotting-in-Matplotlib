import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d


## Single Points
plt.style.use('dark_background') ## I put this in because I prefer darkmode
'''
other styles = default, classic, Solarize_Light2, bmh, fast, fivethirtyeight, ggplot, greyscale, petroff10,... etc...

'''
ax = plt.axes(projection="3d")
ax.scatter(3, 5, 7)
plt.show()