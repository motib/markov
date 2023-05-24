# Multiple gamblers

# Copyright 2023. Moti Ben-Ari
# Creative Commons Attribution-ShareAlike

import configuration as C
import math
import matplotlib.pyplot as plt

# Initialize the graph
def init_graph():
    # Close previous graph
    plt.close()
    # Define the figure size
    fig, ax = plt.subplots(figsize=(12, 6))
    # Interactive plot
    if not C.CLOSE:
        plt.ion()
        plt.show()
    return fig, ax

# Plot the graphs
#   xlabel: "Gambler" or "Total capital"
#   a_save: total number of gamblers or total captial
#   yvalues1: averages
#   yvalues2: expectations
def generate_vlines(xlabel, a_save, yvalues1, yvalues2):
    n = len(yvalues1)
    fig, ax = init_graph()

    # Set labels
    plt.xlabel(xlabel)
    plt.ylabel("Steps")
    plt.title("Averages and expectations for multiple " + \
              xlabel.lower())

    # Set x-axis ticks and values
    # Expectations are slightly offset
    xvalues1 = [math.floor(x*a_save) for x in C.PERCENTAGES]
    xvalues2 = [x+(0.01*a_save) for x in xvalues1]
    ax.set_xticks(xvalues1)

    # Draw lines from 0 
    plt.vlines(xvalues1, [0]*len(yvalues1), yvalues1,
               colors="blue", label="Average")
    plt.vlines(xvalues2, [0]*len(yvalues2), yvalues2,
               colors="red", label="Expectation")

    finish_graph()

# Display the graph
def finish_graph():
    plt.legend()
    # Draw the plot
    if not C.CLOSE:
        plt.draw()
        plt.pause(0.001)
    else:
        plt.show()
