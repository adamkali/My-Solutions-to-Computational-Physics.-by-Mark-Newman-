import numpy as np
import matplotlib.pyplot as mp

pi = 3.14159
rad = 0.08 # Radius of the ball
den = 1.22 # Density of the air
coe = 0.47 # Coefficient of drag
vin = 100  # Initial velocity
ang = pi/6 # Angle of inclination
gra = 9.81 # Gravitational field

drag_coefficient = 0.5*pi* rad**2 *den*coe

# Calculate the drag coefficient

px0, py0 = 0.0 , 0.0 # Initial Posititions
vx0, vy0 = vin*np.cos(ang), vin*np.sin(ang) # Initial Velocities

def drag(m):
    return drag_coefficient/m

def f(r,t,m):
    x1 = r[0]
    v1 = r[1]
    x2 = r[2]
    v2 = r[3]
    velocity = np.sqrt(v1**2 + v2**2)
    f_v1 = -drag(m)*v1*velocity
    f_v2 = -gra - drag(m)*v2*velocity
    return np.array([v1,f_v1,v2,f_v2], float)


a,b = 0.00, 20.00
h =(b-a)/10000
time=np.arange(a,b,h)
def rk4(m):
    x_po, y_po = [], []
    r = np.array([px0,vx0,py0,vx0], float)
    for t in time:
        x_po.append(r[0])
        y_po.append(r[2])
        k1 = h*f(r,t,m)
        k2 = h*f(r+0.5*k1,t+0.5*h,m)
        k3 = h*f(r+0.5*k2,t+0.5*h,m)
        k4 = h*f(r+k3,t+h,m)
        r += (k1+2*k2+2*k3+k4)/6
    return x_po, y_po

x_1, y_1 = rk4(1)
x_2, y_2 = rk4(2)
x_3, y_3 = rk4(4)
mp.plot(x_1,y_1, label="mass = 1")
mp.plot(x_2,y_2, label="mass = 2")
mp.plot(x_3,y_3, label="mass = 4")
mp.axhline(y=0)
mp.legend()
mp.show()



