# Random Walk

# Simulation of one-dimensional random walk

# Copyright 2023. Moti Ben-Ari
# Creative Commons Attribution-ShareAlike

import configuration as C
import random_walk_plot as rp
import random

# Save the last probability and limit
p_save, lim_save = C.P_DEFAULT, C.LIM_DEFAULT

# Run the simulations
def step_until_return_to_origin(p, lim):
    # Count returns to the origin and
    #   simulations that exceeded the limit
    origins, limits = 0, 0

    for j in range(C.SIMS):
        # Initialize with the first step
        steps = 1
        (current := 1) if random.random() < p else (current := -1)

        # Move until reached zero
        while current != 0:
            if random.random() < p: current += 1
            else:                   current -= 1
            steps += 1
            if steps > lim : break

        # Count wins and losses
        if    current == 0: origins += 1
        else:               limits += 1
    
    display_output(p, lim, origins, limits)
    return origins, limits

# Display output for these parameters and this plot
def display_output(p, lim, origins, limits):
    print("Probability = {:.2f}, step limit   = {:d}".
          format(p, lim))
    print("Proportion returning to origin   = {:.3f}".
          format(origins / C.SIMS))
    print("Probability of return to origin  = {:.3f}".
          format((1-p)/p))
    print("Proportion reaching limit        = {:.3f}\n".
          format(limits / C.SIMS))

# Get new parameters
# Check for validity of type and range
def get_parameters():
    while (True):
        try:
            p = float(input("Probability of step to the right = "))
            if p >= 0.5 and p <= 1.0: break
            else: print("Must be 0.5 <= p <= 1.0")
        except: print("Must be real number")

    while (True):
        try:
            lim = int(input("Limit of steps for a simulation = "))
            if 0 < lim: break
            else: print("Must be 0 < lim")
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
            # Store counts of returns to origin for each
            #   set of simulations
            origins = []
            # Run the simulations
            for k in C.PROBABILITIES:
                origins.append(step_until_return_to_origin(
                               k, lim_save)[0] / C.SIMS)
            # Plot the graph of returns to origin
            rp.generate_vlines("Proportion returning to origin out of {:d} simulations".format(C.SIMS),
                               "Probability", C.PROBABILITIES, origins)

        # Multiple limits, loop over tuple in configuration
        # The tuple is of fractions of the total capital
        elif r == 'l':
            # Store counts of limits exceeded
            #   set of simulations
            limits = []
            # Run the simulations
            for k in C.LIMITS:
                limits.append(step_until_return_to_origin(
                              p_save, round(k*C.SIMS))[1] / C.SIMS)
            # Plot the graph of the limits reached
            rp.generate_vlines("Proportion reaching limit" + \
                               " for probability {:.3f}".format(p_save),
                               "Limits",
                               [round(k*C.SIMS) for k in C.LIMITS],
                               limits)

if __name__ == '__main__':
    main()
