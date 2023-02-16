# Random Walk

# Plot proprotion of returns to origin and limits reached

# Copyright 2023. Moti Ben-Ari
# Creative Commons Attribution-ShareAlike

import configuration as C
import matplotlib.pyplot as plt

# Initialize the graph
def init_graph():
    # Close previous graph
    plt.close()
    # Define the figure size
    plt.figure(figsize=(12, 6))
    # Interactive plot
    if not C.CLOSE:
        plt.ion()
        plt.show()

# Plot the graph
def generate_vlines(title, xlabel, xvalues, yvalues):
    init_graph()
    plt.xlabel(xlabel)
    plt.title(title)
    # Draw lines from zero to yvalues
    plt.vlines(xvalues, [0]*len(yvalues), yvalues)
    finish_graph()

# Display the graph
def finish_graph():
    # Draw the plot
    if not C.CLOSE:
        plt.draw()
        plt.pause(0.001)
    else:
        plt.show()
