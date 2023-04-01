# Maze Markov chain
# From Privault (2018), Section 5.3

# Copyright 2023. Moti Ben-Ari
# Creative Commons Attribution-ShareAlike

# Since Python arrays are indexed from 0
#   the indices are offset from those in the book

import configuration as C
import random

# Returns to state i when goal is state i
returns = [0]*C.STATES

# Run the simulation
def simulate_return(goal):
    global returns
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
    # Returns to i from i
    returns[goal] = counts[goal]
    # Display output when all simulations terminate
    formatted_array("Average  steps to return to {:d} = ".format(goal), counts)

def formatted_array(s, a):
    values = ["{:2d}".format(elem) for elem in [c // C.SIMS for c in a]]
    print(s + '[' + ', '.join(values) + ']')

def main():
    # Print the expectations from Privault
    print("Expected steps to return to 0 = " + \
          "[16, 15, 28, 59, 48, 39, 58, 55, 56]")
    for goal in range(0,9):
        simulate_return(goal)
    print("\nExpected steps to return to i from i = " + \
          "[16,  8,  8, 16,  8,  8,  8,  5, 16]")
    formatted_array("Average  steps to return to i from i = ", returns)

if __name__ == '__main__':
    main()
