from dice import Dice
import pygal

# Create a D6
dice = Dice()
number_rolls = 10000

# Make some rolls, and store results in a list
results = []
for roll in range(number_rolls):
    result = dice.roll()
    results.append(result)

# analyze the results
frequencies = []
for value in range(1, dice.num_sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results
hist = pygal.Bar()

hist.title = 'Results of rolling one D6 1000 times.'
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist._x_title = 'Result'
hist._y_title = 'Frequency of Result'

hist.add('D6', frequencies)
hist.render_to_file('./Project_2-Data_Visualization/exercises/dice_visual.svg')