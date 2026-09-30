# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Aidan
# Section:      519
# Assignment:   Lab 11 Individual 
# Date:        7 11 2025

file_name = input("Enter the output filename: ")
P = float(input("Enter the principal amount: "))
N = int(input("Enter the term length (months): "))
i = float(input("Enter the annual interest rate: "))
M = (P * (i/12)) / (1 - (1/(1 + i/12)**(N)))  #Calculates monthly payment

month_number = 0
amount_remaining = P
total_interest_accrued = 0.0

with open(file_name, 'w') as file:
    #Header
    file.write("Month,Total Accrued Interest,Loan Balance\n")
    #Starting amonuts
    file.write(f"{month_number},${total_interest_accrued:.2f},${amount_remaining:.2f}\n")   
    while amount_remaining > 0.01:
        month_number += 1       
        # Calculate monthly accrued interest and total accrued interest
        monthly_accrued_interest = amount_remaining * (i / 12)
        total_interest_accrued += monthly_accrued_interest
        if amount_remaining + monthly_accrued_interest < M:
            M = amount_remaining + monthly_accrued_interest       
        # Calculate new balance remaining
        amount_remaining = amount_remaining + monthly_accrued_interest - M
        file.write(f"{month_number},${total_interest_accrued:.2f},${amount_remaining:.2f}\n")