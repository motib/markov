# Gambler's ruin

# Plot proprotion of wins and histogram of durations

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
    # Title on figure, not subplots
    fig.suptitle(title, fontsize=16)
    # Label on x-axis and legend
    plt.xlabel('Duration (steps)')
    plt.legend()
    # Draw the plot
    if not C.CLOSE:
        plt.draw()
        plt.pause(0.001)
    else:
        plt.show()

# Plot the proportion of wins as vertical lines
#   x_values: list of probabilities or initial values
#             for the x-coordinate
#   proportion_wins: y-coordinate
#   k: Element of x_values
def plot_wins(x_values, proportion_wins, k, xlabel):
    # Plot on first subplot
    plt.subplot(1,2,1)
    plt.xlabel(xlabel)
    plt.ylabel('Proportion of wins')
    plt.vlines(
        x_values[k], 0, proportion_wins,
        color=C.COLORS[k], linestyles="solid")
    # Return to second subplot for histograms
    plt.subplot(1,2,2)

# Plot histograms
#   counts: count in each bin
def generate_histogram(counts, k, label):
    return plt.hist(counts, bins=C.BINS, color=C.COLORS[k],
                histtype='step', range=(C.MIN_RANGE, C.MAX_RANGE),
                label=label)

# Plot vertical lines for expectations on histograms
#   x: x-coordinate
#   m: height of vertical line
def generate_vline(x, m, k):
    plt.vlines(x, 0, m, color=C.COLORS[k], linestyles="dashed")
