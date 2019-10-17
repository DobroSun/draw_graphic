#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

from func import f

x = np.array([0.46, 0.36, 0.37, 0.36, 0.41, 0.42, 0.43, 0.44, 0.45, 0.45])
y = np.array([1.79, 1.41, 1.45, 1.51, 1.62, 1.65, 1.70, 1.78, 1.79, 1.79])
#z = np.array([1.70, 1.55, 1.44, 1.29, 1.26, 1.19, 1.13, 1.07, 1.02, 1.08])

x.sort()
y.sort()

_, ax = plt.subplots()
ax.grid()

ax.set_xlabel('длина(L), м')
ax.set_ylabel('период(T^2), с^2')

"""
x_smooth = np.linspace(x.min(), x.max(), 1000000)

spl = make_interp_spline(x, y, k=3)
y_smooth = spl(x_smooth)
"""
print(x)
print(y)
plt.plot(x, y, "ro")
plt.plot([0.36, 0.46], [1.41, 1.79])
#plt.legend(loc='upper right')
plt.show()
