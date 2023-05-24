# Multiple gamblers

# Copyright 2023. Moti Ben-Ari
# Creative Commons Attribution-ShareAlike

# Parameters:
#   g: number of gamblers
#   n: total capital

# Output:
#   random division of total capital
#   average number of steps until one gambler wins
#   expectation of number of steps until one gambler wins

import configuration as C
import multiple_plot as mp
import random
import math

# Save parameters between runs
# Initialize with the defaults
g_save, n_save = C.G_DEFAULT, C.N_DEFAULT

# Initial indices of gamblers and division of captial
initial_gamblers, initial_capital = None, None

# Divide capital n randomly among all gamblers g
def initialize(g, n):
    global initial_gamblers, initial_capital

    # Indices of gamblers
    initial_gamblers = [i for i in range(g)]
    # Initial capital amounts to zero
    initial_capital  = [0]*g
    capital = n

    for i in range(g-1):
        # At most 1/2 of remaining capital to a gambler
        # so not too many with zero
        if capital > 1:
            initial_capital[i] = random.randint(1,capital//2)
        capital -= initial_capital[i]

    # Last gambler takes capital that removes
    initial_capital[g-1] = capital

    # Remove gamblers with 0 capital
    initial_gamblers = [gam for gam in initial_gamblers 
                        if initial_capital[gam] !=0]

# Display output: parameters, division of capital
#   average steps and expectation of steps
def display_output(g, n, steps, expectation):
    print("Number of gamblers = {:d}, capital = {:d}".
          format(g, n))
    print("Division of initial capital =", initial_capital)
    print("Average  number of steps = {:d}".
          format(steps // C.SIMS))
    print("Expected number of steps = {:d}".
          format(expectation))

# Simulate the game
def simulate(g, n):
    steps = 0
    initialize(g, n)

    for i in range(C.SIMS):
        # current is the current distribution of capital
        #   and is updated after each round
        current = initial_capital.copy()
        # gamblers is the current set of gamblers
        #   those whose capital is 0 are removed
        gamblers = initial_gamblers.copy()

        while n not in current:
            steps += 1
            # Randomly choose two gamblers
            gambler1 = gamblers[random.randint(0,len(gamblers)-1)]
            gambler2 = gambler1
            # Make sure they are different
            while gambler2 == gambler1:
                gambler2 = gamblers[random.randint(0,len(gamblers)-1)]

            # Play a round of the game and update current
            if random.randint(0,1) == 0:
                current[gambler1] -= 1
                current[gambler2] += 1
            else:
                current[gambler1] += 1
                current[gambler2] -= 1

            # Remove a ruined gambler from gamblers
            if current[gambler1] == 0:
                gamblers.remove(gambler1)
            elif current[gambler2] == 0:
                gamblers.remove(gambler2)

    # Compute expectation and display the output
    expectation = (n**2 - sum([i**2 for i in initial_capital])) // 2
    display_output(g, n, steps, expectation)
    return steps, expectation

# Get new parameters: gamblers and capital
# Check for validity of type and range
def get_parameters():
    while (True):
        try:
            g = int(input("Number of gamblers = "))
            if g >= 2: break
            else: print("Must be >= 2")
        except: print("Must be integer")

    while (True):
        try:
            n = int(input("Capital = "))
            if n > 0: break
            else: print("Must be > 0")
        except: print("Must be integer")

    return g, n

def main():
    global g_save, n_save

    while True:
        r = input(C.PROMPT)
        # Initialize list for multiple runs
        averages = []
        expectations = []

        if   r == 'q': break
        elif r == 'h': input(C.HELP)
        elif r == 'n':
            g_save, n_save = get_parameters()
            simulate(g_save, n_save)
        elif r == 's':
            simulate(g_save, n_save)
        elif r == 'g':
            for g in C.PERCENTAGES:
                steps, expectation = simulate(math.floor(g*g_save), n_save)
                averages.append(steps // C.SIMS)
                expectations.append(expectation)
            mp.generate_vlines("Gamblers", g_save, averages, expectations)

        elif r == 'c':
            for c in C.PERCENTAGES:
                steps, expectation = simulate(g_save, math.floor(c*n_save))
                averages.append(steps // C.SIMS)
                expectations.append(expectation)
            mp.generate_vlines("Total capital", n_save, averages, expectations)

if __name__ == '__main__':
    main()
