# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Aidan
# Section:      519
# Assignment:   Lab 6 Individual 
# Date:         27 9 2025

#Gets digits from the user
firstint = int(input("Enter an integer: "))
secondint = int(input("Enter another integer: "))

#Loop to figure out what to print
for i in range(1, 101):
    if i % firstint == 0 and i % secondint == 0:
        print("Howdy Whoop")
    elif i % firstint == 0:
        print("Howdy")
    elif i % secondint == 0:
        print("Whoop")
    else:
        print(i)