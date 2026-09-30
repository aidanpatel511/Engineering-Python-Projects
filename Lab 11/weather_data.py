# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Aidan
# Section:      519
# Assignment:   Lab 11 Individual 
# Date:        7 11 2025

max_temp = -1000
min_temp = 1000

with open('WeatherDataCLL.csv', 'r') as file:
    lines = file.readlines()
    for line in lines[1:]:  # Skip header
        data = line.strip().split(',')
        try:
            max_val = float(data[-2])  # Convert string to float
            min_val = float(data[-1])
        except ValueError:
            continue  # Skip rows with missing values

        if max_val > max_temp:
            max_temp = max_val
        if min_val < min_temp:
            min_temp = min_val

print(f"10-year maximum temperature: {int(max_temp)} F")
print(f"10-year minimum temperature: {int(min_temp)} F")

file.close()

month = input("Please enter a month: ")
year = int(input("Please enter a year: "))

months = {"January": 1,"February": 2,"March": 3,"April": 4,"May": 5,"June": 6,"July": 7,"August": 8,"September": 9,"October": 10,"November": 11,"December": 12}

target_month = months[month]

total_pressure = 0
count = 0

with open('WeatherDataCLL.csv', 'r') as file:
    lines = file.readlines()
    for line in lines[1:]:
        data = line.strip().split(',')
        date_parts = data[0].split('/')
        record_month = int(date_parts[0])
        record_year = int(date_parts[2])
        if record_month == target_month and record_year == year:
            try:
                avg_pressure = float(data[2])
                total_pressure += avg_pressure
                count += 1
            except ValueError:
                continue  # Skip missing values

mean_pressure = total_pressure / count
# print(f"Mean average daily pressure: {mean_pressure:.2f} in Hg") --> Works (tested, will print later)
file.close()

total_temperature = 0
count = 0

with open('WeatherDataCLL.csv', 'r') as file:
    lines = file.readlines()
    for line in lines[1:]:
        data = line.strip().split(',')
        date_parts = data[0].split('/')
        record_month = int(date_parts[0])
        record_year = int(date_parts[2])
        if record_month == target_month and record_year == year:
            try:
                avg_temperature = float(data[-3])
                total_temperature += avg_temperature
                count += 1
            except ValueError:
                continue  # Skip missing values
mean_temperature = total_temperature / count
file.close()

total_wet_bulb_temp = 0
count = 0

with open('WeatherDataCLL.csv', 'r') as file:
    lines = file.readlines()
    for line in lines[1:]:
        data = line.strip().split(',')
        date_parts = data[0].split('/')
        record_month = int(date_parts[0])
        record_year = int(date_parts[2])
        if record_month == target_month and record_year == year:
            try:
                avg_wet_bulb_temp = float(data[3])
                total_wet_bulb_temp += avg_wet_bulb_temp
                count += 1
            except ValueError:
                continue  # Skip missing values
mean_wet_bulb_temp = total_wet_bulb_temp / count
file.close()

total_average_dew_point = 0
count = 0

with open('WeatherDataCLL.csv', 'r') as file:
    lines = file.readlines()
    for line in lines[1:]:
        data = line.strip().split(',')
        date_parts = data[0].split('/')
        record_month = int(date_parts[0])
        record_year = int(date_parts[2])
        if record_month == target_month and record_year == year:
            try:
                avg_dew_point = float(data[1])
                total_average_dew_point += avg_dew_point
                count += 1
            except ValueError:
                continue  # Skip missing values
mean_dew_point = total_average_dew_point / count
file.close()

total_average_relative_humidity = 0
count = 0

with open('WeatherDataCLL.csv', 'r') as file:
    lines = file.readlines()
    for line in lines[1:]:
        data = line.strip().split(',')
        date_parts = data[0].split('/')
        record_month = int(date_parts[0])
        record_year = int(date_parts[2])
        if record_month == target_month and record_year == year:
            try:
                avg_relative_humidity = float(data[-4])
                total_average_relative_humidity += avg_relative_humidity
                count += 1
            except ValueError:
                continue  # Skip missing values
mean_relative_humidity = total_average_relative_humidity / count
file.close()

total_average_windspeed = 0
count = 0

with open('WeatherDataCLL.csv', 'r') as file:
    lines = file.readlines()
    for line in lines[1:]:
        data = line.strip().split(',')
        date_parts = data[0].split('/')
        record_month = int(date_parts[0])
        record_year = int(date_parts[2])
        if record_month == target_month and record_year == year:
            try:
                avg_windspeed = float(data[4])
                total_average_windspeed += avg_windspeed
                count += 1
            except ValueError:
                continue  # Skip missing values
mean_windspeed = total_average_windspeed / count
file.close()

total_days_with_precipitation = 0
count = 0
with open('WeatherDataCLL.csv', 'r') as file:
    lines = file.readlines()
    for line in lines[1:]:
        data = line.strip().split(',')
        date_parts = data[0].split('/')
        record_month = int(date_parts[0])
        record_year = int(date_parts[2])
        if record_month == target_month and record_year == year:
            try:
                precipitation = float(data[5])
                if precipitation > 0:
                    total_days_with_precipitation += 1
                count += 1
            except ValueError:
                continue  # Skip missing values
percent_days_with_precipitation = total_days_with_precipitation / count * 100
file.close()

print(f'For {month} {year}:')
print(f"Mean average daily pressure: {mean_pressure:.2f} in Hg")
print(f"Mean average daily temperature: {mean_temperature:.1f} F")
print(f"Mean average daily wet bulb temperature: {mean_wet_bulb_temp:.1f} F")
print(f"Mean average daily dew point: {mean_dew_point:.1f} F")
print(f"Mean average daily relative humidity: {mean_relative_humidity:.1f}%")
print(f"Mean average daily wind speed: {mean_windspeed:.2f} mph")
print(f"Percentage of days with precipitation: {percent_days_with_precipitation:.1f}%")