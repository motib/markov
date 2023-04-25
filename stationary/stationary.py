# Maze Markov chain stationary distribution
# From Privault (2018), Section 7.2

# Copyright 2023. Moti Ben-Ari
# Creative Commons Attribution-ShareAlike

# Since Python arrays are indexed from 0
#   the indices are offset from those in the book

import configuration as C
import random

# Choose a random start state according to the distribution
def random_state():
      r = random.random()
      for i in range(C.STATES):
            if r < C.CUMMULATIVE[i]:
                  return i

# Run the simulation
def simulate():
    # Counts for first state
    first_states = [0]*C.STATES

    for n in range(C.SIMS):
        # Choose zero'th state according to 
        #   stationary distribution
        zero_state = random_state()
        # Take transition to a next state according to
        #   the transition matrix
        r = random.random()
        for i in range(C.STATES):
            if r < C.P[zero_state][i]:
                first_states[i] += 1
                break

    # Print zero-state theoretical distribution
    #   and simulated first-state distribution
    # first-state are counts so divide by C.SIMS
    formatted_array("Stationary distribution:      \n", C.DISTRIBUTION)
    formatted_array("Distribution after first step:\n", [count/C.SIMS for count in first_states])

# Format with forced four decimal places
#   and no quotes
def formatted_array(s, a):
    values =  [f'{c:.4f}' for c in a]
    print(s + '[' + ', '.join(values) + ']')

def main():
    simulate()

if __name__ == '__main__':
    main()
