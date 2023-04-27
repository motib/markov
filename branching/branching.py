# Branching process

# Compute mean population size

# Copyright 2023. Moti Ben-Ari
# Creative Commons Attribution-ShareAlike

import configuration as C
#import branching_plot as pp
import random

# Save parameters between runs
# Initialize with the defaults
d_save, l_save = C.DISTRIBUTION_DEFAULT, C.LEVELS_DEFAULT

# Functions for computing population in the following state
# Throwing a fair die
def sample0():
    return random.randint(1,6)

# Throwing a fair die until a six appears
def sample1():
    r = random.randint(1,6)
    throws = 1
    while r != 6:
        r = random.randint(1,6)
        throws += 1
    return throws

# Draw a random coupon from a box until all
#   five coupons have been drawn
def sample2():
    # Initially no coupon draw
    bins = [False] * C.COUPONS
    # Draw until all coupons drawn
    all_drawn = False
    draws = 0
    while not all_drawn:
        # Draw and update bins
        bins[random.randint(0,C.COUPONS-1)] = True
        draws += 1
        # Check if all bins True
        all_drawn = True
        for c in range(C.COUPONS):
            if not bins[c]:
                all_drawn = False
    return draws

def simulate(distribution, title, expectation, levels):
    # Total population of all simulation runs
    total_population = 0
    for n in range(C.SIMS):
        # For each level compute its population
        population_at_this_level = 1
        for l in range(levels):
            population_of_states = 0
            # Each state at this level adds a number
            #   accodring to the distribution
            for i in range(population_at_this_level):
                if distribution == 0:
                    population_of_states += sample0()
                elif distribution == 1:
                    population_of_states += sample1()
                else:
                    population_of_states += sample2()
            population_at_this_level = population_of_states
        total_population += population_at_this_level

    # Total expectation is the expectation of a single level
    #   raised to the number of levels
    display_output(title, 
                   int(expectation ** levels),
                   total_population // C.SIMS)

def display_output(title, expectation, mean):
    print(title + ", levels = {:d}".format(l_save))
    print("Expectation of mean population size: {:d}".
          format(expectation))
    print("Simulatation   mean population size: {:d}\n".
          format(mean))

# Get new parameters
# Check for validity of type and range
# Allow empty string input for default
def get_parameters():
    while (True):
        try:
            d = input(C.PROMPT2)
            d = int(d)
            if 0 <= d and d <= 2: break
            else: print("Must be 0 <= d <= 2")
        except: 
            if d == "":
                d = C.DISTRIBUTION_DEFAULT
                break
            else: print("Must be integer")
    while (True):
        try:
            l = input(C.PROMPT3)
            l = int(l)
            if l >= 2: break
            else: print("Must be l >= 2")
        except:
            if l == "":
                l = C.LEVELS_DEFAULT
                break
            else: print("Must be integer")
    return d, l

def main():
    global d_save, l_save

    while True:
        r = input(C.PROMPT1)

        if   r == 'q': break
        elif r == 'h': input(C.HELP)
        elif r == 's':
            simulate(d_save, C.TITLES[d_save], 
                     C.EXPECTATIONS[d_save], l_save)
        elif r == 'n':
            d_save, l_save = get_parameters()
            simulate(d_save, C.TITLES[d_save], 
                     C.EXPECTATIONS[d_save], l_save)

if __name__ == '__main__':
    main()
