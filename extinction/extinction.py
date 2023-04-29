# Branching process

# Compute extinction probability

# Copyright 2023. Moti Ben-Ari
# Creative Commons Attribution-ShareAlike

import configuration as C
import extinction_plot as ep
import random

# Save parameters between runs
# Initialize with the defaults
d_save, p_save, l_save = \
    C.DISTRIBUTION_DEFAULT, C.PROBABILITY_DEFAULT, C.LEVELS_DEFAULT

def simulate():
    # Total extinctions of all simulation runs
    extinctions = 0
    for n in range(C.SIMS):
        # For each level compute its population
        population_at_this_level = 1
        for l in range(l_save):
            population_of_states = 0
            # Each state at this level adds a number
            #   according to the distribution
            for i in range(population_at_this_level):
                if d_save == 0:
                    y1 = 1 if random.random() < p_save else 0
                else:  # d_save = 1
                    y1 = 2 if random.random() < p_save else 0
                population_of_states += y1
            population_at_this_level = population_of_states
            # If population is zero, this is an extinction
            if population_at_this_level == 0:
                extinctions += 1
                break

    prob = display_output(extinctions)
    return prob, extinctions

def display_output(extinctions):
    global d_save, p_save, l_save
    print("Probability = {:.3f}, levels = {:d}".\
          format(p_save, l_save))
    if d_save == 0:
        prob = 0.0 if p_save == 1.0 else 1.0
        print("Probability of extinction  = {:.3f}".format(prob))
    else:
        prob = (1.0-p_save)/p_save if 1.0-p_save < p_save else 1.0
        print("Probability of extinction  = {:.3f}".format(prob))
    print("Proportion  of extinctions = {:.3f}\n".
          format(extinctions / C.SIMS))
    return prob

#def generate_plot(title, exp, mean):
#    global populations
#    fig = bp.init_graph()
#    bp.generate_histogram(populations, exp, mean)
#    bp.finish_graph(fig, title)

# Get new parameters
# Check for validity of type and range
# Allow empty string input for default
def get_parameters():
    while (True):
        try:
            d = int(input(C.PROMPT2))
            if 0 <= d and d <= 1: break
            else: print("Must be 0 <= d <= 1")
        except: 
            print("Must be integer")
    while (True):
        try:
            p = float(input(C.PROMPT3))
            if 0.0 <= p and p <= 1.0: break
            else: print("Must be 0.0 <= p <= 0.1")
        except:
            print("Must be float")
    while (True):
        try:
            l = int(input(C.PROMPT4))
            if l >= 2: break
            else: print("Must be l >= 2")
        except:
            print("Must be integer")
    return d, p, l

# Display the distribution only once for
#   multiple probabilities
def display_distribution():
    global d_save
    if d_save == 0:
        print("Distribution is P(Y_1=1 | X_1=1)")
    else:
        print("Distribution is P(Y_1=2 | X_1=1)")

def main():
    global d_save, p_save, l_save

    while True:
        r = input(C.PROMPT1)

        if   r == 'q': break
        elif r == 'h': input(C.HELP)

        elif r == 's':
            display_distribution()
            simulate()

        elif r == 'n':
            d_save, p_save, l_save = get_parameters()
            display_distribution()
            simulate()

        elif r == 'p':
            # Simulate for multiple probabilities
            #   and save probabilities and proportions
            p_values = (0.4, 0.5, 0.6, 0.7, 0.8, 0.9)
            probabilities = []
            proportions   = []
            d_save = 1
            display_distribution()
            for p in p_values:
                p_save = p
                prob, extinctions = simulate()
                probabilities.append(prob)
                proportions.append(extinctions / C.SIMS)

            # Plot probabilities and proportions
            ep.generate_vlines(p_values, probabilities, proportions)
 
if __name__ == '__main__':
    main()
