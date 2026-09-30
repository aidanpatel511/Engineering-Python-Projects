# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Aidan
# Section:      519
# Assignment:   Lab 6 Individual 
# Date:         4 10 2025

numbers = input("Enter numbers: ") #Gets numbers from user  
number_list = []
for i in numbers.split(): 
    number_list.append(int(i)) #Converts each number to integer and adds to list


sum = 0
for i in range(len(number_list)):
    sum += number_list[i]

left_sum = 0
left_list = []
i = 0
while i < len(number_list):
    if left_sum != sum:
        left_sum += number_list[i]
        left_list.append(number_list[i])
        sum -= number_list[i]
        number_list.pop(i)
    else:
        break
if number_list == []:
    print("Cannot split evenly")
else:
    print(f'Left: {left_list}')
    print(f'Right: {number_list}')
    print(f'Both sum to {left_sum}')