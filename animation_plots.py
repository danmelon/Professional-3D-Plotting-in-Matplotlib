import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.animation import PillowWriter

fig = plt.figure()
l, = plt.plot([], [], 'k-')

plt.xlabel('xlabel')
plt.ylabel('ylabel')
plt.title('title')

plt.xlim(-5, 5)
plt.ylim(-5, 5)

def func(x):
    return np.sin(x)*3

## Animation
metadata = dict(title = 'Movie', artist = 'me')
writer = PillowWriter(fps=15, metadata = metadata)

## List of data which will get progressively longer
xlist = []
ylist = []

with writer.saving(fig, "sinWave.gif", 100):
    for xval in np.linspace(-5, 5, 100):
        xlist.append(xval)
        ylist.append(func(xval))

        l.set_data(xlist, ylist)

        writer.grab_frame()