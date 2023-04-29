# Branching process - extinction

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
def generate_vlines(p_values, yvalues1, yvalues2):
    n = len(yvalues1)
    fig, ax = init_graph()

    # Set graph properties
    plt.xlabel("P(Y_1=2 | X_1=1)")
    plt.ylabel("Probability and proportion")
    plt.title("Probability and proportion of extinction")
    ax.set_xticks(p_values)

    # x-values are probabilities of P(Y_1=2 | X_1=1)
    # proportion values are slightly offset for visibilty
    xvalues1 = p_values
    xvalues2 = [p+0.005 for p in p_values]
    # Draw lines from 0 to proportion
    plt.vlines(xvalues1, [0]*len(yvalues1), yvalues1,
               colors="blue", label="Probability")
    plt.vlines(xvalues2, [0]*len(yvalues2), yvalues2,
               colors="red", label="Proportion")

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
