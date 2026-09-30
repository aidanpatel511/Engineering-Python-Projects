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
invalid_id = False
valid_hcl_values = "0123456789abcdef"
valid_eye_colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
lines_read = []
valid_ids = 0
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
        if "cid" not in passport or "iyr" not in passport or "eyr" not in passport or "hgt" not in passport or "hcl" not in passport or "ecl" not in passport or "pid" not in passport:
            continue
        invalid_id = False
        for key, value in passport.items():
            #If id iyr is not in between 2015 and 2025 make the id invalid
            if key == "iyr":
                if "\n" in value:
                    value = value[:-1]
                if int(value) < 2015 or int(value) > 2025:
                    invalid_id = True

            #if eyr is not between 2025 and 2035 invalid id is true
            elif key == "eyr":
                if "\n" in value:
                    value = value[:-1]

                if int(value) < 2025 or int(value) > 2035:
                    invalid_id = True

            elif key == "hgt":
                #f cm, the number must be between 150 and 193, inclusive
                #o If in, the number must be between 59 and 76, inclusive
                if "cm" in value:
                    #If there is a new line, exclude it and just get the numbers
                    if "\n" in value:
                        numbers = value[:-3]
                    else:
                        numbers = value[:-2]
                    if int(numbers) < 150 or int(numbers) > 193:
                        invalid_id = True
                elif "in" in value:
                    #If there is a newline, exclude it and just get the numbers
                    if  "\n" in value:
                        numbers = value[:-3]
                    else:
                        numbers = value[:-2]
                    if int(numbers) < 59 or int(numbers) > 76:
                        invalid_id = True
                else:
                    invalid_id = True

            #If hcl has more than 7 characters or less than, invalid id = true
            elif key == "hcl":
                if "\n" in value:
                    value = value[:-1]
                if "#" not in value:
                    invalid_id = True
                if len(value) > 7 or len(value) < 7:
                    invalid_id = True
                for thing in value[1:]:
                    if thing not in valid_hcl_values:
                        invalid_id = True

            #If ecl is not in valid eye colors, invalid_id = true
            elif key == "ecl":
                if "\n" in value:
                    value = value[:-1]
                passed = False
                for eyes in valid_eye_colors:
                    if value == eyes:
                        passed = True
                if passed == False:
                    invalid_id = True

            #if pid characters is less than or more than 9 invalid_id = true
            elif key == "pid":
                if "\n" in value:
                    value = value[:-1]
                if len(value) < 9 or len(value) > 9:
                    invalid_id = True

            #if cid has leadings 0's, invalid_id = true
            elif key == "cid":
                if "\n" in value:
                    value = value[:-1]
                if len(value) < 3 or len(value) > 3:
                    invalid_id = True
                if value[:1] == "0":
                    invalid_id = True
        if invalid_id == False:
            valid_passports.append(passport)
            valid_passport_texts.append(formatted_data[i])         
 
file.close()

with open('valid_passports2.txt', 'w') as valid_file: #writes valid passports to new file 
    for passport_text in valid_passport_texts:
        valid_file.write(passport_text + "\n\n")
valid_file.close()
print(f"There are {len(valid_passports)} valid passports")