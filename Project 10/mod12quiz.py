import numpy as np
arraylst = []
file = open("module12quizF25.txt", "r")
for line in file:
    line = line.strip()
    arraylst.append(line)
array = np.array(arraylst).reshape(100,100)
# print(array)
#First part of key
row6 = array[5]
# print(row6)
sum = 0
for i in row6:
    sum += int(i)
letter1 = sum/100
print(letter1) #M

#Second part of key
smallest = []
for i in range(len(array)):
    for j in range(len(array[i])):
        if j == 28:
            smallest.append(array[i][j])
minimum = min(smallest)
print(minimum) #A

#Third Part of Key
Max = []
for i in range(len(array)):
    for j in range(len(array[i])):
        if j == 23:
            Max.append(array[i][j])
# print(Max[0])
# print(Max[1])
print(Max[2]) #G

#Forth part of key
lst = []
print(array[99][-1])
print(array[99][-2])
print(array[99][-3]) #I

#Fifth Part of Key
print(array[90][-3]) #C
key = "MAGIC"
alphabet1 = "abcdefghijclmnopqrstuvwxyz"
cypherbet = "magicdefhjklnopqrstuvwxyzb"
hiddenmsg = "tcgscufpxiz" #Secrethowdy
