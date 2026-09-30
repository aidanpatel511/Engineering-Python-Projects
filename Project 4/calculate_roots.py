# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Aidan
# Section:      519
# Assignment:   Lab 4 Individual 
# Date:         14 9 2025

import math

A = float(input("Please enter the coefficient A: "))
B = float(input("Please enter the coefficient B: "))
C = float(input("Please enter the coefficient C: "))

if A == 0 and B == 0:
    if C != 0:
        print("You entered an invalid combination of coefficients!") #No solution

elif A == 0:
    root = -C / B
    print(f"The root is x = {root}")
elif A != 0:
    discriminant = B**2 - 4*A*C
    if discriminant > 0:
        root1 = (-B + math.sqrt(discriminant)) / (2*A) # Regular Quadratic formula
        root2 = (-B - math.sqrt(discriminant)) / (2*A)
        if root1 > root2:
            print(f"The roots are x = {root1} and x = {root2}")
        else:
            print(f"The roots are x = {root2} and x = {root1}")
    elif discriminant == 0:
        root3 = -B / (2*A)
        print(f"The root is x = {root3}")
    elif discriminant < 0:
        root4 = (-B/(2*A))
        imaginary_root1 = ((math.sqrt(abs(discriminant))) / (2*A)) #takes abs of discriminant and adds i later
        root5 = (-B/(2*A))
        imaginary_root2 = ((math.sqrt(abs(discriminant))) / (2*A))
        if root4 > root5:
            print(f"The roots are x = {root4} + {imaginary_root1}i and x = {root5} - {imaginary_root2}i")
        else:
            print(f"The roots are x = {root5} + {imaginary_root2}i and x = {root4} - {imaginary_root1}i")