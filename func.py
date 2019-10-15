#!env/bin/python3

import numpy as np

class Functions():
    def cos(self, x):
        return np.cos(x)

    def sin(self, x):
        return np.sin(x)

    def double(self, x):
        return x * x

    def sqrt(self, x):
        assert x >= 0, "Ожидалось положительно число"
        return np.sqrt(x)

    def lim1(self, x):
        return np.sin(x) / float(x)

    def lim2(self, x):
        return np.power(1 + 1/float(x), x)

f = Functions()
