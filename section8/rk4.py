import numpy as np
import matplotlib.pyplot as mp

def f(x,t):
    return -x**3 + np.sin(t)

def g(x,t):
    one = np.sin(t*x)
    two = np.cos(t*x)
    return one + two

a = 0.0
b = 10.0
c = 100.0
d = -100.0
N = 100
N2 = 1000

h1 = (b-a)/N
h2 = (c-d)/N2

t1 = np.arange(a,b,h1)
t2 = np.arange(d,c,h2)
x1p, x2p = [], []
x1, x2 = 0.0,0.0

for t in t1:
    x1p.append(x1)
    k11 = h1*f(x1,t)
    k12 = h1*f(x1+0.5*k11,t+0.5*h1)
    k13 = h1*f(x1+0.5*k12,t+0.5*h1)
    k14 = h1*f(x1+k13,t+h1)
    x1 += (k11+2*k12+2*k13+k14)/6
for t in t2:
    x2p.append(x2)
    k21 = h2*g(x2,t)
    k22 = h2*g(x2+0.5*k21,t+0.5*h2)
    k23 = h2*g(x2+0.5*k22,t+0.5*h2)
    k24 = h2*g(x2+k23,t+h2)
    x2 += (k21+2*k22+2*k23+k24)/6

mp.plot(t1,x1p)
mp.show()

mp.plot(t2,x2p)
mp.show()



