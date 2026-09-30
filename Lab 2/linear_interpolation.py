# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Aidan Patel
# Simon Soto
# Kai Fuentes-Hamilton
# James Willard
# Section: 519
# Assignment: Lab 2 Part 2 (Team)
# Date: 29 AUG 2025
#
#
# YOUR CODE HERE
#

import math
#First kilometers and minutes = (10,2029)
#Last Kilometers and minutes = (55,23029)
x1 = 10  #Minutes
y1 = 2029  #Kilometers
x2 = 55  #Minutes
y2 = 23029  #Kilometers
#y = (slope)(x - x1) + y1

km1 = ((y2-y1)/(x2 - x1)) * (25 - x1) + y1
print("Part 1:")
print("For t =", 25, "minutes, the position p =", km1, "kilometers")

houston = 6745 * 2*math.pi
km2 = ((y2-y1)/(x2 - x1)) * (300 - x1) + y1
distance_from_houston = km2 % houston
print("Part 2:")
print("For t =", 300, "minutes, the position p =", distance_from_houston, "kilometers")