import numpy as np
from numpy.fft import rfft
import matplotlib.pyplot as mp
from dft import dft

piano = np.loadtxt("piano.txt", float)
mp.title('Piano Sound Wave')
mp.plot(list(map(abs,piano)), '.')
mp.show()
p_fourier = rfft(piano)
mp.title('Fourier Transform of a Piano Signal')
mp.plot(abs(p_fourier[:10001]))
mp.show()

trumpet = np.loadtxt("trumpet.txt", float)
mp.title('Trumpet Sound Wave')
mp.plot(list(map(abs,trumpet)), '.')
mp.show()
t_fourier = rfft(trumpet)
mp.title('Fourier Transform of a Trumpet Signal')
mp.plot(abs(t_fourier[:10001]))
mp.show()

