# Random Walk

# Simulation of one-dimensional random walk

# Copyright 2023. Moti Ben-Ari
# Creative Commons Attribution-ShareAlike

import configuration as C
import random_walk_plot as rp
import random
import numpy as np

# Array of number of steps
step_counts = np.zeros(C.SIMS, dtype=int)

# Save the last probability and limit
p_save, lim_save = C.P_DEFAULT, C.LIM_DEFAULT

# Run the simulations
def step_until_return_to_origin(p, lim):
    # Count returns to the origin and
    #   simulations that exceeded the limit
    origins, limits = 0, 0

    for j in range(C.SIMS):
        # By symmetry initialize the first step to the right
        steps = 1
        current = 1

        # Move until reached zero or limit
        while current != 0:
            if random.random() < p: current += 1
            else:                   current -= 1
            steps += 1
            if steps > lim : break

        # Count wins and losses
        if    current == 0: origins += 1
        else:               limits += 1
        step_counts[j] = steps

    display_output(p, lim, origins, limits)
    return origins, limits

# Display output for these parameters and this plot
def display_output(p, lim, origins, limits):
    print("\nProbability = {:.2f}, step limit   = {:d}".
          format(p, lim))
    print("Proportion returning to origin   = {:.3f}".
          format(origins / C.SIMS))
    print("Probability of return to origin  = {:.3f}".
          format(1.0 if p<= 1/2 else (1.0-p)/p))
    print("Proportion reaching limit        = {:.3f}".
          format(limits / C.SIMS))
    print("Mean duration (steps)            = {:d}".
          format(round(np.mean(step_counts[0:C.SIMS]))))
    if p >= 0.5:
        print("Expected duration (steps)        = infinity\n")
    else: 
        print("Expected duration (steps)        = {:d}\n".
            format(round(1.0 / ((1.0-p)-p))))

# Get new parameters
# Check for validity of type and range
def get_parameters():
    while (True):
        try:
            p = float(input("Probability of step to the right = "))
            if p >= 0.0 and p <= 1.0: break
            else: print("Must be 0.0 <= p <= 1.0")
        except: print("Must be real number")

    while (True):
        try:
            lim = int(input("Limit of steps for a simulation  = "))
            if 0 < lim: break
            else: print("Must be 0 < limit")
        except: print("Must be integer")
    return p, lim

# Get mode and call simulations
def main():
    global p_save, lim_save

    while True:
        r = input(C.PROMPT)

        if   r == 'q': break
        elif r == 'h': input(C.HELP)
        elif r == 's':
            step_until_return_to_origin(p_save, lim_save)

        elif r == 'n':
            p_save, lim_save = get_parameters()
            step_until_return_to_origin(p_save, lim_save)
        
        # Multiple probabilities, loop over tuple in configuration
        elif r == 'p':
            # Store counts of returns to origin and durations
            #   for each set of simulations
            origins = []
            durations = []
            # Run the simulations and append results
            for k in C.PROBABILITIES:
                origins.append(step_until_return_to_origin(
                               k, lim_save)[0] / C.SIMS)
                durations.append(round(np.mean(step_counts[0:C.SIMS])))
            # Plot the graph of returns to origin and durations
            rp.generate_vlines("Proportion returning to origin",
                               "Probability", C.PROBABILITIES, origins,
                               "Mean duration (steps)", durations)

        # Multiple limits, loop over tuple in configuration
        # The tuple is of fractions of the total capital
        elif r == 'l':
            # Store counts of limits exceeded and durations
            #   for each set of simulations
            limits = []
            durations = []
            # Run the simulations and append results
            for k in C.LIMITS:
                limits.append(step_until_return_to_origin(
                              p_save, round(k*C.SIMS))[1] / C.SIMS)
                durations.append(round(np.mean(step_counts[0:C.SIMS])))
            # Plot the graph of the limits reached and durations
            rp.generate_vlines("Proportion reaching limit" + \
                               " for probability {:.3f}".format(p_save),
                               "Limits", C.LIMITS, limits,
                               "Mean duration (steps)", durations)

if __name__ == '__main__':
    main()
