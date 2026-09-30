# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Aidan
# Section:      519
# Assignment:   Lab 4 Individual 
# Date:         14 9 2025


days = int(input("Please enter a positive value for day: "))
gadgets = 0
if days < 1:
    print("You entered an invalid number!")
else:
    if days <= 10:
        gadgets = 10 * days
    elif days <= 50:
        gadgets = 100 + (days*(days+1)//2) - 55 #Adds the amount in the first 10 days to the sum of the next days subtracting the sum in first 10 days
    elif days <= 100:
        gadgets = 100 + (50*(51)//2) - 55 + ((days - 50) * 50) #Get sum for first 50 then its just 50 times the amount of days left
    else:
        gadgets = 100 + (50*(51)//2) - 55 + ((100 - 50) * 50) #Same amount as 100 days cuz it stops after day 100
    print(f"The sum total number of gadgets produced on day {days} is {gadgets}")