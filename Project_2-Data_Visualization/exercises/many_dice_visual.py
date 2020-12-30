from dice import Dice
import pygal
from functools import reduce
# Create two D6 dice
number_dice = 100

# Number of rolls
number_rolls = 10000

# list of dice
my_dice = []
for i in range(number_dice):
    my_dice.append(Dice())

# Make some rolls, and store results in a list
results = []
for roll in range(number_rolls):
    result = 0
    for i in my_dice:
        result += i.roll()
    results.append(result)

# analyze the results
frequencies = []
max_result = number_dice * 6
for value in range(number_dice, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results
hist = pygal.Bar()

hist.title = f'Results of rolling two D6 {number_rolls} times.'
hist.x_labels = [str(i) for i in range(number_dice, max_result)]
#hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
hist._x_title = 'Result'
hist._y_title = 'Frequency of Result'

hist.add('D6 + D6', frequencies)
hist.render_to_file('./Project_2-Data_Visualization/exercises/100_dice_visual.svg')