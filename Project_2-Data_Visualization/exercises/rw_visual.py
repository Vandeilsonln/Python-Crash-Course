import matplotlib.pyplot as plt
from random_walk import RandomWalk

# Keep making new walks, as long as the progrm is active.
while True:
    # Make a random walk, and plot the points.
    rw = RandomWalk(10000)
    rw.fill_walk()

    # Set the size of the plotting window
    plt.figure(figsize=(10, 6))

    point_numbers = list(range(0, rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Wistia, edgecolor='none', s=2)

    # Emphasize the first and last points
    plt.scatter(0, 0, c='green', edgecolors='none', s=20)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=20)

    # remove the axis
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()

    keep_running = input('Make another walk? (y/n): ')
    if keep_running == 'n':
        break
