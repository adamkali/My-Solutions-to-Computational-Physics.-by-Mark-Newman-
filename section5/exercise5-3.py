import numpy as np
import matplotlib.pyplot as mp

def simpsons(f, a,b):
    N = 10000
    h = (b-a)/N
    __sum__ = 0
    __sum__ = f(a) + f(b)
    for m in range(1,int( N/2)):
        __sum__ += 4*f( a + ((2*m) -1)*h)
    for n in range(1,int(N/2 -1)):
        __sum__ += 2 * f(a + 2*n*h)
    __sum__ = __sum__ * (1/3) * h
    return __sum__

def gaussian(t):
    return np.exp(- t ** t)

x = np.linspace(0,3,300)
y = []

for i in range(len(x)):
   y.append( simpsons(gaussian,0,x[i]) )
   i += 1

mp.plot(x,y)
mp.show()
