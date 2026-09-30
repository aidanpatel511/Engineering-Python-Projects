# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Aidan
# Section:      519
# Assignment:   Lab 11 Individual 
# Date:        8 11 2025

file_name = input("Enter the name of the file: ")
valid_barcodes = []  

with open(file_name, 'r') as file: #opens file and reads barcodes to and uses function to check validity
    barcodes = file.readlines()
for barcode in barcodes:
    barcode = barcode.strip()
    group1 = barcode[0:-1:2]
    group2 = barcode[1:-1:2]
    sumg1 = sum(int(x) for x in group1)
    sumg2 = sum(int(x) for x in group2)
    total = sumg1 + sumg2*3
    check_digit = (10 - total%10)
    if check_digit == int(barcode[-1]):
        valid_barcodes.append(barcode)
file.close()

with open('valid_barcodes.txt', 'w') as valid_file: #writes valid barcodes to new file 
    for i in range(len(valid_barcodes)):
        valid_file.write(valid_barcodes[i] + '\n')
valid_file.close()
print(f"There are {len(valid_barcodes)} valid barcodes")