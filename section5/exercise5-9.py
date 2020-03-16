"""
Callculating the heat capacity
of a solid using gaussian quadrature
"""

import numpy as np
import matplotlib.pyplot as mp
from gaussxw import gaussxwab

def f(x):
    numerator = (x**4) * (np.exp(x))
    denomenator = (np.exp(x) - 1)**2
    return numerator / denomenator

volume=1e-3 # cubic meters
density= 6.022e28 # 1/ cubic meters
debeye= 428 # kelvin
boltz=1.381e-23
cv_0= 9 * volume * density * boltz

temp = np.linspace(5,1000,100)
Cv = []


def cv(Temp):
    # do __sum__
    TEMP = Temp / debeye
    __sum__ = 0.0
    x,w = gaussxwab(50,0,1/TEMP)
    for k in range(50):
        __sum__ += w[k] * f(x[k])
    return __sum__ * cv_0 * (TEMP**3)

for m in range(len(temp)):
    Cv.append(cv(temp[m]))

mp.plot(temp,Cv)
mp.show()
