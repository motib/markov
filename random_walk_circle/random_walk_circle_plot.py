# Random walk circle

# Plot histogram of steps until all points are visited

# Copyright 2023. Moti Ben-Ari
# Creative Commons Attribution-ShareAlike

import configuration as C
import matplotlib.pyplot as plt

# Initialize the graph
def init_graph():
    # Close previous graph
    plt.close()
    # Define the figure size
    fig = plt.figure(figsize=(12, 6))
    # Interactive plot
    if not C.CLOSE:
        plt.ion()
        plt.show()
    return fig

# Display the graph
def finish_graph(fig):
    fig.suptitle('Histogram of a random walk on a circle', fontsize=16)
    plt.xlabel('Steps until all points visited')
    # Draw the plot
    if not C.CLOSE:
        plt.draw()
        plt.pause(0.001)
    else:
        plt.show()

# Plot histograms
#   counts: count in each bin
def generate_histogram(counts):
    return plt.hist(counts, bins=C.BINS, histtype='step',
                    range=(C.MIN_RANGE, C.MAX_RANGE))
