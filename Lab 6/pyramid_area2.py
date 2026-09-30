    # By submitting this assignment, I agree to the following:
    # "Aggies do not lie, cheat, or steal, or tolerate those who do."
    # "I have not given or received any unauthorized aid on this assignment."
    #
    # Names: James Willard
    # NAME Simon Soto
    # NAME Aidan Patel
    # NAME Kai Fuentes-Hamilton
    # Section: 519
    # Assignment: Lab 6 Activity 2 Team
    # Date: 28 SEP 2025

from math import * #importing math functions

#Gets input for side length and layers from user
sidelen = float(input("Enter the side length in meters: "))
layers = int(input("Enter the number of layers: "))

#Calculates the area of the sides of the pyramid
square_count = (layers * (layers + 1)) / 2
side_area = (square_count * sidelen) * (sidelen * 4)

#Calculates the area of the top of the pyramid
top_area = (layers**2) * (sidelen**2)

total_area = side_area + top_area
print(f'You need {total_area:.2f} m^2 of gold foil to cover the pyramid')
