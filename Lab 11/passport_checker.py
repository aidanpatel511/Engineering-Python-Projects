# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: James Willard
# NAME Simon Soto
# NAME Aidan Patel
# NAME Kai Fuentes-Hamilton
# Section: 519
# Assignment: Lab 11 Activity 1 Team
# # Date: 8 NOV 2025

file_name = input("Enter the name of the file: ")
valid_passports = []
passports = []
passport = {}
passport_data = ""
formatted_data = []
valid_passport_texts = []
with open(file_name, "r") as file:
    for line in file:
        line = line.strip()
        if line == "":  # blank line means a new passports information
            passports.append(passport)
            formatted_data.append(passport_data.strip())
            passport = {} #reset passport dictionary for next passport (when a new blank line is reached)
            passport_data = ""
        else:
            fields = line.split()
            for field in fields:
                key, value = field.split(":")
                passport[key] = value #update passport dictionary with key value pairs until a blank line is reached            
            passport_data += line + "\n"
if passport:  # Add the last passport because the file doesn't end with a blank line
    passports.append(passport)
    formatted_data.append(passport_data.strip())
        
    for i, passport in enumerate(passports): #Checks if all required fields keys are each passport dictionary
        if "cid" in passport and "iyr" in passport and "eyr" in passport and "hgt" in passport and "hcl" in passport and "ecl" in passport and "pid" in passport:
                valid_passports.append(passport)
                valid_passport_texts.append(formatted_data[i])         
 
file.close()

with open('valid_passports.txt', 'w') as valid_file: #writes valid passports to new file 
    for passport_text in valid_passport_texts:
        valid_file.write(passport_text + "\n\n")
valid_file.close()
print(f"There are {len(valid_passports)} valid passports")