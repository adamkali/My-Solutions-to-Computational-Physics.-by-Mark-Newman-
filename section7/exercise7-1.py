import numpy as np
import matplotlib.pyplot as mp
from dft import dft

pi = 3.14159
N = 1000
x = np.linspace(1,N,501)

square = np.zeros(N,complex)
for i in range(1, N//2):
    square[i] = 1.0
mp.plot(list(map(abs,dft(square))))
mp.show()

sawtooth = np.empty(N,complex)
for i in range(N):
    sawtooth[i] = i
mp.plot(list(map(abs,dft(sawtooth))))
mp.show()

mod_sine = np.empty(N,complex)
for n in range(N):
    mod_sine[n] = np.sin( pi * n / N ) * np.sin(20*pi*n/N)
mp.plot(list(map(abs,dft(mod_sine))))
mp.show()

