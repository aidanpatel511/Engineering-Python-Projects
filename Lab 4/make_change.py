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
# Date: 9 SEP 2025

amount_paid = float(input("How much did you pay? "))
amount_cost = float(input("How much did it cost? "))
change = round(amount_paid - amount_cost, 2)
print(f'You received ${change:.2f} in change. That is...') #money remaining

# sets the type of currency to 0 
quarters = 0
dimes = 0
nickels = 0
pennies = 0
still_have_money = True
while still_have_money:
    change = round(change,2)
    if change >= .25:
        quarters += 1
        change -= .25
    elif change >= .1:
        dimes += 1
        change -= .1
    elif change >= .05:
        nickels += 1
        change -= .05
    elif change >= .01:
        pennies += 1
        change -= .01
    else:
        still_have_money = False

if quarters > 1:
    print(f'{quarters} quarters')
elif quarters == 1: 
    print(f'{quarters} quarter')
else: 
    pass

if dimes > 1:
    print(f'{dimes} dimes')
elif dimes == 1: 
    print(f'{dimes} dime')
else: 
    pass

if nickels > 1:
    print(f'{nickels} nickels')
elif nickels == 1:  
    print(f'{nickels} nickel')
else: 
    pass

if pennies > 1:
    print(f'{pennies} pennies')
elif pennies == 1: 
    print(f'{pennies} penny')
else: 
    pass