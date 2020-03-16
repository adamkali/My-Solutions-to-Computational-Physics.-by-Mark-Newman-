import numpy as np
import matplotlib.pyplot as mp
from scipy import floor

V_out = 0.0 # Initial condition
t_ini = 0.0 # initial time
t_fin = 10.0 # final time
N = 5000
h = (t_fin - t_ini)/N

def V_in(time):
    if np.floor(2*time) % 2 == 0:
        return 1
    else:
        return -1

def f(V, t, RC):
    return (1/RC) * (V_in(t) - V)

def g(RC):
    time = np.arange(t_ini , t_fin,h)
    Pot = []
    V = V_out
    for t in time:
        Pot.append(V)
        k1 = h*f(V,t,RC)
        k2 = h*f(V+0.5*k1,t+0.5*h,RC)
        k3 = h*f(V+0.5*k2,t+0.5*h,RC)
        k4 = h*f(V+k3,t+h,RC)
        V += (k1+2*k2+2*k3+k4)/6
    return Pot

time = np.arange(t_ini , t_fin,h)
mp.plot(time, g(0.01), label='RC = 0.01')
mp.plot(time, g(0.1), label='RC = 0.1')
mp.plot(time, g(10.0), label='RC = 10.0')
mp.legend()
mp.show()

