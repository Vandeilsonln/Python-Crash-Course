from dice import Dice
import pygal

# Create a D6
dice = Dice()
number_rolls = 1000

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

print(frequencies)