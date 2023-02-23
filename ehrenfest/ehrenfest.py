# Ehrenfest model
# Compute and simulate stationary distribution

# Parameters are:
#   n: total particles in both urns

# Output and graph:
#   theoretical distribution
#   simulation distribution

# Copyright 2023. Moti Ben-Ari
# Creative Commons Attribution-ShareAlike

import configuration as C
import ehrenfest_plot as gp
import random
import numpy as np
import math

# Save parameters between runs
# Initialize with the defaults
n_save = C.N_DEFAULT

# Run the simulation
def step_until_limit(n):
    # left is the number of paricles in the left urn
    #   the stationary distribution is independent of the
    #   initial value so arbitrarily choose the middle
    left = n // 2

    # Counts of contents of left urn in the each state
    left_counts = np.zeros(n+1, dtype=int)

    # Move particles until the limit is reached
    for i in range(C.LIMIT):
        left_counts[left] += 1
        # At zero only go right
        if left == 0:
            left  += 1
        # At end only go left
        elif left == n:            
            left  -= 1
        # Otherwise randomly
        elif random.random() > left / n:
            left  += 1
        else:
            left  -= 1
    display_output(n, left_counts)

# Display output for these parameters and this plot
def display_output(n, left_counts):
    # Print parameters
    print("\nTotal particles in urns = {:d}".format(n))

    print("Theoretical stationary distribution")
    np.set_printoptions(precision=3)
    theory = theoretical_distribution(n_save)
    print(theory)

    print("Simulation stationary distribution")
    sim = left_counts / C.LIMIT
    print(sim)

    gp.generate_vlines(n, theory, sim)

# Compute theoretical distribution
def theoretical_distribution(n):
    # From 0 to n (inclusive!)
    return np.array([(math.comb(n,i)/2**n) for i in range(n+1)])

# Get new parameters
# Check for validity of type and range
def get_parameters():
    while (True):
        try:
            n = int(input("Total particles in urns = "))
            if n >= 1: break
            else: print("Must be n >= 1")
        except: print("Must be integer")
    return n

# Get mode and call simulations, then plot
def main():
    global n_save
    while True:
        r = input(C.PROMPT)
        if   r == 'q': break
        elif r == 'h': input(C.HELP)
        elif r == 's':
            step_until_limit(n_save)
        elif r == 'n':
            n_save = get_parameters()
            step_until_limit(n_save)

if __name__ == '__main__':
    main()
