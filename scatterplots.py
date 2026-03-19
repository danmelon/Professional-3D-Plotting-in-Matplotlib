import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d



plt.style.use('dark_background') ## I put this in because I prefer darkmode
'''
other styles = default, classic, Solarize_Light2, bmh, fast, fivethirtyeight, ggplot, greyscale, petroff10,... etc...

'''
ax = plt.axes(projection="3d")
x_data = np.random.randint(0, 100, (500, ))
y_data = np.random.randint(0, 100, (500, ))
z_data = np.random.randint(0, 100, (500, ))

ax.scatter(x_data, y_data, z_data, color ='hotpink')

plt.show()

trig = plt.axes(projection="3d")
x = np.arange(0, 50, 0.1)
y = np.arange(0, 50, 0.1)
z = np.sin(x) * np.cos(y)

trig.scatter(x, y, z, color="hotpink")
trig.set_title("function scatter")
trig.set_xlabel("x values")
trig.set_ylabel("y values")
trig.set_zlabel("z values")


plt.show()