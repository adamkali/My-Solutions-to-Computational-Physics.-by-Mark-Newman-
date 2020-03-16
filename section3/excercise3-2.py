import numpy as np
import matplotlib.pyplot as mp

# Part a  ------------------------------
tau = 2 * 3.1415926535897932384626
theta_a = np.linspace(0,tau,1000)
def x_a(theta):
    return 5 * np.cos(theta) + np.cos(theta * 5)
def y_a(theta):
    return 5 * np.sin(theta) - np.sin(theta * 5)

x_1,y_1 = [],[]

for i in range(len(theta_a)):
    x_1.append(x_a(theta_a[i]))
    y_1.append(y_a(theta_a[i]))
    i += 1

mp.plot(x_1,y_1)
mp.show()

# Part b  ----------------------------------------
end = tau * 5
theta_b = np.linspace(0,end,1000)

r, x_2, y_2 = [], [], []

for i in range(len(theta_b)):
    r.append(theta_b[i]*theta_b[i])
    x_2.append(r[i]*np.cos(theta_b[i]))
    y_2.append(r[i]*np.sin(theta_b[i]))
    i += 1

mp.plot(x_2,y_2)
mp.show()

# Part c -----------------------------------------
end = tau * 12
theta_c = np.linspace(0,end,1000)

def radius(a):
    return np.exp(np.cos(a)) - 2*np.cos(4*a) + (np.sin(a/12))**5

r, x_3, y_3 = [], [], []

for i in range(len(theta_c)):
    r.append(radius(theta_c[i]))
    x_3.append(r[i]*np.cos(theta_c[i]))
    y_3.append(r[i]*np.sin(theta_c[i]))
    i += 1


mp.plot(x_3,y_3)
mp.show()


