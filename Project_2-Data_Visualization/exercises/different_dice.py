from dice import Dice
import pygal

# Create D6 and D10
die_1 = Dice()
die_2 = Dice(10)

# Number of rolls
number_rolls = 50000

# Make some rolls, and store results in a list
results = []
for roll in range(number_rolls):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# analyze the results
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results
hist = pygal.Bar()

hist.title = 'Results of rolling a D6 and a D10 50000 times.'
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']
hist._x_title = 'Result'
hist._y_title = 'Frequency of Result'

hist.add('D6 + D10', frequencies)
hist.render_to_file('./Project_2-Data_Visualization/exercises/different_dice.svg')