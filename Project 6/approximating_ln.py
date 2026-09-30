# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: James Willard
# NAME Simon Soto
# NAME Aidan Patel
# NAME Kai Fuentes-Hamilton
# Section: 519
# Assignment: Lab 6 Activity 3 Team
# Date: 28 SEP 2025

from math import * #importing math functions

x = float(input("Enter a value for x: "))

#Checks to see if x is valid
while not (0 < x <= 2):
    print("Out of range! Try again: ") 
    x = float(input())

tolerance = float(input("Enter the tolerance: "))

i = 1 
ln_approx = 0
term = (x - 1) #first term in series
#Loop to approximate ln(x)
while abs(term) >= tolerance: #magnitude of the term is either greater than or equal to the tolerance 
    ln_approx += term
    i += 1
    term = (((-1)**(i+1)) * ((x - 1)**i) / i) #Creates the even odd terms for the series

print(f'ln({x}) is approximately {float(ln_approx)}')
print(f'ln({x}) is exactly {log(x)}')
print(f'The difference is {abs(ln_approx - log(x))}')