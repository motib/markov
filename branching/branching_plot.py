# Branching processes

# Plot histogram of populations

# Copyright 2023. Moti Ben-Ari
# Creative Commons Attribution-ShareAlike

import configuration as C
import matplotlib.pyplot as plt
from matplotlib import lines

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
def finish_graph(fig, title):
    fig.suptitle(title, fontsize=16)
    # Label on x-axis
    plt.xlabel('Population')
    # Draw the plot
    if not C.CLOSE:
        plt.draw()
        plt.pause(0.001)
    else:
        plt.show()

# Plot histograms
#   counts: count in each bin
def generate_histogram(counts, exp, mean):
    hist = plt.hist(counts, bins=C.BINS, histtype='step')
    # Plot vertical lines for mean and expecation
    plt.vlines(mean, 0, max(hist[0]), 
               color="red",
               linestyles="dashed",
               label="mean")
    plt.vlines(exp, 0, max(hist[0]), 
               color="blue", 
               linestyles="dashed",
               label="expectation")
    plt.legend()
