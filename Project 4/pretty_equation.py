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

#Input from user
coefficient_A = int(input("Please enter the coefficient A: "))
coefficient_B = int(input("Please enter the coefficient B: "))
coefficient_C = int(input("Please enter the coefficient C: "))

#strings to use
shown_coeff1 = ""
shown_coeff2 = ""
shown_coeff3 = ""

#Negative values
if coefficient_A < 0:
    shown_coeff1 += "- "
if coefficient_B < 0:
    shown_coeff2 += "- "
elif (coefficient_A != 0):
    shown_coeff2 += "+ "
if coefficient_C <= 0:
    shown_coeff3 += "- "
elif (not((coefficient_B == 0) and (coefficient_A == 0))):
      shown_coeff3 += "+ "

#Create equations
if abs(coefficient_A) > 1:
    shown_coeff1 += str(abs(coefficient_A))
    shown_coeff1 += "x^2 "
elif abs(coefficient_A) == 1:
    shown_coeff1 += "x^2 "
elif abs(coefficient_A) == 0:
    shown_coeff1 = ""
if abs(coefficient_B) > 1:
    shown_coeff2 += str(abs(coefficient_B))
    shown_coeff2 += "x "
elif abs(coefficient_B) == 1:
    shown_coeff2 += "x "
elif abs(coefficient_B) == 0:
    shown_coeff2 = ""
if abs(coefficient_C) >= 1:
    shown_coeff3 += str(abs(coefficient_C))
    shown_coeff3 += " "
elif abs(coefficient_C) == 0:
    shown_coeff3 = ""

#print equation
print(f"The quadratic equation is {shown_coeff1}{shown_coeff2}{shown_coeff3}= 0")
