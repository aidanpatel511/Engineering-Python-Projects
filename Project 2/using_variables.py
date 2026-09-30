# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Aidan
# Section:      519
# Assignment:   Lab 2 Individual 
# Date:         28 8 2025

import math
#Calculation for a Reynolds number with a fluid with velocity (𝑢𝑢) 9 m/s, kinematic viscosity (𝜈𝜈) 0.0015 m^2/s, and a characteristic linear dimension (𝑢𝑢) of 0.875 m.
velocity = 9
viscosity = 0.0015
linear_dimension = 0.875
reynolds_number = (velocity * linear_dimension) / viscosity
print("Reynolds number is " + str((reynolds_number)))

#Calculation of the wavelength of x-rays scattering from a crystal lattice with a distance between crystal layers of 0.029 nm, scattering angle of 35 degrees, and first order diffraction.
scattering_angle = 35
crystal_layers_distance = 0.029
wavelength = (crystal_layers_distance*2)*(math.sin((scattering_angle*math.pi)/180))*1
print("Wavelength is " + str((wavelength)) + " nm")

#Calculation of the production rate of a well after 10 days, if it had an initial production rate (𝑞𝑞𝑖𝑖) of 100 barrels/day, an initial decline rate (𝐷𝐷𝑖𝑖) of 2/day, and a hyperbolic constant (𝑏𝑏) of 0.8.
initial_production = 100 #barrels/day
initial_decline = 2 #/day
HYPERBOLIC_CONSTANT = 0.8
time = 10 #days
future_production_rate = (initial_production/(1 + HYPERBOLIC_CONSTANT*initial_decline*time)**(1/HYPERBOLIC_CONSTANT))
print("Production rate is " + str((future_production_rate)) + " barrels/day")

#Calculation of the change of velocity of a fighter jet for an initial mass of 11000 kg, final mass of 8300 kg, and exhaust velocity of 2029 m/s
initial_mass = 11000 #kg
final_mass = 8300 #kg
exhaust_velocity = 2029 #m/s
print("Change of velocity is " + str((exhaust_velocity*math.log(initial_mass/final_mass))) + " m/s")