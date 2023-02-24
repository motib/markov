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
import random

# Save parameters between runs
# Initialize with the defaults
a_save, b_save = C.A_DEFAULT, C.B_DEFAULT

# Run the simulation
def step_until_limit(a, b):
    # Current position of the particle
    at_A = True
    # Counts of particle locations
    a_count, b_count = 1, 0

    # Move particles until the limit is reached
    for i in range(C.LIMIT):
        if at_A:
            if random.random() < a_save:
                at_A = not at_A
                b_count += 1
            else:
                a_count += 1
        else:
            if random.random() < b_save:
                at_A = not at_A
                a_count += 1
            else:
                b_count += 1
    display_output(a_save, b_save, a_count, b_count)

# Display output for these parameters and this plot
def display_output(a, b, a_count, b_count):
    # Print parameters
    print("\nProbabilities:  a = {:.3f}, b = {:.3f}".format(a,b))
    print("Theoretical stationary distribution: a = {:.3f}, b = {:.3f}" \
          .format(b/(a+b), a/(a+b)))
    print("Simulation  stationary distribution: a = {:.3f}, b = {:.3f}\n" \
          .format(a_count/C.LIMIT, b_count/C.LIMIT))

# Get new parameters
# Check for validity of type and range
def get_parameters():
    while (True):
        try:
            a = float(input("A to B probability = "))
            if a >= 0.0 and a <= 1.0: break
            else: print("Must be 0.0 <= a <= 1.0")
        except: print("Must be float")
    while (True):
        try:
            b = float(input("B to A probability = "))
            if b >= 0.0 or b <= 1.0: break
            else: print("Must be 0.0 <= b <= 1.0")
        except: print("Must be float")
    return a, b

# Get mode and call simulation
def main():
    global a_save, b_save
    while True:
        r = input(C.PROMPT)
        if   r == 'q': break
        elif r == 'h': input(C.HELP)
        elif r == 's':
            step_until_limit(a_save, b_save)
        elif r == 'n':
            a_save, b_save = get_parameters()
            step_until_limit(a_save, b_save)

if __name__ == '__main__':
    main()
