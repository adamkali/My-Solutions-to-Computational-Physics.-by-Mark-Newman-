import numpy as np
import matplotlib.pyplot as mp

#constants
M = 100 # Number of grid squares
V = 1.0 # top wall
target = 1e-6

#Create arrays to hold potentilal values
phi = np.zeros([M+1,M+1], float)
phi[0,:] = V
phi_prime = np.empty([M+1,M+1], float)

# Main Loop
delta = 1.0
while delta>target:

    # Calculate the new Values of the potential
    for i in range(M+1):
        for j in range(M+1):
            if i==0 or i==M or j==0 or j==M:
                phi_prime[i,j] = phi[i,j]
            else:
                phi_prime[i,j] = (phi[i+1,j] + phi[i-1,j] \
                                    + phi[i,j+1] + phi[i,j-1])/4

        # calculate the maximum value between the old values
        delta = np.max(abs(phi - phi_prime))

        # swap the phis to get to accuracy
        phi,phi_prime = phi_prime, phi

color = mp.imshow(phi)
color.set_cmap("Blues_r")
mp.colorbar()
mp.show()

