import numpy as np
import matplotlib.pyplot as mp
from vpython import cylinder, vector, sphere, rate
from scipy import array, arange, pi, sin, cos

pi = 3.14159

g = 9.81 # m/s^2
l = 0.4 # length of the bar in meters
th10, th20, om10, om20 = (90 * pi)/180,(0 * pi)/180,0.0, 0.0  # initial angle in radians, initial angular velocity
t0, tf = 0.0, 100.0 # Initial time, Final time
N = 50000
h = (tf -t0)/N

#Function defined in the textbook as the second order differential equation
def f(r,t):
    theta1 = r[0]
    omega1 = r[1]
    theta2 = r[2]
    omega2 = r[3]
    f_omega1 = - (omega1 ** 2 * sin(2 * theta1 - 2 * theta2) + 2 * omega2 ** 2 * sin(theta1 - theta2) + \
                  g / l * (sin(theta1 - 2 * theta2) + 3 * sin(theta1))) / (3 - cos(2 * theta1 - 2 * theta2))
    f_omega2 = (4 * omega1 ** 2 * sin(theta1 - theta2) + omega2 ** 2 * sin(2 * theta1 - 2 * theta2) + \
                 2 * g / l * (sin(2 * theta1 - theta2) - sin(theta2))) / (3 - cos(2 * theta1 - 2 * theta2))
    return array([ omega1, f_omega1, omega2, f_omega2], float)

# initialize time array resposible for evolution
tp = np.arange(t0,tf,h)

# initialize parameters for the angle of the pendulum and the angular velocity
th1p, om1p, th2p, om2p = [], [], [], []

#initialize the position array:
r = np.array([th10,om10,th20,om20], float)

# RK4 algorithm
for t in tp:
    th1p.append(r[0])
    om1p.append(r[1])
    th2p.append(r[2])
    om2p.append(r[3])
    k1 = h*f(r,t)
    k2 = h*f(r+0.5*k1,t+0.5*h)
    k3 = h*f(r+0.5*k2,t+0.5*h)
    k4 = h*f(r+k3,t+h)
    r += (k1+2*k2+2*k3+k4)/6


mp.plot(tp,th2p)
mp.show()

import numpy.fft as ft
ang = ft.rfft(th2p)
mp.plot(abs(ang[int(len(ang)/100):]))
mp.show()

mp.title('Phasee Portrait of a Pendulum')
mp.plot(th1p,om1p,label="Bob1")
mp.plot(th2p,om2p,label="Bob2")
mp.xlabel(r'Angle $(Rads)$')
mp.ylabel(r'Angular Velocity $(\frac{Rads}{s})$')
mp.show()

rod1 = cylinder(pos=vector(0, 0, 0), axis=vector(l * np.cos(th10 - pi / 2), l * np.sin(th10 - pi / 2), 0), radius=l/40)
bob1 = sphere(pos=vector(l * np.cos(th10 - pi / 2), l * np.sin(th10 - pi / 2), 0), radius=l/10)
rod2 = cylinder(pos=vector(l * np.cos(th10 - pi / 2), l * np.sin(th10 - pi / 2), 0), \
                axis=vector(l * np.cos(th20 - pi / 2), l * np.sin(th20 - pi / 2), 0), radius=l/40)
bob2 = sphere(pos=vector(l * np.cos(th20 - pi / 2), l * np.sin(th20 - pi / 2), 0), radius=l/10)

for i in range(N):
    rate(N // 100)
    vector1 = vector(l * np.cos(th1p[i] - pi / 2), l * np.sin(th1p[i] - pi / 2), 0)
    vector2 = vector(l * np.cos(th2p[i] - pi / 2), l * np.sin(th2p[i] - pi / 2), 0)
    rod1.axis = vector1
    bob1.pos = vector1
    rod2.pos = vector1
    rod2.axis = vector2
    bob2.pos = vector1 + vector2
