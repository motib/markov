# Gambler's ruin

# Copyright 2023. Moti Ben-Ari
# Creative Commons Attribution-ShareAlike

# Global configuration constants

import math

CLOSE = False
# False: The plot need not be closed before running again
#       Does not work is run from Thonny and IDLE
#         but does work in Visual Studio Code
# True: Plot must be closed before continuing


# Help string
HELP = "Extinction of a branching process\n" + \
       "  Choose the distribution for population in a new state,\n" + \
       "     probability and number of levels\n" + \
       "Output is:\n" + \
       "  Probability of extinction\n" + \
       "  Proportion  of extinctions"

# Prompt strings
PROMPT1 = "s(aved) parameters,  n(ew) parameters\n" + \
          "multiple (p)robabilities\n" + \
          "q(uit),              h(elp)\n"

PROMPT2 = "Distribution:\n" + \
          "  0 = P(Y_1=1 | X_1=1)\n" + \
          "  1 = P(Y_1=2 | X_1=1)\n"

PROMPT3 = "Probability:\n"

PROMPT4 = "Number of levels:\n"

# Number of simulations
SIMS = 100

# Default distribution and number of levels
DISTRIBUTION_DEFAULT = 0
PROBABILITY_DEFAULT  = 0.7
LEVELS_DEFAULT       = 6
