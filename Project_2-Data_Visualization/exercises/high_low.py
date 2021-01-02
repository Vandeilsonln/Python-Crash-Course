import csv
from os import chdir
from matplotlib import pyplot as plt

# Set up Current Working Directiory
chdir('./Project_2-Data_Visualization/exercises')

# Convert temperature to Celsius
def convertTemperature(degrees):
    return int(round((degrees - 32) * 5 / 9, 0))

# Get high temperatures from file.
filename = 'sitka_weather_07-2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    highs = []
    for row in reader:
        highFarenheit = int(row[1])
        highCelsius = convertTemperature(highFarenheit)
        highs.append(highCelsius)

# Plot data
fig = plt.figure(dpi=128, figsize=(9, 6))
plt.plot(highs, c='red')

# Format plot
plt.title('Daily high temperatures, July 2014', fontsize=24)
plt.xlabel('', fontsize=16)
plt.ylabel('Temperature (F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
