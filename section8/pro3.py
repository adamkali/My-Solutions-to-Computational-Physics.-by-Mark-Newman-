import numpy as np
import matplotlib.pyplot as mp

x0, v0, a0 = 1.0 , 0.0, 0.0
t0, tf = 0.0, 200.0 # Initial time, Final time
N = 5000
h = (tf -t0)/N
omega = 2/3
beta = 0.5
alpha=1.2

def f(r,t):
    pos = r[0]
    vel = r[1]
    f_x = vel
    f_a = alpha*np.cos(omega*t) - 0.5*beta*(1 - np.cos(2*pos))*vel + np.sin(pos)
    return np.array([f_x,f_a])

tp = np.arange(t0,tf,h)

xp, vp = [], []

r = np.array([x0,v0], float)

for t in tp:
    xp.append(r[0])
    vp.append(r[1])
    k1 = h*f(r,t)
    k2 = h*f(r+0.5*k1,t+0.5*h)
    k3 = h*f(r+0.5*k2,t+0.5*h)
    k4 = h*f(r+k3,t+h)
    r += (k1+2*k2+2*k3+k4)/6

mp.plot(tp,xp)
mp.plot(tp,vp)
mp.show()

mp.title('Phase Portrait of the Oscillator')
mp.plot(xp,vp,label="x vs v")
mp.legend()
mp.show()


