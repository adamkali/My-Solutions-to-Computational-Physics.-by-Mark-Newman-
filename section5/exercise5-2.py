"""
This is a program using Simpsons rule to integrate
the function x^4 - 2x+1
"""

def function(x):
    return  (x**4) - (2*x) + 1

N = 10000
a = 0.0
b = 2.0
def simpsons(f, a,b,N):
    h = (b-a)/N
    __sum__ = 0
    __sum__ = f(a) + f(b)
    for m in range(1,int( N/2)):
        __sum__ += 4*f( a + ((2*m) -1)*h)
    for n in range(1,int(N/2 -1)):
        __sum__ += 2 * f(a + 2*n*h)
    __sum__ = __sum__ * (1/3) * h
    return __sum__

print(simpsons(function,a,b,N))


