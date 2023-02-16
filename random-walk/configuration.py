# One-dimensional random walk

# Copyright 2023. Moti Ben-Ari
# Creative Commons Attribution-ShareAlike

# Global configuration constants

CLOSE = False
# False: The plot need not be closed before running again
#       Does not work is run from Thonny and IDLE
#         but does work in Visual Studio Code
# True: Plot must be closed before continuing

# Number of simulations
SIMS = 10000

# Prompt string
PROMPT = "One run:       s(aved) parameters,  n(ew) parameters\n" + \
         "Multiple runs: p(robabilities),     l(limits)\n" + \
         "               q(uit),              h(elp)\n"

# Help string
HELP = "\nOne-dimensional random walk\n" + \
       "Parameters are:\n" + \
       "  p = probability of a step to the right\n" + \
       "  lim = step limit\n" + \
       "Output is:\n" + \
       "  proportion and probability of return to the origin\n" + \
       "  proportion of simulations that reached the limit\n"

# Default parameters:
# Probability, number of simulations, step limit
P_DEFAULT, LIM_DEFAULT = 0.5, 1000

# Probabilities for multiple simulations
PROBABILITIES = (0.50, 0.55, 0.60, 0.65, 0.70, 0.75)

# Limits (percentages) for multiple simulations
LIMITS = (0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0)
