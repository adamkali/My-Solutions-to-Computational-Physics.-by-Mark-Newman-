import numpy as np
from numpy.fft import rfft, irfft
import matplotlib.pyplot as mp
from dft import dft

dow = np.loadtxt("dow.txt")
mp.title("Dow Jones Industrial Average")
mp.plot(dow)
mp.show()

dow_for = rfft(dow)
mp.title("Dow Jones Fourier Transform")
mp.plot(abs(dow_for))
mp.show()

N = len(dow_for)
first_10_percent = np.zeros(N,float)
first_10_percent[0 : int(N / 10)] = np.copy(dow_for[0 : int(N / 10)])
dow_first_10_p = irfft(first_10_percent)

mp.title("Dow Jones Filtering")
mp.plot(dow_first_10_p)
mp.show()

first_2_percent = np.zeros(N,float)
first_2_percent[0 : int(N/50)] = np.copy(dow_for[0 : int(N/50)])
dow_first_2_p = irfft(first_2_percent)

mp.title("Dow Jones Industial Average")
mp.plot(dow, label='Unfiltered')
mp.plot(dow_first_10_p, label='Filtering 10%')
mp.plot(dow_first_2_p, label='Filtering 2%')
mp.legend()
mp.show()



