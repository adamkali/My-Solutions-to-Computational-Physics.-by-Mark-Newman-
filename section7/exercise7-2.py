import numpy as np
import matplotlib.pyplot as mp
from dft import dft

data= np.loadtxt("sunspots.txt", float)
time = data[:,0]
number_of_sunspots = data[:,1]

mp.plot(time,number_of_sunspots, label="Number of Sunspots")
mp.legend()
mp.show()

fourier = dft(number_of_sunspots)
fourier = abs(fourier*fourier)
mp.plot(list(map(abs,fourier)))
mp.show()
