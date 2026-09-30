# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Aidan
# Section:      519
# Assignment:   Lab 1
# Date:         25 8 2025

import math

#Calculation for a Reynolds number with a fluid with velocity (𝑢𝑢) 9 m/s, kinematic viscosity (𝜈𝜈) 0.0015 m^2/s, and a characteristic linear dimension (𝑢𝑢) of 0.875 m.
print("Reynolds number is " + str((9*0.875)/0.0015))

#Calculation of the wavelength of x-rays scattering from a crystal lattice with a distance between crystal layers of 0.029 nm, scattering angle of 35 degrees, and first order diffraction.
print("Wavelength is " + str((0.029*2)*(math.sin((35*math.pi)/180))*1) + " nm")

#Calculation of the production rate of a well after 10 days, if it had an initial production rate (𝑞𝑞𝑖𝑖) of 100 barrels/day, an initial decline rate (𝐷𝐷𝑖𝑖) of 2/day, and a hyperbolic constant (𝑏𝑏) of 0.8.
print("Production rate is " + str(100/((1 + 0.8*2*10))**(1/0.8)) + " barrels/day")

#Calculation of the change of velocity of a fighter jet for an initial mass of 11000 kg, final mass of 8300 kg, and exhaust velocity of 2029 m/s
print("Change of velocity is " + str(2029*math.log(11000/8300)) + " m/s")
