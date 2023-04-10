# Random walk around a circle

# Copyright 2023. Moti Ben-Ari
# Creative Commons Attribution-ShareAlike

# Global configuration constants

CLOSE = False
# False: The plot need not be closed before terminating
#        Does not work is run from Thonny and IDLE
#          but does work in Visual Studio Code
# True: Plot must be closed before terminating

# Number of simulations
SIMS = 1000

# Number of steps per simulation
STEPS = 3000

# Number of points in the circle
POINTS = 50

# Designated last point (arbitrary)
LAST_POINT = 24

# Parameters for the histogram
BINS = 50

MIN_RANGE = 0
MAX_RANGE = (STEPS * 3) // 4
