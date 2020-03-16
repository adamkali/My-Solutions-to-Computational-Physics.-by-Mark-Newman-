import numpy as np
import matplotlib.pyplot as mp

M = 1.989e30  # kg
G = 66374.2  # in m^3/ kg*yr^2
m = 5.0722e24

px0,py0 = 1.471e11, 0
vx0,vy0 = 0, 3.0287e4 * 8760 * 60 * 60
t0,tf,h = 0.0, 10.0, 1 / (8760*3)

gamma1 = G*M
gamma2 = gamma1*0.5

def f(r,gamma):
    x1,x2 = r[0],r[2]
    v1,v2 = r[1],r[3]
    R = np.sqrt(x1**2 + x2**2)
    a1 = -gamma * x1 / (R**3)
    a2 = -gamma * x2 / (R**3)
    return np.array([v1,a1,v2,a2], float)

tp,xp,yp,up,kp = np.arange(t0,tf,h),[],[],[],[]
r = np.array([px0,vx0,py0,vy0], float)

def vverlet(r,gamma,h):
    f_half_step = 0.5 * h * f(r,gamma)
    vx_half_step = r[1] + f_half_step[1]
    vy_half_step = r[3] + f_half_step[3]
    r[0] += h*vx_half_step
    r[2] += h*vy_half_step
    Return = np.array([r[0],vx_half_step,r[2],vy_half_step],float)
    k = h*f(Return,gamma)
    Return[1] += k[1]
    Return[3] += k[3]
    return Return

def potential(r):
    R = np.sqrt(r[0]**2 + r[2]**2)
    return -6.674e-11*M*m/R

def kinetic(r):
    V_square = r[1]**2 + r[3]**2
    return 0.5*m*V_square / (8760 * 60 * 60)**2


for t in tp:
    xp.append(r[0])
    yp.append(r[2])
    up.append(potential(r))
    kp.append(kinetic(r))
    if t < 5.0:
        r = vverlet(r,gamma1,h)
    else:
        r =vverlet(r,gamma2,h)

mp.title("Earth's Trajectory")
mp.plot(xp,yp,label='Earth')
mp.xlabel('x (m)')
mp.ylabel('y (m)')
mp.legend()
mp.show()

mp.title("Energy vs Time")
mp.plot(tp, up, label="Potential Energy")
mp.plot(tp, kp, label="Kinetic Energy")
mp.xlabel("Time (t)")
mp.ylabel("Energy (J)")
mp.legend()
mp.show()
