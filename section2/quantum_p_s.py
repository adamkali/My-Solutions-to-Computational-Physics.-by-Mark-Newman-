#Adam Kalinowski

from math import sqrt

h_bar = 1.0545718e-34 #the constant
mass = 9.11e-31 #mass of an electron
Total_Energy = 10 * 1.6022e-19 #Energy of the particle approaching the potential
Potential = 9* 1.6022e-19

k_1 = sqrt(2 * mass * Total_Energy) / h_bar
k_2 = sqrt(2 * mass * (Total_Energy - Potential)) / h_bar

Trans_prob = (4 * k_1 * k_2) / ( (k_1 + k_2) * (k_1 + k_2) )
Refle_prob = ((k_1 - k_2) / (k_1 + k_2)) \
        * ((k_1 - k_2) / (k_1 + k_2))

print(str(Trans_prob) + "%", str(Refle_prob) + "%")
