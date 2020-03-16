import numpy as np
import matplotlib.pyplot as mp

#constants
M = 200 # Number of grid squares
V = 1.0 # top wall
target = 1e-6
omega = 0.9

#Create arrays to hold potentilal values
phi = np.zeros([M+1,M+1], float)

#phi_prime = np.empty([M+1,M+1], float)

# Main Loop
delta = 1.0
while delta>target:

    delta = 0.0
    # Calculate the new Values of the potential
    for i in range(1,M):
        for j in range(1,M):

            if i>20 and i<80 and j==20:
                phi[i,j] = 10
            elif i>20 and i<80 and j==80:
                phi[i,j] = -10
            else:
                diff = (phi[i+1,j] + phi[i-1,j] \
                        + phi[i,j+1] + phi[i,j-1])/4 \
                        - phi[i,j]
                phi[i,j] = phi[i,j] + (1+omega)*diff

            #Update the delta until it hits the target
            if diff>delta: delta = diff

color = mp.imshow(phi)
color.set_cmap("Blues_r")
mp.colorbar()
mp.show()

