# Two-state Markov chain
# Compute and simulate stationary distribution

# Parameters are:
#   transition probabilities A->B and B->A

# Output:
#   theoretical distribution
#   simulation distribution

# Copyright 2023. Moti Ben-Ari
# Creative Commons Attribution-ShareAlike

import configuration as C
import two_state_plot as tp
import random

# Save parameters between runs
# Initialize with the defaults
a_save, b_save = C.A_DEFAULT, C.B_DEFAULT
# For requesting a given proportion of B's
proportion = 0.0

# Run the simulation
def step_until_limit(a, b):
    # Current position of the particle
    # Result does not depend on the initial position
    at_A = True
    # Counts of particle locations
    a_count, b_count = 0, 1

    # Move particles until the limit is reached
    for i in range(C.LIMIT):
        if at_A:
            if random.random() < a:
                at_A = not at_A
                b_count += 1
            else:
                a_count += 1
        else:
            if random.random() < b:
                at_A = not at_A
                a_count += 1
            else:
                b_count += 1
    display_output(a, b, a_count, b_count)
    return a_count, b_count

# Display output for these parameters and this plot
def display_output(a, b, a_count, b_count):
    global proportion
    # Print parameters
    parameters = "\nProbabilities:  a = {:.3f}, b = {:.3f}".format(a,b)
    if proportion > 0.0:
        parameters += ", p = {:.3f}".format(proportion)
    print(parameters)
    print("Theoretical stationary distribution: A = {:.3f}, B = {:.3f}" \
          .format(b/(a+b), a/(a+b)))
    print("Simulation  stationary distribution: A = {:.3f}, B = {:.3f}\n" \
          .format(a_count/C.LIMIT, b_count/C.LIMIT))

# Get new parameters
# Check for validity of type and range
def get_parameters(r):
    while (True):
        try:
            a = float(input("A to B probability = "))
            if a >= 0.0 and a <= 1.0: break
            else: print("Must be 0.0 <= a <= 1.0")
        except: print("Must be float")
    if r == 'm':
        b = 0  # Not used
    else:
        while (True):
            try:
                b = float(input("B to A probability = "))
                if b >= 0.0 or b <= 1.0: break
                else: print("Must be 0.0 <= b <= 1.0")
            except: print("Must be float")
    return a, b, 0.0

# Enter a proportion p of visits to B
#   and a probability 0 < a < p,
#   compute the value of b
def get_proportion():
    while (True):
        try:
            p = float(input("Proportion of B's = "))
            if p > 0.0 and p < 1.0: break
            else: print("Must be 0.0 < p < 1.0")
        except: print("Must be float")
    while (True):
        try:
            a = float(input("A to B probability = "))
            if a > 0.0 and a < p: break
            else: print("Must be 0.0 < a < p")
        except: print("Must be float")
    b = a * (1-p)/p
    return a, b, p

# Get mode and call simulation
def main():
    global a_save, b_save, proportion
    while True:
        r = input(C.PROMPT)
        if   r == 'q': break
        elif r == 'h': input(C.HELP)
        elif r == 's':
            step_until_limit(a_save, b_save)
        elif r == 'n':
            a_save, b_save, proportion = get_parameters(r)
            step_until_limit(a_save, b_save)
        elif r == 'm':
            a_save, b_save, proportion = get_parameters(r)
            a_dist = []
            b_dist = []
            for b in range(1, 10):
                a_count, b_count = step_until_limit(a_save, b*0.1)
                a_dist.append(a_count/C.LIMIT)
                b_dist.append(b_count/C.LIMIT)
            tp.generate_vlines(a_save, a_dist, b_dist)
        elif r == 'p':
            a_save, b_save, proportion = get_proportion()
            step_until_limit(a_save, b_save)

if __name__ == '__main__':
    main()
