# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Aidan
# Section:      519
# Assignment:   Lab 3 Individual 
# Date:         5 9 2025


import math
digits = int(input("Please enter the number of digits of precision for tau: "))
tau = 2*math.pi
print(f"The value of tau to {digits} digits is: {tau:.{digits}f}")