from dice import Dice

# Create a D6
dice = Dice()

# Make some rolls, and store results in a list
results = []
for roll in range(100):
    result = dice.roll()
    results.append(result)

print(results)