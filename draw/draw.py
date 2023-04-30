# Gambler's ruin with possibility of a draw

# Select parameters:
#   p: probability of step right by A
#   n: total capital
#   i: initial capital of A

# Output:
#   wins, losses, proportion of wins,
#   theoretical probability of winning,
#   average duration, expected duration

# Display:
#   histogram of duration

# Run once or for a sequence of
#   probabilities or initial values
# Display graph of proportions of wins
#   and histograms for a sequence

# Copyright 2023. Moti Ben-Ari
# Creative Commons Attribution-ShareAlike

import configuration as C
import draw_plot as dp
import random
import numpy as np

# Array of number of steps
#   First index is the plot number
#   Second index is the number of steps in a simulation
step_counts = np.zeros((C.PLOTS, C.SIMS), dtype=int)

# Save parameters between runs
# Initialize with the defaults
p_save, n_save, i_save = C.P_DEFAULT, C.N_DEFAULT, C.I_DEFAULT

# Run the simulation
#   sim_index for multiple simulations of
#     probabilities or initial values
def step_until_zero_or_n(p, n, i, sim_index=0):
    # Count of A's wins and losses
    # Count of simulations terminated by reaching a limit
    wins, losses, limits = 0, 0,  0
    
    for j in range(C.SIMS):
        steps = 0      # Count number of steps
        current = i    # Current capital of A

        # Move until reached zero or end
        while current != 0 and current != n:
            steps += 1
            if steps > C.LIMIT:
                limits += 1
                break
            # Range is 0 to p for +1, p to 1-p for -1,
            #   1-p to 1 for draw
            r = random.random()
            if   r < p:   current += 1
            elif r > 1-p: current -= 1

        # Save step count for this simulation
        step_counts[sim_index][j] = steps

        # Count wins and losses
        if   current == 0: losses += 1
        elif current == n: wins += 1

    display_output(p, n, i, sim_index, wins, losses, limits)
    return wins

# Display output for these parameters and this plot
def display_output(p, n, i, sim_index, wins, losses, limits):
    # Print parameters
    print("\nProbability = {:.2f}, capital = {:d}, initial = {:d}".
          format(p, n, i))
    # Print wins, losses and limits
    print("Wins = {:d}, losses = {:d}, limits exceeded = {:d}".
          format(wins, losses, limits))
    # Print proportion of wins and
    #   theoretical probability of winning for these parameters
    print("Proportion of wins     = {:.4f}".
          format(wins/C.SIMS))
    print("Probability of winning = {:.4f}".
           format((n-i) / n))

    # Print average and expected duration
    print("Average duration  = {:d}".
          format(round(np.mean(step_counts[sim_index]))))
    print("Expected duration = {:d}".
          format(int((i*(n-i)/(2*p)))))

# Get new parameters
# Check for validity of type and range
def get_parameters():
    while (True):
        try:
            p = float(input("Probability of A winning = "))
            if p > 0.0 and p <= 0.5: break
            else: print("Must be 0.0 < p <= 0.5")
        except: print("Must be real number")

    while (True):
        try:
            n = int(input("Total amount = "))
            if n > 0: break
            else: print("Must be 0 < n")
        except: print("Must be integer")

    while (True):
        try:
            i = int(input("A's initial amount = "))
            if 0 <= i and i <= n: break
            else: print("Must be 0 <= i <= n")
        except: print("Must be integer")
    return p, n, i

# Generate the plots for probabilities or initials
# Caller generates constant list for the other one
def generate_plots(r, probabilities, n, initials, title):
    fig = dp.init_graph()
    histograms = []

    for k in range(len(probabilities)):
        # Run the simulation which returns number of wins
        wins = step_until_zero_or_n(
                    probabilities[k], n, initials[k], k)

        # Create label for probabilities or initials
        #   and plot the proportion of wins for each element
        label = "p = " + str(probabilities[k])
        if r == "p":
            dp.plot_wins(probabilities, wins/C.SIMS, k, "Probability")
        if r == 'i':
            label = "i = " + str(initials[k])
            dp.plot_wins(initials, wins/C.SIMS, k, "Initial values")

        # Generate the histograms for each entry
        #   and append to the list of histograms
        # The first element of the returned list
        #   is a list of the counts in each bin
        histograms.append(
            dp.generate_histogram(step_counts[k], k, label))
    
    # Plot vertical lines at the average duration
    #   for each probability or initial
    # The height of a line is the maximum of the
    #   maximum of each histogram
    for k in range(len(probabilities)):
        dp.generate_vline(
            round(np.mean(step_counts[k])),
            max([max(h[0]) for h in histograms]), k)

    dp.finish_graph(fig, title)

# Get mode and call simulations, then plot
def main():
    global p_save, n_save, i_save

    while True:
        r = input(C.PROMPT)

        if   r == 'q': break
        elif r == 'h': input(C.HELP)
        elif r == 's':
            title = "Gambler's ruin for p = {:.2f}, n = {:d}, i = {:d}".\
                        format(p_save, n_save, i_save)
            generate_plots(r, [p_save], n_save, [i_save], title)

        elif r == 'n':
            p_save, n_save, i_save = get_parameters()
            title = "Gambler's ruin for p = {:.2f}, n = {:d}, i = {:d}".\
                        format(p_save, n_save, i_save)
            generate_plots(r, [p_save], n_save, [i_save], title)

        # Multiple probabilities, loop over tuple in configuration
        elif r == 'p':
            title = "Gambler's ruin for n = {:d}, i = {:d}".\
                      format(n_save, i_save)
            # Generate constant list of initials
            initials = [i_save] * len(C.PROBABILITIES)
            generate_plots(r, C.PROBABILITIES, n_save, initials, title)

        # Multiple initial values, loop over tuple in configuration
        # The tuple is of fractions of the total capital
        elif r == 'i':
            initials = [round(n_save*i) for i in C.INITIALS]
            title = "Gambler's ruin for p = {:.2f}, n = {:d}".\
                      format(p_save, n_save)
            # Generate constant list of probabilities
            probabilities = [p_save] * len(initials)
            generate_plots(r, probabilities, n_save, initials, title)

if __name__ == '__main__':
    main()
