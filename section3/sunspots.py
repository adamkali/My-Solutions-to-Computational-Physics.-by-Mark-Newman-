# Adam Kalinowski

import numpy as np
import matplotlib.pyplot as mp

"""
Here we read in the data sunspots.txt
we then assign the values
"""
data= np.loadtxt("sunspots.txt", float)
time = data[:1000,0]
number_of_sunspots = data[:1000,1]

def running_avg(array):
    return_array = []
    return_array.append(array[0])
    return_array.append(array[1])
    return_array.append(array[2])
    return_array.append(array[3])
    return_array.append(array[4])
    stop = len(array) - 5
    for i in range(5,stop):
        __sum__ = 0
        for j in range(i-5, i+5):
            __sum__ = __sum__ + array[j]
        __sum__ = (1/11) * __sum__
        return_array.append(__sum__)
    return return_array

running_average = running_avg(number_of_sunspots)
time_average = np.linspace(0,len(running_average), len(running_average))

mp.plot(time,number_of_sunspots, label="Number of Sunspots")
mp.plot(time_average, running_average, label="Running Average of Sunspots")
mp.legend()
mp.show()
