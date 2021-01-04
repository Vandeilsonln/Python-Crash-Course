import csv
from os import chdir
from matplotlib import pyplot as plt
from datetime import datetime

# Set up Current Working Directiory
chdir('./Project_2-Data_Visualization/exercises')

# Convert temperature to Celsius
def convertTemperature(degrees):
    return int(round((degrees - 32) * 5 / 9, 0))

# Get dates, high and low temperatures from file.
filename = 'sitka_weather_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[0], "%Y-%m-%d")
        dates.append(current_date)

        highFarenheit = int(row[1])
        highCelsius = convertTemperature(highFarenheit)
        highs.append(highCelsius)

        lowFahrenheit = int(row[3])
        lowCelsius = convertTemperature(lowFahrenheit)
        lows.append(lowCelsius)

# Plot data
fig = plt.figure(dpi=128, figsize=(9, 5))
plt.plot(dates, highs, c='red')
plt.plot(dates, lows, c='blue')

# Format plot
plt.title('Daily high and low temperatures - 2014', fontsize=20)
plt.xlabel('', fontsize=12)
fig.autofmt_xdate()
plt.ylabel('Temperature (F)', fontsize=12)
plt.tick_params(axis='both', which='major', labelsize=12)

plt.show()
