# Two-dimensional random walk

# Copyright 2023. Moti Ben-Ari
# Creative Commons Attribution-ShareAlike

# Global configuration constants

CLOSE = False
# False: The plot need not be closed before running again
#       Does not work is run from Thonny and IDLE
#         but does work in Visual Studio Code
# True: Plot must be closed before continuing

# Number of simulations
SIMS = 1000

# Probability is always 0.5 for 2D, 3D random walk
p = 0.5

# Prompt string
PROMPT = "One run:       s(aved) parameters,  n(ew) parameters\n" + \
         "Multiple runs: l(limits)\n" + \
         "               q(uit),              h(elp)\n"

# Help string
HELP = "\nTwo-dimensional random walk\n" + \
       "Parameters are:\n" + \
       "  limit = step limit\n" + \
       "Output is:\n" + \
       "  proportion and probability of return to the origin\n" + \
       "  proportion of simulations that reached the limit\n" + \
       "  mean duration and expected duration (steps)\n"

# Default step limit
LIMIT_DEFAULT = 10000

# Limits (percentages) for multiple simulations
LIMITS = (0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9)
