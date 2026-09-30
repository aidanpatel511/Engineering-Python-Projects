# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Aidan
# Section:      519
# Assignment:   Lab 2 Individual 
# Date:         31 8 2025

import math
#initial and final positions/times
x0 = 8
y0 = 6
z0 = 7
x2 = -5
y2 = 30
z2 = 9
t0 = 12.0 #seconds
t1 = 30.0 #seconds
t2 = 85.0 #seconds
t_2 = 37.5 #seconds
t3 = 45.0 #seconds
t4 = 52.5 #seconds
t5 = 60.0 #seconds
# First interpolation point
n=1
for i in range(4):
    x1 = ((x2 - x0)/(t2 - t0) * (t1 - t0) + x0)
    y1 = ((y2 - y0)/(t2 - t0) * (t1 - t0) + y0)
    z1 = ((z2 - z0)/(t2 - t0) * (t1 - t0) + z0)
    print("At time", str(t1), "seconds:")
    print("x" + str(n), "=", str(x1), "m")
    print("y" + str(n), "=", str(y1), "m")
    print("z" + str(n), "=", str(z1), "m")
    print("-----------------------")
    t1 += 7.5
    n +=1

# Fifth interpolation point
n=5
x1 = ((x2 - x0)/(t2 - t0) * (t5 - t0) + x0)
y1 = ((y2 - y0)/(t2 - t0) * (t5 - t0) + y0)
z1 = ((z2 - z0)/(t2 - t0) * (t5 - t0) + z0)
print("At time", str(t5), "seconds:")
print("x" + str(n), "=", str(x1), "m")
print("y" + str(n), "=", str(y1), "m")
print("z" + str(n), "=", str(z1), "m")