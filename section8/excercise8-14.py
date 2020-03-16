import numpy as np
import matplotlib.pyplot as mp
# Program Constants
m = 9.1094e-31      # Mass of an electron
hbar = 1.0546e-34   # Planks Angular constant
e = 1.6022e-19      # Electron charge
L = 5.2918e-11      # Bohr Radius
N=1000
pi=3.14159
epsilon0 = 8.8541e-12
a=1e-11
V0= 50*e
li,lf=-10*a, 10*a
h= (lf-li)/N

well = np.arange(li,lf,h)

# Define the potential function here
def V(x):
    return V0*((x**4 / a**4) - (x**2 / a**2))

def f(r,x,E):
    psi = r[0]  # Solution to the Schrodinger Equation
    phi = r[1]  # First Derivative of Psi
    fpsi = phi
    fphi = (2*m/hbar**2)*(V(x) - E)*psi
    return np.array([fpsi,fphi], float)

# Calculate the wavefunction for a particular energy
def psi(E):
    psi = 0.0
    phi = 1.0
    r = np.array([psi,phi],float)
    wavefunction = []
    for x in well:
        wavefunction.append(r[0])
        k1 = h*f(r,x,E)
        k2 = h*f(r+0.5*k1,x+0.5*h,E)
        k3 = h*f(r+0.5*k2,x+0.5*h,E)
        k4 = h*f(r+k3,x+h,E)
        r += (k1+2*k2+2*k3+k4)/6

    return np.array(wavefunction, float)

# Main program to find the energy using the secant method


def secant_root(E1, E2):
    target_accuracy = e / 1000 #  eV
    wavefunction = psi(E1)
    psi2 = wavefunction[N - 1]
    while abs(E1 - E2) > target_accuracy:
        wavefunction = psi(E2)
        psi1, psi2 = psi2, wavefunction[N-1]
        E1, E2 = E2, E2 - psi2 * (E2 - E1) / (psi2 - psi1)

    # Normalize the wavefunction using Simpson's rule
    mod_squared = wavefunction * wavefunction
    integral = h / 3 *(mod_squared[0] + mod_squared[N//2 - 1] + \
            4 * sum(mod_squared[1 : N//2 : 2]) + 2 * sum(mod_squared[0 : N//2 + 1 : 2]) )

    return E2 / e, wavefunction / np.sqrt(2*integral)

# First three lowest energies of anharmonic oscillator
E0, psi0 = secant_root(0, 0.5*e)
E1, psi1 = secant_root(1.5*E0*e, 3*E0*e)
E2, psi2 = secant_root(3*E0*e, 9*E0*e)
print('E_0 = ', E0, 'eV')
print('E_1 = ', E1, 'eV')
print('E_2 = ', E2, 'eV')

xpoints = well
x_range = slice(N // 4 ,  3 * N // 4 , 1)
mp.plot(xpoints[x_range], psi0[x_range], 'k')
mp.plot(xpoints[x_range], psi1[x_range], 'b')
mp.plot(xpoints[x_range], psi2[x_range], 'g')
mp.xlabel('x (m)')
mp.ylabel('psi')
mp.show()
