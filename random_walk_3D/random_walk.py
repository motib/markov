# 3D Random Walk

# Simulation of three-dimensional random walk

# Copyright 2023. Moti Ben-Ari
# Creative Commons Attribution-ShareAlike

import configuration as C
import random_walk_plot as rp
import random
import numpy as np

# Array of number of steps
step_counts = np.zeros(C.SIMS, dtype=int)

# Save the last limit
lim_save = C.LIMIT_DEFAULT

# Run the simulations
def step_until_return_to_origin(lim):
    # Count returns to the origin and
    #   simulations that exceeded the limit
    origins, limits = 0, 0

    for j in range(C.SIMS):
        # Initialize the first step
        steps = 1
        current_x = 1 if random.random() < C.p else -1
        current_y = 1 if random.random() < C.p else -1
        current_z = 1 if random.random() < C.p else -1
    
        # Move until reached zero or limit
        while current_x != 0 or current_y != 0 or current_z != 0:
            current_x += 1 if random.random() < C.p else -1
            current_y += 1 if random.random() < C.p else -1
            current_z += 1 if random.random() < C.p else -1
            steps += 1
            if steps > lim : break

        # Count wins and losses
        if current_x == 0 and current_y == 0 and current_z == 0:
            origins += 1
        else: limits += 1
        step_counts[j] = steps

    display_output(lim, origins, limits)
    return origins, limits

# Display output for these parameters and this plot
def display_output(lim, origins, limits):
    print("\nLimit                            = {:d}".
          format(lim))
    print("Proportion returning to origin   = {:.3f}".
          format(origins / C.SIMS))
    print("Proportion reaching limit        = {:.3f}".
          format(limits / C.SIMS))
    print("Mean duration (steps)            = {:d}".
          format(round(np.mean(step_counts[0:C.SIMS]))))

# Get new parameter
# Check for validity of type and range
def get_parameters():
    while (True):
        try:
            lim = int(input("Limit of steps for a simulation  = "))
            if 0 < lim: break
            else: print("Must be 0 < limit")
        except: print("Must be integer")
    return lim

# Get mode and call simulations
def main():
    global lim_save

    while True:
        r = input(C.PROMPT)

        if   r == 'q': break
        elif r == 'h': input(C.HELP)
        elif r == 's':
            step_until_return_to_origin(lim_save)

        elif r == 'n':
            lim_save = get_parameters()
            step_until_return_to_origin(lim_save)
        
        # Multiple limits, loop over tuple in configuration
        # The tuple is of fractions of the limit parameter
        elif r == 'l':
            # Store counts of limits exceeded and durations
            #   for each set of simulations
            limits = []
            durations = []
            # Run the simulations and append results
            for k in C.LIMITS:
                limits.append(step_until_return_to_origin(
                              round(k*lim_save))[1] / C.SIMS)
                durations.append(round(np.mean(step_counts[0:C.SIMS])))
            # Plot the graph of the limits reached and durations
            rp.generate_vlines("Proportion reaching limit = {:d}".format(lim_save),
                               "Limits", C.LIMITS, limits,
                               "Mean duration (steps)", durations)

if __name__ == '__main__':
    main()
