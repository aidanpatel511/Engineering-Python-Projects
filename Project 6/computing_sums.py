# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Aidan
# Section:      519
# Assignment:   Lab 6 Individual 
# Date:         27 9 2025

#Gets integers from the user
firstnum = int(input("Enter an integer: "))
secondnum = int(input("Enter another integer: "))

#Calculates sum by taking each integer in the loop and adding it to var (sum)
sum = 0
for i in range(firstnum, secondnum + 1):
    sum += i
print(f'The sum of all integers from {firstnum} to {secondnum} is {sum}')