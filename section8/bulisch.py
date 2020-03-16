import numpy as np
import matplotlib.pyplot as mp

g, l, pi = 9.81, 0.1 , 3.14159
th0 = (179.0 * pi)/180
a, b, N = 0.0, 10.0, 100
H = (b-a)/N
delta = 1e-8

def f(r,t):
    theta = r[0]
    omega = r[1]
    f_th = omega
    f_om = - (g/l) * np.sin(theta)
    return np.array ([f_th,f_om], float)

tp = np.arange(t0,tf,h)
thp, omp = [], []
r = np.array([th0,0.0], float)

for t in tp:

    thp.append(r[0])
    # Do one of the modified midpoint step size of H
    n = 1
    r1 = r + 0.5*H*f(r)
    r2 = r + H*f(r1)
    # These store the midpoints for the calculation.

""" The array R1 stoers the first row
    extrapolation table, which contains
    only the single modified midpoint
    estimate of the solution at the end
    of the interval. """
    R1 = np.empty([1,2], float)
    R1[0] = 0.5*(r1 + r2 + 0.5*H*f(r2))

    #now increase n until the desired accuracy is reached
    error = 2*H*delta
    while error>H*delta:

        n += 1
        h = H/n

        #MOdified midpoint method
        r1 = r + 0.5*h*f(r)
        r2 = r + h*f(r1)
        for i in range(n-1):
            r1 += h*f(r2)
            r2 += h*f(r1)


        # Calculate extrapolation estimates
        R2 = R1
        R1 = np.empty([n,2], float)
        R1[0] = 0.5*(r1+r2+0.5*f(r2))
        for m in range(1,n):
            epsilon = (R1[m-1] - R2[m-1]) / ((n/(n-1))**(2*m)-1)


