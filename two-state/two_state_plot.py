# Two-state

# Copyright 2023. Moti Ben-Ari
# Creative Commons Attribution-ShareAlike

import configuration as C
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
#   yvalues1: probabilities
#   yvalues2: proportions
def generate_vlines(a_save, yvalues1, yvalues2):
    n = len(yvalues1)
    fig, ax = init_graph()

    # Set graph properties
    plt.xlabel("Probability b")
    plt.ylabel("Stationary distribution")
    plt.title("Stationary distribution for a = {:.3f}".format(a_save))
    ax.set_xticks([i*.1 for i in range(0, n, 2)])

    # x-values are number of votes for B
    # proportion values are slightly offset for visibilty
    xvalues1 = [i*0.1 for i in range(n)]
    xvalues2 = [i*0.1+0.005 for i in range(n)]
    # Draw lines from 0 to proportion
    plt.vlines(xvalues1, [0]*len(yvalues1), yvalues1,
               colors="blue", label="A")
    plt.vlines(xvalues2, [0]*len(yvalues2), yvalues2,
               colors="red", label="B")

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
