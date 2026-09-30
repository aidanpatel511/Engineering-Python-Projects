# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: James Willard
# NAME Simon Soto
# NAME Aidan Patel
# NAME Kai Fuentes-Hamilton
# Section: 519
# Assignment: Lab 6 Activity 1 Team
# Date: 22 SEP 2025

from math import * #importing math functions

#Gets input for side length and layers from user
sidelen = float(input("Enter the side length in meters: "))
layers = int(input("Enter the number of layers: "))

#Calculates the area of the sides of the pyramid
square_count = 0
side_area = 0
for i in range(1, layers + 1):
    square_count += 1
    side_area += (square_count * sidelen) * (sidelen * 4)

#Calculates the area of the top of the pyramid
top_area = (layers**2) * (sidelen**2)

total_area = side_area + top_area
print(f'You need {total_area:.2f} m^2 of gold foil to cover the pyramid')