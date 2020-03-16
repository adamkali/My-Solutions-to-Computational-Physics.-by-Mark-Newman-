import numpy as np
import matplotlib.pyplot as mp

r_min = 1
r_max = 4
r_delta = 0.01

iterations = 1000

initial_x = 0.5

x = initial_x
x_list= []

for i in np.arange(r_min, r_max, r_delta).tolist():
    y=[]
    for i in range(iterations):
        x = i * x * (1.0 - x)
        y.append(x)
    x_list.append(y)

mp.plot(x_list, "ko")
mp.show()
