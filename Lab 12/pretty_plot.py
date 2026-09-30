# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Aidan
# Section:      519
# Assignment:   Lab 12 Individual 
# Date:        15 11 2025

import numpy as np
import matplotlib.pyplot as plt

v0 = np.array([0, 1]).reshape(2,1)
print(v0)
M = np.array([1.02, 0.095, -0.095, 1.02]).reshape(2,2)
print(M)

v1 = M @ v0
print(v1)

vectors = [v0]
for i in range(250): #Updates list of vectors with each new matrix product (sends to the back of list). It also uses the last item in the list to get the new product and append it
    vectors.append(M @ vectors[-1])
x = []
y = []
for i in vectors:
    x.append(i[0])
    y.append(i[1])
# Plot the points
plt.figure()
plt.plot(x, y, marker='o', markersize=2, linestyle='-')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Spiral Pattern')
plt.axis('equal')
plt.show()