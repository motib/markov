# Ballot box

# Copyright 2023. Moti Ben-Ari
# Creative Commons Attribution-ShareAlike

# Global configuration constants

CLOSE = False
# False: The plot need not be closed before running again
#       Does not work is run from Thonny and IDLE
#         but does work in Visual Studio Code
# True: Plot must be closed before continuing

# Prompt string
PROMPT = "s(aved) parameters,  n(ew) parameters\n" + \
         "m(ultiple) votes for B\n" + \
         "q(uit), h(elp)\n"

# Help string
HELP = "Ballot box\n" + \
       "Parameters are:\n" + \
       "  a = votes for A\n" + \
       "  b = votes for B\n" + \
       "Output is:\n" + \
       "  theoretical probability   A always leading\n" + \
       "  proportion of simulations A always leading \n"

# Number of simulations
SIMS = 1000

# Default parameters:
A_DEFAULT, B_DEFAULT = 20, 18

# Delta for multiple B votes
DELTA_B = 2
