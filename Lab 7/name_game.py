# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Aidan
# Section:      519
# Assignment:   Lab 6 Individual 
# Date:         4 10 2025

#Gets name from user
name = input("What is your name? ")

# if name[0].upper() in ("A", "E", "I", "O", "U", "Y"): #Checks if name starts with a vowel
#     print(f"{name}, {name}, Bo-B{name[0:].lower()}")
#     #Prints second rhyme
#     print(f"Banana-Fana Fo-F{name[0:].lower()}")
#     #Prints third rhyme
#     print(f"Me Mi Mo-M{name[0:].lower()}")
#     print(f"{name}!")
# elif (name[0:3].upper()) not in ("A", "E", "I", "O", "U","Y"): #Checks for triple consonant
#     print(f"{name}, {name}, Bo-B{name[3:].lower()}")
#     #Prints second rhyme
#     print(f"Banana-Fana Fo-F{name[3:].lower()}")
#     #Prints third rhyme
#     print(f"Me Mi Mo-M{name[3:].lower()}")
#     print(f"{name}!")
# elif (name[0].upper() and name[1].upper()) not in ("A", "E", "I", "O", "U","Y"): #Checks for double consonant
#     print(f"{name}, {name}, Bo-B{name[2:].lower()}")
#     #Prints second rhyme
#     print(f"Banana-Fana Fo-F{name[2:].lower()}")
#     #Prints third rhyme
#     print(f"Me Mi Mo-M{name[2:].lower()}")
#     print(f"{name}!")
# else:
#     #Prints name twice followed by first rhyme
#     print(f"{name}, {name}, Bo-B{name[1:].lower()}")
#     #Prints second rhyme
#     print(f"Banana-Fana Fo-F{name[1:].lower()}")
#     #Prints third rhyme
#     print(f"Me Mi Mo-M{name[1:].lower()}")
#     print(f"{name}!")

vowels = ("A", "E", "I", "O", "U","Y")
index = 0
for char in range(len(name)): #Loops through each character in name
    if name[char].upper() in vowels: #Checks if character is a vowel
        index = char
        break #Exits loop if vowel is found

rhymed_name = name[index:] #Slices name to start from first vowel
#Prints name twice followed by first rhyme
print(f"{name}, {name}, Bo-B{rhymed_name.lower()}")
#Prints second rhyme
print(f"Banana-Fana Fo-F{rhymed_name.lower()}")
#Prints third rhyme
print(f"Me Mi Mo-M{rhymed_name.lower()}")
print(f"{name}!")
    