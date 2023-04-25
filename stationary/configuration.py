# Maze Markov chain stationary DISTRIBUTION
# From Privault (2018), Section 7.2

# Copyright 2023. Moti Ben-Ari
# Creative Commons Attribution-ShareAlike

# Global configuration constants

import numpy as np

# Number of simulations
SIMS = 10000

# Number of states in the maze
STATES = 9

# Theoretical stationary distribution
DISTRIBUTION = [1/16, 2/16, 2/16, 1/16, 2/16, 2/16, 2/16, 3/16, 1/16]

# Cummulative distribution
CUMMULATIVE = DISTRIBUTION.copy()
for i in range(1,STATES):
    CUMMULATIVE[i] += CUMMULATIVE[i-1]

# Transition matrix
# Initialize with zeros and then
#   add non-zero transitions
P_0 = np.zeros((STATES, STATES), dtype=float)
P_0[0][1] = 1.0
P_0[1][0] = P_0[1][2] = 1/2
P_0[2][1] = P_0[2][5] = 1/2
P_0[3][6] = 1.0
P_0[4][5] = P_0[4][7] = 1/2
P_0[5][2] = P_0[5][4] = 1/2
P_0[6][3] = P_0[6][7] = 1/2
P_0[7][4] = P_0[7][6] = P_0[7][8] = 1/3
P_0[8][7] = 1.0

# Construct "cummulative" transition matrix
#   to facilitate search for the transition to take
# For example, instead of P10=P12=1/2
#   use P10=1/2, P12=1
P = np.zeros((STATES, STATES), dtype=float)
for i in range(STATES):
    so_far = 0.0
    for j in range(STATES):
        if P_0[i][j] == 0.0:
            P[i][j] = 0.0
        else:
            P[i][j] = so_far + P_0[i][j]
            so_far = P[i][j]
