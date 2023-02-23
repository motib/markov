# Ehrenfest model

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
         "q(uit),              h(elp)\n"

# Help string
HELP = "Ehrenfest model\n" + \
       "Parameters are:\n" + \
       "  n = total particles in both urns\n" + \
       "Output is:\n" + \
       "  theoretical stationary distribution and its graph (blue)\n" + \
       "  simulation  stationary distribution and its graph (red)"

# Default parameters:
#   n: total particles in both urns
N_DEFAULT = 10

# Limit of simulations steps
LIMIT = 10000
