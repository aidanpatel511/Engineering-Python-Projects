# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Aidan
# Section:      519
# Assignment:   Lab 4 Individual 
# Date:         14 9 2025


number_1 = float(input("Enter number 1: "))
number_2 = float(input("Enter number 2: "))
number_3 = float(input("Enter number 3: "))

largest = number_1
# Compare to find the largest
if number_2 > largest:
    largest = number_2
if number_3 > largest:
    largest = number_3

print("The largest number is", largest)