import numpy as np
import matplotlib.pyplot as mp

# initialize parameters
s, r, b = 10.0, 8, 4.0/3
t0, tf = 0.0, 50.0
N=20000
h=(tf-t0)/N

# Initialize  positions of a particle
xi, yi, zi = 1.0, 0.0, 1.0

# Define the position functions
def f_x(x,y,z):
    return 1- y*z
def f_y(x,y,z):
    return (1+x) + s*z + y
def f_z(x,y,z):
    return b*y + (1 - x*z)

# Define position array function
def f(w):
    x = w[0]
    y = w[1]
    z = w[2]
    return np.array([ f_x(x,y,z), f_y(x,y,z), f_z(x,y,z)], float)

# Initialize the position array
w = np.array([ xi, yi, zi], float)

# Make the RK4
time = np.arange(t0,tf,h)
xp, yp, zp = [], [], []
for t in time:
    xp.append(w[0])
    yp.append(w[1])
    zp.append(w[2])
    k1 = h*f(w)
    k2 = h*f(w+0.5*k1)
    k3 = h*f(w+0.5*k2)
    k4 = h*f(w+k3)
    w += (k1+2*k2+2*k3+k4)/6

mp.plot(time, yp)
mp.show()

mp.plot(xp,zp)
mp.show()


