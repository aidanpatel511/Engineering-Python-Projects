# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."

# Name:         Aidan
# Section:      519
# Assignment:   Lab 13 Individual 
# Date:        24 11 2025

import turtle as t

def parta(turn_angle):
    '''Creates a turtle drawing based on the input turn angle.'''
    # Initialize turtle
    t.speed(100)
    t.penup()
    t.goto(0, 0)
    t.pendown()
    # Calculate the number of iterations needed to return to starting point
    angle_sum = 0
    iterations = 0
    while angle_sum % 360 != 0 or iterations == 0:
        angle_sum += turn_angle
        iterations += 1

    # Draw the figure
    for i in range(iterations):
        t.forward(100) 
        t.left(turn_angle)  # Turn left by the specified angle

def partb(string):
    '''Creates a turtle drawing based on the input string of '0's and '1's.'''
    # Initialize turtle
    t.speed(100)
    t.penup()
    t.goto(0, 0)
    t.pendown()
    
    angle_0 = 30
    angle_1 = -114
    
    # Draw the figure
    for char in string:
        if char == '0':
            t.left(angle_0)  # Turn left by 30 degrees
            t.forward(100) 
        elif char == '1':
            t.left(angle_1)  # Turn left by -114 degrees
            t.forward(100) 

def partc(sequence, angle_0, angle_1):
    '''Creates a turtle drawing a spiral based on the input sequence and angles for '0' and '1'.'''
    # Initialize turtle
    t.speed(100)
    t.penup()
    t.goto(0, 0)
    t.pendown()
    
    # Draw the figure
    distance = 5
    for char in sequence:
        if char == '0':
            t.left(angle_0)  # Turn left by angle corresponding to '0'
            t.forward(distance)         
        elif char == '1':
            t.left(angle_1)  # Turn left by angle corresponding to '1'
            t.forward(distance) 

#Main code
parta(160)
input()
t.reset()
parta(141)
input()
t.reset()
partb("01001")
input()
t.reset()
partb("01001011")
input()
t.reset()
seq1 = "110100100010000100000100000010000000100000000100000000010000000000100000000000100000000000010000000000000100000000000000100000000000000010000000000000000100000000000000000100000000000000000010000000000000000000"
partc(seq1, 0, 90)
input()
t.reset()
partc(seq1, 0, 30)
input()
t.reset()
seq2 = "110100100010000100000100000010000000100000000100000000010000000000100000000000100000000000010000000000000100000000000000100000000000000010000000000000000100000000000000000100000000000000000010000000000000000000100000000000000000000100000000000000000000010000000000000000000000100000000000000000000000100000000000000000000000010000000000000000000000000100000000000000000000000000100000000000000000000000000010000000000000000000000000000100000000000000000000000000000100000000000000000000000000000010000000000000000000000000000000100000000000000000000000000000000100000000000000000000000000000000010000000000000000000000000000000000100000000000000000000000000000000000100000000000000000000000000000000000010000000000000000000000000000000000000100000000000000000000000000000000000000100000000000000000000000000000000000000010000000000000000000000000000000000000000100000000000000000000000000000000000000000100000000000000000000000000000000000000000010000000000000000000000000000000000000000000100000000000000000000000000000000000000000000100000000000000000000000000000000000000000000010000000000000000000000000000000000000000000000100000000000000000000000000000000000000000000000100000000000000000000000000000000000000000000000010000000000000000000000000000000000000000000000000"
partc(seq2, 0, 150)
input()
t.reset()
partc(seq2, 5, 108)
t.done()

