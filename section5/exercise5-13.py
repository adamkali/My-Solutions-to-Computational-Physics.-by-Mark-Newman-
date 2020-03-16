import numpy as np
import matplotlib.pyplot as mp
from math import factorial
from gaussxw import gaussxwab

def H(n,x):
    if n==0:
        return 1
    elif n==1:
        return 2*x
    else:
        return 2*x*H(n-1,x)-2*(n-1)*H(n-2,x)

sqpi = np.sqrt(3.14159265358)

def psi(n,x):
    first = 1 / np.sqrt( 2**n * factorial(n) * sqpi )
    second = np.exp(- x**2 / 2) * H(n,x)
    return first * second

x = np.linspace(-4,4,100)
p0, p1, p2, p3 = [], [], [], []

for i in range(len(x)):
    p0.append(psi(0,x[i]))
    p1.append(psi(1,x[i]))
    p2.append(psi(2,x[i]))
    p3.append(psi(3,x[i]))
    i += 1

mp.plot(x,p0, label=r"$\Psi_0$")
mp.plot(x,p1, label=r"$\Psi_1$")
mp.plot(x,p2, label=r"$\Psi_2$")
mp.plot(x,p3, label=r"$\Psi_3$")
mp.legend()
mp.show()

def integrand(z):
    def x(z):
        return z / (1 - z**2)

    def dx(z):
        num = 1 + z**2
        den = (1 - z**2)**2
        return num / den

    return x(z)**2 * np.abs(psi(5,x(z)))**2 * dx(z)

__sum__ = 0.0
x,w = gaussxwab(100, -1 , 1)
for i in range(len(x)):
    __sum__ += w[i] * integrand(x[i])
print(np.sqrt(__sum__))
