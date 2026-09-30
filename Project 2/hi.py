import math
    
timep1 = 12
timep2 = 85
#12 seconds, (8,6,7) meters
#85 seconds, (-5,30,9) meters
#seconds is x1, coordinate is y1, x is the time in seconds
#y = (slope)(x - x1) + y1
xslope = (-5-8)/(timep2-timep1)
yslope = (30-6)/(timep2-timep1)
zslope = (9-7)/(timep2-timep1)
x1 = xslope*(30-timep1) + 8
y1 = yslope*(30-timep1) + 6
z1 = zslope*(30-timep1) + 7
x2 = xslope*(37.5-timep1) + 8
y2 = yslope*(37.5-timep1) + 6
z2 = zslope*(37.5-timep1) + 7
x3 = xslope*(45.0-timep1) + 8
y3 = yslope*(45.0-timep1) + 6
z3 = zslope*(45.0-timep1) + 7
x4 = xslope*(52.5-timep1) + 8
y4 = yslope*(52.5-timep1) + 6
z4 = zslope*(52.5-timep1) + 7
x5 = xslope*(60.0-timep1) + 8
y5 = yslope*(60.0-timep1) + 6
z5 = zslope*(60.0-timep1) + 7


print("At time 30.0 seconds:")
print("x1 =", x1, "m")
print("y1 =", y1, "m")
print("z1 =", z1, "m")
print("-----------------------")
print("At time 37.5 seconds:")
print("x2 =", x2, "m")
print("y2 =", y2, "m")
print("z2 =", z2, "m")
print("-----------------------")
print("At time 45.0 seconds:")
print("x3 =", x3, "m")
print("y3 =", y3, "m")
print("z3 =", z3, "m")
print("-----------------------")
print("At time 52.5 seconds:")
print("x4 =", x4, "m")
print("y4 =", y4, "m")
print("z4 =", z4, "m")
print("-----------------------")
print("At time 60.0 seconds:")
print("x5 =", x5, "m")
print("y5 =", y5, "m")
print("z5 =", z5, "m")

print(x4)