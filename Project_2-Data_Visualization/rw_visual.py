import matplotlib.pyplot as plt
from random_walk import RandomWalk

# Keep making new walks, as long as the progrm is active.
while True:
    # Make a random walk, and plot the points.
    rw = RandomWalk(10000)
    rw.fill_walk()

    plt.scatter(rw.x_values, rw.y_values, s=1)
    plt.show()

    keep_running = input('Make another walk? (y/n): ')
    if keep_running == 'n':
        break
