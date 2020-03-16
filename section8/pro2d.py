import numpy as np
import matplotlib.pyplot as mp
from mpl_toolkits.mplot3d import Axes3D

pi= 3.1415926
x0, v0, a0 = (1 * pi)/180 , 0.0, 0.0
t0, tf = 0.0, 500.0 # Initial time, Final time
N = 5000
h = (tf -t0)/N
omega = 2/3
beta = 1.21

def f(r,t):
    pos = r[0]
    vel = r[1]
    #acc = r[2]
    f_x = vel
    f_v = beta*np.cos(omega*t) - 0.5*vel - np.sin(pos)
    return np.array([f_x,f_v])

tp = np.arange(t0,tf,h)

xp, vp = [], []

r = np.array([x0,v0], float)

for t in tp:
    xp.append(r[0])
    vp.append(r[1])
    #ap.append(r[2])
    k1 = h*f(r,t)
    k2 = h*f(r+0.5*k1,t+0.5*h)
    k3 = h*f(r+0.5*k2,t+0.5*h)
    k4 = h*f(r+k3,t+h)
    r += (k1+2*k2+2*k3+k4)/6

mp.plot(tp,xp)
#mp.plot(tp,ap)
mp.show()

mp.title('Phase Portrait of the Oscillator')
mp.plot(xp,vp,label="x vs v")
#mp.plot(xp,ap,label="x vs a")
#mp.plot(vp,ap,label="v vs a")
mp.legend()
mp.show()


fig = mp.figure()
ax = fig.gca(projection="3d")
ax.plot(tp,xp,vp)
ax.set_xlabel('t')
ax.set_ylabel(r'$\theta(t)$')
ax.set_zlabel(r'$\omega(t)$')
mp.show()

