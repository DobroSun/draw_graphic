#!env/bin/python3

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

from func import f


x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y = np.array([1.21, 1.20, 1.18, 1.17, 1.16, 1.14, 1.13, 1.11, 1.10, 1.09])
z = np.array([1.70, 1.55, 1.44, 1.29, 1.26, 1.19, 1.13, 1.07, 1.02, 1.08])
#y = np.array(list(map(f.lim2, x)))

_, ax = plt.subplots()
ax.grid()

ax.set_xlabel('расстояние, см')
ax.set_ylabel('период, с')

x_smooth = np.linspace(x.min(), x.max(), 1000000)

spl = make_interp_spline(x, y, k=3)
y_smooth = spl(x_smooth)

plt.plot(x, y, label="T_прям")
plt.plot(x, z, label="Т_пер")
plt.legend(loc='upper right')
plt.show()
