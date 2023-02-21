# 2D Random Walk

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
    fig = plt.figure(figsize=(12, 6))
    # Interactive plot
    if not C.CLOSE:
        plt.ion()
        plt.show()
    return fig

# Plot the graphs
def generate_vlines(title1, xlabel, 
                    xvalues, yvalues1, title2, yvalues2):
    fig = init_graph()
    fig.suptitle(C.GRAPH_TITLE)
    # Plot the proportions of returns to the origin
    plt.subplot(1,2,1)
    plt.xlabel(xlabel)
    plt.title(title1)
    # Draw lines from zero to yvalues
    plt.vlines(xvalues, [0]*len(yvalues1), yvalues1)
    # Plot the mean durations
    plt.subplot(1,2,2)
    plt.xlabel(xlabel)
    plt.title(title2)
    plt.vlines(xvalues, [0]*len(yvalues2), yvalues2)
    finish_graph()

# Display the graph
def finish_graph():
    # Draw the plot
    if not C.CLOSE:
        plt.draw()
        plt.pause(0.001)
    else:
        plt.show()
