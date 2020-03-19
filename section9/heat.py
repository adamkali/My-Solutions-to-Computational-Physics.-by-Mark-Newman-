from numpy import empty
from matplotlib.pyplot import plot, xlabel, ylabel, show

# Define constants
L = 0.01        # Thickness of the barrier
D = 4.25e-6     # Thermal Diffusivity
N = 100         # Numbert of Divisions in Grid
a = L/N         # Grid Spacing
h = 1e-4        # Time-step
epsilon = h/1000

Tl, Tm, Th = 0.0, 20.0, 50.0

t1, t2, t3, t4, t5 = 0.01, 0.1, 0.4, 1.0, 10.0
tend = t5+ epsilon

T = empty(N+1, float)
T[0], T[1:N], T[N] = 100, 30, 0.0
Tp = empty(N+1, float)
Tp[0], Tp[1:N], Tp[N] = 100, 30, 0.0

# Main Loop
t = 0.0
c = h*D/(a*a)
while t < tend:

    #calculate the values of T
    Tp[1:N] = T[1:N] + c*(T[2:N+1] + T[0:N-1] - 2*T[1:N])
    T,Tp = Tp,T
    t += h

    if abs(t-t1) < epsilon:
        plot(T)
    if abs(t-t2) < epsilon:
        plot(T)
    if abs(t-t3) < epsilon:
        plot(T)
    if abs(t-t4) < epsilon:
        plot(T)
    if abs(t-t5) < epsilon:
        plot(T)

xlabel("Position in the Steel Beam")
ylabel("Temprature in the Steel Beam")
show()
