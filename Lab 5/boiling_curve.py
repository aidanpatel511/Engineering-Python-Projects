# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Aidan
# Section:      519
# Assignment:   Lab 3 Individual 
# Date:         19 9 2025


#Step 1 → Gathering Information Neccessary for Linear Interpolation
#Variables Needed
#excess_temp #Has the user input the excess temp for me to use
#Ax, Ay #Data points at point A (x, y)
#Bx By  #Data points at point B (x, y)
#Cx, Cy #Data points at point C (x, y)
#Dx, Dy #Data points at point D (x, y)
#Ex, Ey #Data points at point E (x, y)
#m =  #(math.log(_y-_y)/math.log(_x - _x))
#Determined by the region of the graph
#heat_flux = #_y(excess_temp/_x)^m
#Determined by the region of the graph

import math

Ax = 1.3
Ay = 1000
Bx = 5
By = 7000
Cx = 30
Cy = 1.5*(10**6)
Dx = 120
Dy = 2.5*(10**4)
Ex = 1200
Ey = 1.5*(10**6)
excess_temp = float(input("Enter the excess temperature: "))

#Step 2 → Determine the Region of the Graph The Point is Located
#I’ll use the output for the excess temperature to determine where on the graph the point is
if 1 <= excess_temp < 5:
    m = (math.log(By / Ay)/math.log(Bx / Ax)) #Free Convection section (use points A and B)
    y0 = Ay
    x0 = Ax

#Step 3 → Calculate the Heat Flux
#I’ll calculate the heat_flux using the corresponding equation and print it out
    heat_flux = y0*(excess_temp/x0)**m
    heat_flux = round(heat_flux, 0)
    print(f'The surface heat flux is approximately {int(heat_flux)} W/m^2')

elif 5 <= excess_temp < 30:
    m = (math.log(Cy / By)/math.log(Cx / Bx)) #Nucleate section (use point B and C)
    y0 = By
    x0 = Bx

#Step 3 → Calculate the Heat Flux
#I’ll calculate the heat_flux using the corresponding equation and print it out
    heat_flux = y0*(excess_temp/x0)**m
    heat_flux = round(heat_flux, 0)
    print(f'The surface heat flux is approximately {int(heat_flux)} W/m^2')

elif 30 <= excess_temp < 120:
    m = (math.log(Dy / Cy)/math.log(Dx / Cx)) #Transition section (use points C and D)
    y0 = Cy
    x0 = Cx

#Step 3 → Calculate the Heat Flux
#I’ll calculate the heat_flux using the corresponding equation and print it out
    heat_flux = y0*(excess_temp/x0)**m
    heat_flux = round(heat_flux, 0)
    print(f'The surface heat flux is approximately {int(heat_flux)} W/m^2')

elif 120 <= excess_temp <= 1200:
    m = (math.log(Ey / Dy)/math.log(Ex / Dx)) #Film sections (use points D and E)
    y0 = Dy
    x0 = Dx 

#Step 3 → Calculate the Heat Flux
#I’ll calculate the heat_flux using the corresponding equation and print it out
    heat_flux = y0*(excess_temp/x0)**m
    heat_flux = round(heat_flux, 0)
    print(f'The surface heat flux is approximately {int(heat_flux)} W/m^2')

#Based off where on the graph I am I will use the corresponding slope and linear interpolation equation to get a y-value on the corresponding line segement

else:
    print("Surface heat flux is not available")