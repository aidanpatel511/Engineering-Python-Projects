# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: James Willard
# NAME Simon Soto
# NAME Aidan Patel
# NAME Kai Fuentes-Hamilton
# Section: 519
# Assignment: Lab 12 Activity 1 Team
# # Date: 13 NOV 2025

import numpy as np
A = np.arange(12).reshape(3, 4)
print("A =", A)
print()
B = np.arange(8).reshape(4, 2)
print("B =", B)
print()
C = np.arange(6).reshape(2, 3)
print("C =", C)
print()
D = A @ B @ C
print("D =", D)
print()
print("D^T =", D.T)
print()
E = (np.sqrt(D) / 2)
print("E =", E)