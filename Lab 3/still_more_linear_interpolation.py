# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: James Willard
# NAME Simon Soto
# NAME Aidan Patel
# NAME Kai Fuentes-Hamilton
# Section: 519
# Assignment: Lab 3 Activity 2 Team
# Date: 6 SEP 2025

#from math import *

#time1 = float(input("Enter time 1: ")) #seconds
#x_position1 = float(input("Enter the x position of the object at time 1: "))
#y_position1 = float(input("Enter the y position of the object at time 1: "))
#z_position1 = float(input("Enter the z position of the object at time 1: "))

#time2 = float(input("Enter time 2: ")) #seconds
#x_position2 = float(input("Enter the x position of the object at time 2: "))
#y_position2 = float(input("Enter the y position of the object at time 2: "))
#z_position2 = float(input("Enter the z position of the object at time 2: "))

#calculation_t = float((time2-time1)/4)
#y = (slope)(x - x1) + y1
#xslope = ((x_position2 - x_position1)/(time2-time1)) * (calculation_t - time1) + x_position1
#yslope = ((y_position2 - y_position1)/(time2-time1)) * (calculation_t - time1) + y_position1
#zslope = ((z_position2 - z_position1)/(time2-time1)) * (calculation_t - time1) + z_position1

#calculation_x_position = float((x_position2-x_position1)/4)
#calculation_y_position = float((y_position2-y_position1)/4)
#calculation_z_position = float((z_position2-z_position1)/4)

#print(f"At time {time1} seconds the object is at ({calculation[0]:.2f}, {calculation[1]:.2f}, {calculation[2]:.2f})")
#print(f"At time {calculation_t + time1} seconds the object is at ({calculation[0]:.2f}, {calculation[1]:.2f}, {calculation[2]:.2f})")
#print(f"At time {2*calculation_t + time1} seconds the object is at ({calculation[0]:.2f}, {calculation[1]:.2f}, {calculation[2]:.2f})")
#print(f"At time {3*calculation_t + time1} seconds the object is at ({calculation[0]:.2f}, {calculation[1]:.2f}, {calculation[2]:.2f})")
#print(f"At time {time2} seconds the object is at ({calculation[0]:.2f}, {calculation[1]:.2f}, {calculation[2]:.2f})")

#for i in range (5):
   # print(f"At time {i*calculation_t + time1:.2f} seconds the object is at ({x_position1 + i*xslope:.3f}, {y_position1 + i*yslope:.3f}, {z_position1 + i*zslope:.3f})")







# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: James Willard
# NAME Simon Soto
# NAME Aidan Patel
# NAME Kai Fuentes-Hamilton
# Section: 519
# Assignment: Lab 3 Activity 2 Team
# Date: 6 SEP 2025
#

from math import *

time1 = float(input("Enter time 1: ")) #seconds
x_position1 = float(input("Enter the x position of the object at time 1: "))
y_position1 = float(input("Enter the y position of the object at time 1: "))
z_position1 = float(input("Enter the z position of the object at time 1: "))

time2 = float(input("Enter time 2: ")) #seconds
x_position2 = float(input("Enter the x position of the object at time 2: "))
y_position2 = float(input("Enter the y position of the object at time 2: "))
z_position2 = float(input("Enter the z position of the object at time 2: "))

calculation_t = float((time2-time1)/4)
#y = (slope)(x - x1) + y1
xslope = ((x_position2 - x_position1)/(time2-time1))
yslope = ((y_position2 - y_position1)/(time2-time1))
zslope = ((z_position2 - z_position1)/(time2-time1))

xinterval1 = xslope * (calculation_t) + x_position1
yinterval1 = yslope * (calculation_t) + y_position1
zinterval1 = zslope * (calculation_t) + z_position1

xinterval2 = xslope * (2 * calculation_t) + x_position1
yinterval2 = yslope * (2 * calculation_t) + y_position1
zinterval2 = zslope * (2 * calculation_t) + z_position1

xinterval3 = xslope * (3 * calculation_t) + x_position1
yinterval3 = yslope * (3 * calculation_t) + y_position1
zinterval3 = zslope * (3 * calculation_t) + z_position1

print(f"At time {time1:.2f} seconds the object is at ({x_position1:.3f}, {y_position1:.3f}, {z_position1:.3f})")
print(f"At time {(time1 + calculation_t):.2f} seconds the object is at ({xinterval1:.3f}, {yinterval1:.3f}, {zinterval1:.3f})")
print(f"At time {(time1 + 2 * calculation_t):.2f} seconds the object is at ({xinterval2:.3f}, {yinterval2:.3f}, {zinterval2:.3f})")
print(f"At time {(time1 + 3 * calculation_t):.2f} seconds the object is at ({xinterval3:.3f}, {yinterval3:.3f}, {zinterval3:.3f})")
print(f"At time {time2:.2f} seconds the object is at ({x_position2:.3f}, {y_position2:.3f}, {z_position2:.3f})")