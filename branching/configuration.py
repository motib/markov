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
HELP = "Mean population of a branching process\n" + \
       "  Choose the distribution for population in a new state\n" + \
       "     and number of levels\n" + \
       "Output is:\n" + \
       "  Expectation of mean population size\n" + \
       "  Simulated mean population size"

# Prompt strings
PROMPT1 = "s(aved) parameters,  n(ew) parameters\n" + \
          "q(uit),              h(elp)\n"

PROMPT2 = "Distribution:\n" + \
          "  0 = throw a die (default),\n" + \
          "  1 = throw a die until a six,\n" + \
          "  2 = coupon collector (five coupons)\n"

PROMPT3 = "Number of levels (default 4):\n"

# Number of simulations
SIMS = 100

# Number of coupons and compute the expectation
COUPONS = 5
exp_coupons = COUPONS * \
       (math.log(COUPONS) + (1.0/(2.0*COUPONS))
        +0.5772)

# Expectation of mean population size
EXPECTATIONS = (3.5, 6, exp_coupons)

# Default distribution and number of levels
DISTRIBUTION_DEFAULT = 0
LEVELS_DEFAULT = 4

# Title for printing output
TITLES = ("Throwing a fair die",
          "Throwing a die until a six appears",
          "Coupon collector (five coupons)")

# Bins
BINS = 30
