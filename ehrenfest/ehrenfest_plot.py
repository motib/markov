# Ehrenfest model

# Plot stationary distribution

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
#   yvalues1: theoretical distribution
#   yvalues2: simulation distribution
def generate_vlines(n, yvalues1, yvalues2):
    init_graph()
    plt.xlabel("Particles in left urn")
    plt.ylabel("Probability and proportion")
    plt.title("Ehrenfest model for {:d} urns".format(n))
    # x-values are each number of particles
    # simulation values are slightly offset for visibilty
    xvalues1 = [i for i in range(0,n+1)]
    xvalues2 = [i+0.1 for i in range(0,n+1)]
    # Draw lines from 0 to proportion
    plt.vlines(xvalues1, [0]*len(yvalues1), yvalues1,
               colors="blue", label="Theory")
    plt.vlines(xvalues2, [0]*len(yvalues2), yvalues2,
               colors="red", label="Simulation")
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
