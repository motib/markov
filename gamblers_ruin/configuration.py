# Gambler's ruin

# Copyright 2023. Moti Ben-Ari
# Creative Commons Attribution-ShareAlike

# Global configuration constants

CLOSE = False
# False: The plot need not be closed before running again
#       Does not work is run from Thonny and IDLE
#         but does work in Visual Studio Code
# True: Plot must be closed before continuing

# Prompt string
PROMPT = "One run:       s(aved) parameters,  n(ew) parameters\n" + \
         "Multiple runs: p(robability) range, i(nitial) range\n" + \
         "               q(uit),              h(elp)\n"

# Help string
HELP = "Gambler's ruin\n" + \
       "Parameters are:\n" + \
       "  p = probability of A winning a step\n" + \
       "  n = total capital of both players\n" + \
       "  i = initial value of A's capital\n" + \
       "Output is:\n" + \
       "  wins, losses, simulation reached limit\n" + \
       "  proportion of wins, theoretical probability of wins\n" + \
       "  histogram of steps until ruin\n" + \
       "Multiple runs for lists of probability and initial capitals\n" +\
       "  given in the configuration file\n" + \
       "Output histogram and plot of proportions of wins\n"

# Number of simulations
SIMS = 10000

# Limit of steps to ruin
LIMIT = 1000

# Default parameters:
#   P = probability, N = total capital, I = A's initial capital
P_DEFAULT, N_DEFAULT, I_DEFAULT = 0.45, 20, 10

# Probabilities for multiple simulations
PROBABILITIES = (0.35, 0.40, 0.45, 0.50, 0.55)

# Initial values (percentages) for multiple simulations
INITIALS = (0.3, 0.4, 0.5, 0.6, 0.7)

# Histogram configuration

# Bins
BINS = 30

# Range of x axis
MIN_RANGE = 0
MAX_RANGE = 200

# Colors for successive plots
# The first color will be used for a single plot
COLORS = ['blue', 'red', 'green',
          'magenta', 'cyan', 'yellow',
          'orange', 'navy', 'lime']

# Maximum number of plots per histogram
PLOTS = len(COLORS)
