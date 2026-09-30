# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Aidan
# Section:      519
# Assignment:   Lab 3 Individual 
# Date:         6 9 2025


side_length = float(input("Please enter the side length: "))
from math import *

def printresult(shape, side, area):
    '''Print the result of the calculation'''
    print(f'A {shape} with side {side:.2f} has area {area:.3f}')
    if shape == "triangle":
        area = triangle_area
    elif shape == "square":
        area = square_area
    elif shape == "pentagon":
        area = pentagon_area
    elif shape == "hexagon":
        area = hexagon_area
    elif shape == "dodecagon":
        area = dodecagon_area
#Area of an equilateral triangle
triangle_area = (sqrt(3)/4)*(side_length**2)

#Area of a square
square_area = side_length*side_length

#Area of a pentagon
pentagon_area = 0.25*(sqrt(5*(5+2*(sqrt(5))))) * (side_length**2)

#Area of a hexagon
hexagon_area = ((3*(sqrt(3)))/2)*side_length**2

#Area of a dodecagon
dodecagon_area = 3*side_length**2*(2 + sqrt(3))


printresult("triangle", side_length, triangle_area)
printresult("square", side_length, square_area)
printresult("pentagon", side_length, pentagon_area)
printresult("hexagon", side_length, hexagon_area)
printresult("dodecagon", side_length, dodecagon_area)
