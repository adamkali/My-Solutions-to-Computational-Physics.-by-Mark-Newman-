import numpy as np
import matplotlib.pyplot as mp

# initialize parameters
a = 1.0
b = 0.5
c = 0.5
d = 0.5
N=20000
t0,tf=0,30
h=(tf-t0)/N

# initialize populations
x_init = 2.0 #thousand
y_init = 2.0 #thousand


# Define population evolution
def f_x(x,y):
    return a*x - b*x*y
def f_y(x,y):
    return c*x*y - d*y

#Define population array function
def f(r):
    x = r[0]
    y = r[1]
    return np.array([ f_x(x,y), f_y(x,y) ], float)

#initialize the population array
r = np.array([x_init,y_init], float)

#rk4
time = np.arange(t0,tf,h)
xp, yp = [], []
for t in time:
    xp.append(r[0])
    yp.append(r[1])
    k1 = h*f(r)
    k2 = h*f(r+0.5*k1)
    k3 = h*f(r+0.5*k2)
    k4 = h*f(r+k3)
    r += (k1+2*k2+2*k3+k4)/6

mp.plot(time,xp, label='Rabbits')
mp.plot(time,yp, label='Foxes')
mp.legend()
mp.show()


