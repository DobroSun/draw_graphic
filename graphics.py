#!env/bin/python3

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

from func import f


x = np.arange(-50, 50)
y = np.array(list(map(f.double, x)))



x_smooth = np.linspace(x.min(), x.max(), 1000)


spl = make_interp_spline(x, y, k=3)
y_smooth = spl(x_smooth)



plt.plot(x_smooth, y_smooth)
plt.show()
