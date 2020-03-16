import numpy as np
import matplotlib.pyplot as mp
from gaussxw import gaussxwab

def f(z):
    return (z**3 / (1 - z)**5) * 1/(np.exp(z/(1-z)) -1 )

N = 20
x, w = gaussxwab(N, 0,1)
__sum__ = 0.0
for i in range(N):
    __sum__ += w[i] * f(x[i])

k_b = 1.38e-23
pi = 3.14159
c= 3e8
h_bar = 1.054e-34

sigma = (k_b**4 * __sum__ ) / (4 * pi**2 * c**2 * h_bar**3 )

print(sigma)
