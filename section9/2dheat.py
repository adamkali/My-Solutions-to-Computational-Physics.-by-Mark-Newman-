import numpy as np
import matplotlib.pyplot as mp
from mpl_toolkits.mplot3d import axes3d
from matplotlib import cm

mp.ion()
fig = mp.figure()
ax = fig.gca(projection='3d')

# Define constants
A = 10        # Thickness of the barrier
D = 4.25e-6     # Thermal Diffusivity
N = 100         # Numbert of Divisions in Grid
a = A/N         # Grid Spacing
k = 10.67
h =  ((1/N)**2)       # Time-step
epsilon = h/100

t1, t2, t3, t4, t5 = 0.01, 0.1, 0.4, 1.0, 5.0
tend = t5+ epsilon

x = np.linspace(0,N+1,101)
y = np.linspace(0,N+1,101)
X,Y = np.meshgrid(x,y)

T = 50*np.ones([N+1,N+1], float)
T[35:45,35:45] = 100
T[55:65,55:65] = 100
Tp = np.copy(T)

t = 0.0
c = h*k/(a*a)

"""
mp.show()
mp.pause(0.01)
"""
while t < tend:

    ax.clear()

    Tp[1:N, 1:N] = T[1:N,1:N] + c*(T[2:N+1,1:N]\
                + T[0:N-1,1:N] + T[1:N,2:N+1] \
                + T[1:N,0:N-1] - 4*T[1:N,1:N])
    T,Tp = Tp, T
    t += h


    surf = ax.plot_surface(X,Y,T, cmap=cm.magma,
                           linewidth=0, antialiased = False)
#    color = mp.imshow(T)
#    color.set_cmap("magma")
    mp.show()
    mp.pause(0.001)

