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

f = Functions()
