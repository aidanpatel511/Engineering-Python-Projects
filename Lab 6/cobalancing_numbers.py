# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Aidan
# Section:      519
# Assignment:   Lab 6 Individual 
# Date:         27 9 2025

#Gets input from user
n = int(input("Enter a value for n: "))

#gets sum of digits to n
sum = 0
for i in range(1, n + 1):
    sum += i

current_sum = 0
r = 0
num_check = n + 1
#Loop to find the balancing number (if it exists)
while current_sum < sum:
    r += 1 
    current_sum += (num_check)
    num_check += 1
    if current_sum == sum:
        print(f'{n} is a co-balancing number with r={r}')
        break
    elif current_sum > sum:
        print(f'{n} is not a co-balancing number')
        break


