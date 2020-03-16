import numpy as np
import matplotlib.pyplot as mp
from gaussxw import gaussxwab




m = 1 # mass
N = 20 # number of points for gaussian quadrature
def T(a):
    def f(x):
        def v(y):
            return y**4
        return 1 / np.sqrt(v(a) - v(x))

    x, w = gaussxwab(N, 0, a)
    integral = 0.0
    for k in range(N):
        integral += w[k] * f(x[k])

    return np.sqrt(8)*integral

a = np.linspace(0,2,100)
Periods = []
for i in range(len(a)):
    Periods.append(T(a[i]))
    i += 1

mp.plot(a,Periods)
mp.show()

