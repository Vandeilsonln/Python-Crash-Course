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
filename = 'death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    dates, highs, lows = [], [], []
    for row in reader:
        try:
            
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            highFarenheit = int(row[1])
            lowFahrenheit = int(row[3])
            
        except ValueError:
            print(current_date, 'missing data')
        
        else:
            dates.append(current_date)

            highCelsius = convertTemperature(highFarenheit)
            highs.append(highCelsius)

            lowCelsius = convertTemperature(lowFahrenheit)
            lows.append(lowCelsius)


# Plot data
fig = plt.figure(dpi=128, figsize=(9, 6))
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format plot
plt.title('Daily high and low temperatures - 2014\nDeath Valley, CA', fontsize=20)
plt.xlabel('', fontsize=12)
fig.autofmt_xdate()
plt.ylabel('Temperature (F)', fontsize=12)
plt.tick_params(axis='both', which='major', labelsize=12)

plt.show()
