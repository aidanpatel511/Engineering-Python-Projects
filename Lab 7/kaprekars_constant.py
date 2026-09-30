# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Aidan
# Section:      519
# Assignment:   Lab 6 Individual 
# Date:         4 10 2025

origin_number = int(input("Enter a four-digit integer: ")) #Gets number from user

list_num = [] #Creates empty list to store digits
for i in range(len(str(origin_number))): #Loops 4 times to get each digit
    list_num.append(int(str(origin_number)[i]))
if len(str(origin_number)) < 4:
    while len(list_num) < 4:
        list_num.insert(0, 0)
number = origin_number #Sets number to original number

n = 0 #Iteration counter
lst = []

while number != 6174: #Loops until number is 6174
    lst.append(number)
    if len(str(number)) < 4:
        while len(list_num) < 4:
            list_num.insert(0, 0)
    list_num.sort(reverse=True) #Reverses list to get descending order
    number_useR = 0
    for d in list_num:
        number_useR = number_useR * 10 + d
    list_num.sort() #Sorts list to get ascending order
    number_useS = 0
    for d in list_num:
        number_useS = number_useS * 10 + d
    number_new = number_useR - number_useS
    number = number_new #Updates number for next iteration

    list_num = [] #Creates empty list to store digits
    for i in range(len(str(number))): #Loops 4 times to get each digit
        list_num.append(int(str(number)[i]))
    n += 1 #Increments iteration counter
    if number == 0:
        lst.append(0)
        print(" > ".join(str(num) for num in lst))
        print(f"{origin_number} reaches 0 via Kaprekar's routine in {n} iterations")
        break
    elif number == 6174:
        lst.append(6174)
        print(" > ".join(str(num) for num in lst))
        print(f"{origin_number} reaches 6174 via Kaprekar's routine in {n} iterations")
        break
