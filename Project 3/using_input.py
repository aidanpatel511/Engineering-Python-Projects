# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Aidan
# Section:      519
# Assignment:   Lab 3 Individual 
# Date:         5 9 2025

import math
print("This program calculates the Reynolds number given velocity, length, and viscosity")
#Calculation for a Reynolds number with a fluid with velocity (𝑢𝑢) 9 m/s, kinematic viscosity (𝜈𝜈) 0.0015 m^2/s, and a characteristic linear dimension (𝑢𝑢) of 0.875 m.
velocity = float(input("Please enter the velocity (m/s): "))
linear_dimension = float(input("Please enter the length (m): "))
viscosity = float(input("Please enter the viscosity (m^2/s): "))
reynolds_number = (velocity * linear_dimension) / viscosity
print(f"Reynolds number is {reynolds_number:.0f}")

#Calculation of the wavelength of x-rays scattering from a crystal lattice with a distance between crystal layers of 0.029 nm, scattering angle of 35 degrees, and first order diffraction.
print("This program calculates the wavelength given distance and angle")
crystal_layers_distance = float(input("Please enter the distance (nm): "))
scattering_angle = float(input("Please enter the angle (degrees): "))
wavelength = (crystal_layers_distance*2)*(math.sin((scattering_angle*math.pi)/180))*1
print(f"Wavelength is {wavelength:.4f} nm")

#Calculation of the production rate of a well after 10 days, if it had an initial production rate (𝑞𝑞𝑖𝑖) of 100 barrels/day, an initial decline rate (𝐷𝐷𝑖𝑖) of 2/day, and a hyperbolic constant (𝑏𝑏) of 0.8.
print("This program calculates the production rate given time, initial rate, and decline rate")
time = float(input("Please enter the time (days): ")) #days
initial_production = float(input("Please enter the initial rate (barrels/day): "))
initial_decline = float(input("Please enter the decline rate (1/day): "))
HYPERBOLIC_CONSTANT = 0.8
future_production_rate = (initial_production/(1 + HYPERBOLIC_CONSTANT*initial_decline*time)**(1/HYPERBOLIC_CONSTANT))
print(f"Production rate is {future_production_rate:.2f} barrels/day")

#Calculation of the change of velocity of a fighter jet for an initial mass of 11000 kg, final mass of 8300 kg, and exhaust velocity of 2029 m/s
print("This program calculates the change of velocity given initial mass, final mass, and exhaust velocity")
initial_mass = float(input("Please enter the initial mass (kg): ")) #kg
final_mass = float(input("Please enter the final mass (kg): ")) #kg
exhaust_velocity = float(input("Please enter the exhaust velocity (m/s): ")) #m/s
print(f"Change of velocity is {(exhaust_velocity*math.log(initial_mass/final_mass)):.1f} m/s")