# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Aidan
# Section:      519
# Assignment:   Lab 6 Individual 
# Date:         27 9 2025
#importing math functions
import math
#gets input from user
n = int(input("Enter a positive integer: "))
iterations = 0
jug_sequence = [n]
#loop to determine the number of iterations to reach 1
while n != 1:
    if n % 2 == 0:
        n = math.floor(math.sqrt(n))
    else:
        n = math.floor(n ** (3/2))
    jug_sequence.append(n)
    iterations += 1

print(f'The Juggler sequence starting at {jug_sequence[0]} is:')
print(str(jug_sequence).replace("[", "").replace("]", ""))
print(f'It took {iterations} iterations to reach 1')
