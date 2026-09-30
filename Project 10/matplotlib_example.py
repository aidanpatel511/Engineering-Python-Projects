# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: James Willard
# NAME Simon Soto
# NAME Aidan Patel
# NAME Kai Fuentes-Hamilton
# Section: 519
# Assignment: Lab 12 Activity 2 Team
# Date: 13 NOV 2025

import matplotlib.pyplot as plt
import numpy as np

# Plot parabolas
x = np.linspace(-2.0, 2.0, 100)
f1 = 2
f2 = 6
y1 = (1/(4*f1)) * x**2
y2 = (1/(4*f2)) * x**2
plt.figure()
plt.plot(x, y1, color='red', linewidth=2.0, label='f = 2')
plt.plot(x, y2, color='blue', linewidth=6.0, label='f = 6')
plt.title('Parabola plots for varying focal length')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

# Plot cubic polynomial
x = np.linspace(-4.0, 4.0, 25)
y = 2*x**3 + 3*x**2 - 11*x - 6
plt.figure()
plt.scatter(x, y, marker='*', color='yellow', edgecolors='black', s=100, label='y = 2x^3 + 3x^2 - 11x - 6') #changed to scatter plot to create black outlines for yellow points and increased size for visibility
plt.title('Plot of Cubic Polynomial')
plt.xlabel('x values')
plt.ylabel('y values')
plt.show()

# Plot sin(x) and cos(x) using two subplots
x = np.linspace(-2*np.pi, 2*np.pi, 101)
y_sin = np.sin(x)
y_cos = np.cos(x)

fig, (ax1, ax2) = plt.subplots(2, 1)

ax1.plot(x, y_cos, color='maroon', label='cos(x)')
ax1.set_title('Plot of cos(x) and sin(x)')
ax1.set_ylabel('y = cos(x)')
ax1.legend()
ax1.legend(loc = "lower right")
ax1.grid(True)
ax1.set_xticklabels([])  # Hide x-axis labels for the first subplot
ax2.plot(x, y_sin, color='grey', label='sin(x)')
ax2.set_xlabel('x')
ax2.set_ylabel('y = sin(x)')
ax2.legend()
ax2.grid(True)

plt.show()