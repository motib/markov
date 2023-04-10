# Random walk around a circle

# Copyright 2023. Moti Ben-Ari
# Creative Commons Attribution-ShareAlike

import configuration as C
import random_walk_circle_plot as rp
import random
import numpy as np

# Number of steps in a simulation to visit all points
# 0 = all points were not visited
visited_all = np.zeros(C.SIMS, dtype=int)

def simulate(last_point):
    # Store which points have been visited
    visited = np.zeros(C.POINTS, dtype=bool)
    # Initially, the first point is visited
    visited[0] = True

    # Number of points visited
    count_visited = 1

    # Current point and step counter
    current = 0
    steps = 0

    for i in range(C.STEPS):
        # Choose to step left or right
        if random.random() < 0.5: current += 1
        else:                     current -= 1
        # Modulo the number of points
        current %= 50
        steps += 1

        # Flag newly visited points
        #   and check if this point is the last one
        if not visited[current]:
            visited[current] = True
            count_visited += 1
            if count_visited == C.POINTS:
                break

    if count_visited == C.POINTS:
        return steps, (current == last_point)
    else:
        return 0, False

def print_output(visited_all, count_of_lasts, count_of_not_all):
    # Print number of times designated point was the last
    #   the probability and the proportion    
    print("For {:d} points, {:d} simulations, at most {:d} steps:".
          format(C.POINTS, C.SIMS, C.STEPS))
    print("  Designated point visited {:2d} times".
          format(count_of_lasts))
    print("    Probability = {:.3f}, proportion = {:.3f}".
          format(1.0/(C.POINTS-1), count_of_lasts/C.SIMS))

    # Print number of times the simulation did not visit all points
    print("  Did not visit all points {:2d} times".
          format(count_of_not_all))

def main():
    # Number of times designed point was the last
    #   and number of times all points were not visited
    count_of_lasts = 0
    count_of_not_all = 0

    for i in range(C.SIMS):
        # Simulate RW which returns number of steps
        #   to visit all points and a flag is the
        #   last point was the designed point
        visited_all[i], last = simulate(C.LAST_POINT)
        if last: count_of_lasts += 1
        if visited_all[i] == 0: count_of_not_all += 1
        
    print_output(visited_all, count_of_lasts, count_of_not_all)

    # Display historgram of steps needed to vist all points
    fig = rp.init_graph()
    h = rp.generate_histogram(visited_all)
    rp.finish_graph(fig)

    if not C.CLOSE: input("Press any key to terminate ")

if __name__ == '__main__':
    main()
