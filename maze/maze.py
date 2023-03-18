# Maze Markov chain
# From Privault (2018), Section 5.3

# Copyright 2023. Moti Ben-Ari
# Creative Commons Attribution-ShareAlike

# Since Python arrays are indexed from 0
#   the indices are offset from those in the book

import configuration as C
import random

# Run the simulation
def simulate_return(goal):
    # Counts for returning to the goal state
    counts = [0]*C.STATES

    for n in range(C.SIMS):
        # Starting in each of the states
        #   compute the count of steps to return
        #   to the goal state
        for initial in range(C.STATES):
            step_count = 0
            current = initial

            while True:
                # Unlikely but stop a simulation if
                #   if it runs for too long
                if step_count >= C.LIMIT:
                    print("Limit reached")
                    break

                # Choose a random number and search for
                #   the appropriate transition
                # For example, if r = 0.6 and P10=1/2, P12=1
                #   take the transition from 1 to 2
                r = random.random()
                for i in range(C.STATES):
                    if r < C.P[current][i]:
                        current = i
                        step_count += 1
                        break

                # Stop when returned to the goal
                if current == goal:
                    counts[initial] += step_count
                    break
    # Display output when all simulations terminate
    display_output(counts)

def display_output(counts):
    # Print the expectations from Privault
    #   and the averages from the simulations
    print("Expectation steps to return = " + \
          "[16, 15, 28, 59, 48, 39, 58, 55, 56]")
    print("Average steps to return     = " + \
          str([c // C.SIMS for c in counts]))

def main():
    simulate_return(C.GOAL)

if __name__ == '__main__':
    main()
