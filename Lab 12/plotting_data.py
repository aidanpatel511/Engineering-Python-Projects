# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Aidan
# Section:      519
# Assignment:   Lab 12 Individual 
# Date:        15 11 2025

import matplotlib.pyplot as plt
import numpy as np

#Line Graph
xi = []
y1 = []
y2 = []
file = open('WeatherDataCLL.csv', 'r')
lines = file.readlines()
for line in lines[1:]:  # Skip header
    data = line.strip().split(',')
    date_parts = data[0].split('/')
    try:
            wet_bulb = float(data[3]) #gets data from file
            pressure = float(data[2]) #same thing
            year = date_parts[2]

            y1.append(wet_bulb)
            y2.append(pressure)
            xi.append(year)

    except (ValueError, IndexError):
        continue
    
x = np.arange(len(xi))
fig, (ax1) = plt.subplots()
ax2 = ax1.twinx()
line1, = ax1.plot(x, y1, color='red', linewidth=2.0, label='Avg Wet Bulb Temp')
line2, = ax2.plot(x, y2, color='blue', linewidth=2.0, label='Avg Pressure')
plt.title('Average Wet Bulb Temperature and Avg Pressure')
ax1.set_xlabel('date')
ax1.set_ylabel('Average Wet Bulb Temperature, F')
ax2.set_ylabel('Average Pressure, in Hg')
lines = [line1, line2]
labels = [line.get_label() for line in lines]
ax1.legend(lines, labels, loc='lower left')
plt.show()
file.close

#Histogram
wind_speeds = []
xi = []
file = open('WeatherDataCLL.csv', 'r')
lines = file.readlines()
for line in lines[1:]:  # Skip header
    data = line.strip().split(',')
    date_parts = data[0].split('/')
    try:
            wind_speed = float(data[4])
            year = date_parts[2]

            wind_speeds.append(wind_speed)
            xi.append(year)

    except (ValueError, IndexError):
        continue
plt.hist(wind_speeds, 29, color='green', edgecolor='black')
plt.title('Histogram of Average Wind Speed')
plt.xlabel('Average Wind Speed, mph')
plt.ylabel('Number of Days')
plt.show()
file.close

#Scatterplot
humidities = []
dews = []
file = open('WeatherDataCLL.csv', 'r')
lines = file.readlines()
for line in lines[1:]:  # Skip header
    data = line.strip().split(',')
    date_parts = data[0].split('/')
    try:
            average_rel_humidity = float(data[-4])
            average_dewpoint = float(data[1])

            # only append if EVERYTHING worked
            humidities.append(average_rel_humidity)
            dews.append(average_dewpoint)
    except (ValueError, IndexError):
        continue
plt.scatter(dews, humidities, color='black', s=10)
plt.title('Average Relative Humidity vs Average Dew Point')
plt.xlabel('Average Dew Point (F)')
plt.ylabel('Average Relative Humidity (%)')
plt.show()
file.close()

#Bar Chart
#First get average temps for each month as bars
Januaryt = []
Februaryt = []
Marcht = []
Aprilt = []
Mayt = []
Junet = []
Julyt = []
Augustt = []
Septembert = []
Octobert = []
Novembert = []
Decembert = []
file = open('WeatherDataCLL.csv', 'r')
lines = file.readlines()
for line in lines[1:]:
    data = line.strip().split(',')
    date_parts = data[0].split('/')
    record_month = int(date_parts[0])
    if record_month == 1:
        try:
            Januaryt.append(float(data[-3]))
        except ValueError:
            continue  # Skip missing values
    elif record_month == 2:
        try:
            Februaryt.append(float(data[-3]))
        except ValueError:
            continue  # Skip missing values
    elif record_month == 3:
        try:
            Marcht.append(float(data[-3]))
        except ValueError:
            continue  # Skip missing values
    elif record_month == 4:
        try:
            Aprilt.append(float(data[-3]))
        except ValueError:
            continue  # Skip missing values
    elif record_month == 5:
        try:
            Mayt.append(float(data[-3]))
        except ValueError:
            continue  # Skip missing values
    elif record_month == 6:
        try:
            Junet.append(float(data[-3]))
        except ValueError:
            continue  # Skip missing values
    elif record_month == 7:
        try:
            Julyt.append(float(data[-3]))
        except ValueError:
            continue  # Skip missing values
    elif record_month == 8:
        try:
            Augustt.append(float(data[-3]))
        except ValueError:
            continue  # Skip missing values
    elif record_month == 9:
        try:
            Septembert.append(float(data[-3]))
        except ValueError:
            continue  # Skip missing values
    elif record_month == 10:
        try:
            Octobert.append(float(data[-3]))
        except ValueError:
            continue  # Skip missing values
    elif record_month == 11:
        try:
            Novembert.append(float(data[-3]))
        except ValueError:
            continue  # Skip missing values
    elif record_month == 12:
        try:
            Decembert.append(float(data[-3]))
        except ValueError:
            continue  # Skip missing values
Januaryt_total = 0
for i in Januaryt:
    Januaryt_total += i
Januaryt_mean = Januaryt_total / len(Januaryt)

# February
Februaryt_total = 0
for i in Februaryt:
    Februaryt_total += i
Februaryt_mean = Februaryt_total / len(Februaryt)

# March
Marcht_total = 0
for i in Marcht:
    Marcht_total += i
Marcht_mean = Marcht_total / len(Marcht)

# April
Aprilt_total = 0
for i in Aprilt:
    Aprilt_total += i
Aprilt_mean = Aprilt_total / len(Aprilt)

# May
Mayt_total = 0
for i in Mayt:
    Mayt_total += i
Mayt_mean = Mayt_total / len(Mayt)

# June
Junet_total = 0
for i in Junet:
    Junet_total += i
Junet_mean = Junet_total / len(Junet)

# July
Julyt_total = 0
for i in Julyt:
    Julyt_total += i
Julyt_mean = Julyt_total / len(Julyt)

# August
Augustt_total = 0
for i in Augustt:
    Augustt_total += i
Augustt_mean = Augustt_total / len(Augustt)

# September
Septembert_total = 0
for i in Septembert:
    Septembert_total += i
Septembert_mean = Septembert_total / len(Septembert)

# October
Octobert_total = 0
for i in Octobert:
    Octobert_total += i
Octobert_mean = Octobert_total / len(Octobert)

# November
Novembert_total = 0
for i in Novembert:
    Novembert_total += i
Novembert_mean = Novembert_total / len(Novembert)

# December
Decembert_total = 0
for i in Decembert:
    Decembert_total += i
Decembert_mean = Decembert_total / len(Decembert)

monthst_mean = []

monthst_mean.append(Januaryt_mean)
monthst_mean.append(Februaryt_mean)
monthst_mean.append(Marcht_mean)
monthst_mean.append(Aprilt_mean)
monthst_mean.append(Mayt_mean)
monthst_mean.append(Junet_mean)
monthst_mean.append(Julyt_mean)
monthst_mean.append(Augustt_mean)
monthst_mean.append(Septembert_mean)
monthst_mean.append(Octobert_mean)
monthst_mean.append(Novembert_mean)
monthst_mean.append(Decembert_mean)
file.close()

#Next get the max of the max temps for each month as a line
JanuaryMt = []
FebruaryMt = []
MarchMt = []
AprilMt = []
MayMt = []
JuneMt = []
JulyMt = []
AugustMt = []
SeptemberMt = []
OctoberMt = []
NovemberMt = []
DecemberMt = []
file = open('WeatherDataCLL.csv', 'r')
lines = file.readlines()
for line in lines[1:]:
    data = line.strip().split(',')
    date_parts = data[0].split('/')
    record_month = int(date_parts[0])
    if record_month == 1:
        try:
            JanuaryMt.append(float(data[-2]))
        except ValueError:
            continue  # Skip missing values
    elif record_month == 2:
        try:
            FebruaryMt.append(float(data[-2]))
        except ValueError:
            continue  # Skip missing values
    elif record_month == 3:
        try:
            MarchMt.append(float(data[-2]))
        except ValueError:
            continue  # Skip missing values
    elif record_month == 4:
        try:
            AprilMt.append(float(data[-2]))
        except ValueError:
            continue  # Skip missing values
    elif record_month == 5:
        try:
            MayMt.append(float(data[-2]))
        except ValueError:
            continue  # Skip missing values
    elif record_month == 6:
        try:
            JuneMt.append(float(data[-2]))
        except ValueError:
            continue  # Skip missing values
    elif record_month == 7:
        try:
            JulyMt.append(float(data[-2]))
        except ValueError:
            continue  # Skip missing values
    elif record_month == 8:
        try:
            AugustMt.append(float(data[-2]))
        except ValueError:
            continue  # Skip missing values
    elif record_month == 9:
        try:
            SeptemberMt.append(float(data[-2]))
        except ValueError:
            continue  # Skip missing values
    elif record_month == 10:
        try:
            OctoberMt.append(float(data[-2]))
        except ValueError:
            continue  # Skip missing values
    elif record_month == 11:
        try:
            NovemberMt.append(float(data[-2]))
        except ValueError:
            continue  # Skip missing values
    elif record_month == 12:
        try:
            DecemberMt.append(float(data[-2]))
        except ValueError:
            continue  # Skip missing values
monthsmaxt = []

monthsmaxt.append(max(JanuaryMt))
monthsmaxt.append(max(FebruaryMt))
monthsmaxt.append(max(MarchMt))
monthsmaxt.append(max(AprilMt))
monthsmaxt.append(max(MayMt))
monthsmaxt.append(max(JuneMt))
monthsmaxt.append(max(JulyMt))
monthsmaxt.append(max(AugustMt))
monthsmaxt.append(max(SeptemberMt))
monthsmaxt.append(max(OctoberMt))
monthsmaxt.append(max(NovemberMt))
monthsmaxt.append(max(DecemberMt))
file.close

#Next get the lowest of the minimum temps for each month
JanuaryLt = []
FebruaryLt = []
MarchLt = []
AprilLt = []
MayLt = []
JuneLt = []
JulyLt = []
AugustLt = []
SeptemberLt = []
OctoberLt = []
NovemberLt = []
DecemberLt = []
file = open('WeatherDataCLL.csv', 'r')
lines = file.readlines()
for line in lines[1:]:
    data = line.strip().split(',')
    date_parts = data[0].split('/')
    record_month = int(date_parts[0])
    if record_month == 1:
        try:
            JanuaryLt.append(float(data[-1]))
        except ValueError:
            continue  # Skip missing values
    elif record_month == 2:
        try:
            FebruaryLt.append(float(data[-1]))
        except ValueError:
            continue  # Skip missing values
    elif record_month == 3:
        try:
            MarchLt.append(float(data[-1]))
        except ValueError:
            continue  # Skip missing values
    elif record_month == 4:
        try:
            AprilLt.append(float(data[-1]))
        except ValueError:
            continue  # Skip missing values
    elif record_month == 5:
        try:
            MayLt.append(float(data[-1]))
        except ValueError:
            continue  # Skip missing values
    elif record_month == 6:
        try:
            JuneLt.append(float(data[-1]))
        except ValueError:
            continue  # Skip missing values
    elif record_month == 7:
        try:
            JulyLt.append(float(data[-1]))
        except ValueError:
            continue  # Skip missing values
    elif record_month == 8:
        try:
            AugustLt.append(float(data[-1]))
        except ValueError:
            continue  # Skip missing values
    elif record_month == 9:
        try:
            SeptemberLt.append(float(data[-1]))
        except ValueError:
            continue  # Skip missing values
    elif record_month == 10:
        try:
            OctoberLt.append(float(data[-1]))
        except ValueError:
            continue  # Skip missing values
    elif record_month == 11:
        try:
            NovemberLt.append(float(data[-1]))
        except ValueError:
            continue  # Skip missing values
    elif record_month == 12:
        try:
            DecemberLt.append(float(data[-1]))
        except ValueError:
            continue  # Skip missing values
monthsmint = []

monthsmint.append(min(JanuaryLt))
monthsmint.append(min(FebruaryLt))
monthsmint.append(min(MarchLt))
monthsmint.append(min(AprilLt))
monthsmint.append(min(MayLt))
monthsmint.append(min(JuneLt))
monthsmint.append(min(JulyLt))
monthsmint.append(min(AugustLt))
monthsmint.append(min(SeptemberLt))
monthsmint.append(min(OctoberLt))
monthsmint.append(min(NovemberLt))
monthsmint.append(min(DecemberLt))
file.close

#Finally get the total average precipitation for each month
JanuaryP = []
FebruaryP = []
MarchP = []
AprilP = []
MayP = []
JuneP = []
JulyP = []
AugustP = []
SeptemberP = []
OctoberP = []
NovemberP = []
DecemberP = []
file = open('WeatherDataCLL.csv', 'r')
lines = file.readlines()
for line in lines[1:]:
    data = line.strip().split(',')
    date_parts = data[0].split('/')
    record_month = int(date_parts[0])
    if record_month == 1:
        try:
            JanuaryP.append(float(data[-5]))
        except ValueError:
            continue  # Skip missing values
    elif record_month == 2:
        try:
            FebruaryP.append(float(data[-5]))
        except ValueError:
            continue  # Skip missing values
    elif record_month == 3:
        try:
            MarchP.append(float(data[-5]))
        except ValueError:
            continue  # Skip missing values
    elif record_month == 4:
        try:
            AprilP.append(float(data[-5]))
        except ValueError:
            continue  # Skip missing values
    elif record_month == 5:
        try:
            MayP.append(float(data[-5]))
        except ValueError:
            continue  # Skip missing values
    elif record_month == 6:
        try:
            JuneP.append(float(data[-5]))
        except ValueError:
            continue  # Skip missing values
    elif record_month == 7:
        try:
            JulyP.append(float(data[-5]))
        except ValueError:
            continue  # Skip missing values
    elif record_month == 8:
        try:
            AugustP.append(float(data[-5]))
        except ValueError:
            continue  # Skip missing values
    elif record_month == 9:
        try:
            SeptemberP.append(float(data[-5]))
        except ValueError:
            continue  # Skip missing values
    elif record_month == 10:
        try:
            OctoberP.append(float(data[-5]))
        except ValueError:
            continue  # Skip missing values
    elif record_month == 11:
        try:
            NovemberP.append(float(data[-5]))
        except ValueError:
            continue  # Skip missing values
    elif record_month == 12:
        try:
            DecemberP.append(float(data[-5]))
        except ValueError:
            continue  # Skip missing values

# January
JanuaryP_total = 0
for i in JanuaryP:
    JanuaryP_total += i
JanuaryP_mean = JanuaryP_total / len(JanuaryP)

# February
FebruaryP_total = 0
for i in FebruaryP:
    FebruaryP_total += i
FebruaryP_mean = FebruaryP_total / len(FebruaryP)

# March
MarchP_total = 0
for i in MarchP:
    MarchP_total += i
MarchP_mean = MarchP_total / len(MarchP)

# April
AprilP_total = 0
for i in AprilP:
    AprilP_total += i
AprilP_mean = AprilP_total / len(AprilP)

# May
MayP_total = 0
for i in MayP:
    MayP_total += i
MayP_mean = MayP_total / len(MayP)

# June
JuneP_total = 0
for i in JuneP:
    JuneP_total += i
JuneP_mean = JuneP_total / len(JuneP)

# July
JulyP_total = 0
for i in JulyP:
    JulyP_total += i
JulyP_mean = JulyP_total / len(JulyP)

# August
AugustP_total = 0
for i in AugustP:
    AugustP_total += i
AugustP_mean = AugustP_total / len(AugustP)

# September
SeptemberP_total = 0
for i in SeptemberP:
    SeptemberP_total += i
SeptemberP_mean = SeptemberP_total / len(SeptemberP)

# October
OctoberP_total = 0
for i in OctoberP:
    OctoberP_total += i
OctoberP_mean = OctoberP_total / len(OctoberP)

# November
NovemberP_total = 0
for i in NovemberP:
    NovemberP_total += i
NovemberP_mean = NovemberP_total / len(NovemberP)

# December
DecemberP_total = 0
for i in DecemberP:
    DecemberP_total += i
DecemberP_mean = DecemberP_total / len(DecemberP)

monthsP = []

monthsP = []

monthsP.append(JanuaryP_total / 12)
monthsP.append(FebruaryP_total / 12)
monthsP.append(MarchP_total / 12)
monthsP.append(AprilP_total / 12)
monthsP.append(MayP_total / 12)
monthsP.append(JuneP_total / 12)
monthsP.append(JulyP_total / 12)
monthsP.append(AugustP_total / 12)
monthsP.append(SeptemberP_total / 12)
monthsP.append(OctoberP_total / 12)
monthsP.append(NovemberP_total / 12)
monthsP.append(DecemberP_total / 12)

file.close

#plotting
months = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']

fig, ax1 = plt.subplots()
ax1.bar(months, monthst_mean, color='yellow')
ax1.plot(months, monthsmaxt, color='red', label='High T')
ax1.plot(months, monthsmint, color='blue', label='Low T')
ax1.plot(months, monthsP, color='cyan', label='Precip')
plt.title('Temperature and Precipitation by Month')
plt.xlabel('Month')
plt.ylabel('Average Temperature, F \nMonthly Precipitation, in')
ax1.legend(loc='upper left')
ax1.set_ylim(0, 120)
plt.show()