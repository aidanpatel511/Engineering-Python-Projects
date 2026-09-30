# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: James Willard
# NAME Simon Soto
# NAME Aidan Patel
# NAME Kai Fuentes-Hamilton
# Section: 519
# Assignment: Lab 4 Activity 4 Team
# Date: 14 SEP 2025

############ Part A ############
a_input = input("Enter True or False for a: ")
b_input = input("Enter True or False for b: ")
c_input = input("Enter True or False for c: ")

a = (a_input.lower() == "t" or a_input.lower() == "true")
b = (b_input.lower() == "t" or b_input.lower() == "true")
c = (c_input.lower() == "t" or c_input.lower() == "true")

############ Part B ############
value_1 = a and b and c
value_2 = a or b or c
print(f'a and b and c: {value_1}')
print(f'a or b or c: {value_2}')

############ Part C ############
XOR_of_ab = (a or b) and not(a and b)
print("XOR:", str(XOR_of_ab))
odd_number = (a and not(b or c)) or (b and not(a or c)) or (c and not (a or b)) or (a and b and c)
print("Odd number:", str(odd_number))

############ Part D ############
value3 = (not (a and not b) or (not c and b)) and (not b) or (not a and b and not c) or (a and not b)
value4 = (not ((b or not c) and (not a or not c))) or (not (c or not (b and c))) or (a and not c) and (not a or (a and b and c) or (a and ((b and not c) or (not b))))
print(f'Complex 1: {value3}')
print(f'Complex 2: {value4}')
print(f'Simple 1: {value3}')
print(f'Simple 2: {value4}')