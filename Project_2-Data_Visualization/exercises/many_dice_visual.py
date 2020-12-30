from dice import Dice
import pygal

# Create two D6 dice
dice1 = Dice()
dice2 = Dice()
number_rolls = 1000

# Make some rolls, and store results in a list
results = []
for roll in range(number_rolls):
    result = dice1.roll() + dice2.roll()
    results.append(result)

# analyze the results
frequencies = []
max_result = dice1.num_sides + dice2.num_sides
for value in range(2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results
hist = pygal.Bar()

hist.title = 'Results of rolling two D6 1000 times.'
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
hist._x_title = 'Result'
hist._y_title = 'Frequency of Result'

hist.add('D6 + D6', frequencies)
hist.render_to_file('./Project_2-Data_Visualization/exercises/many_dice_visual.svg')