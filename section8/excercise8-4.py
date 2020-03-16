import numpy as np
import matplotlib.pyplot as mp
from vpython import cylinder, vector, sphere, rate

pi = 3.14159

g = 9.81 # m/s^2
l = 0.1 # length of the bar in meters
th0, om0 = (90 * pi)/180, 0.0  # initial angle in radians, initial angular velocity
t0, tf = 0.0, 20.0 # Initial time, Final time
N = 5000
h = (tf -t0)/N

# Driving coefficients O=driving frequency C= Driving amplitude
C, O=100.0, g/l

#Function defined in the textbook as the second order differential equation
def f(r,t):
    theta = r[0]
    omega = r[1]
    f_th = omega
    f_om = - (g/l) * np.sin(theta) -0.05*(omega + theta*t)/l
    return np.array ([f_th,f_om], float)

# initialize variables --------------------------------------------------

# initialize time array resposible for evolution
tp = np.arange(t0,tf,h)

# initialize parameters for the angle of the pendulum and the angular velocity
thp, omp = [], []

#initialize the position array:
r = np.array([th0,om0], float)
# RK4 algorithm
for t in tp:
    thp.append(r[0])
    omp.append(r[1])
    k1 = h*f(r,t)
    k2 = h*f(r+0.5*k1,t+0.5*h)
    k3 = h*f(r+0.5*k2,t+0.5*h)
    k4 = h*f(r+k3,t+h)
    r += (k1+2*k2+2*k3+k4)/6

mp.title('Phasee Portrait of a Pendulum')
mp.plot(thp,omp)
mp.xlabel(r'Angle $(Rads)$')
mp.ylabel(r'Angular Velocity $(\frac{Rads}{s})$')
mp.show()

# make animation
rod = cylinder(pos=vector(0, 0, 0), axis=vector(l * np.cos(th0 - pi / 2), l * np.sin(th0 - pi / 2), 0), radius=l/40)
bob = sphere(pos=vector(l * np.cos(th0 - pi / 2), l * np.sin(th0 - pi / 2), 0), radius=l/10)
for theta in thp:
    rate(N // 10)
    rod.axis = vector(l * np.cos(theta - pi / 2), l * np.sin(theta - pi / 2), 0)
    bob.pos = vector(l * np.cos(theta - pi / 2), l * np.sin(theta - pi / 2), 0)
