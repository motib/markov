# Two-state Markov chain

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
         "p(roportion) B's,    m(multiple) b's\n" + \
         "q(uit),              h(elp)\n"

# Help string
HELP = "Two-state Markov chain\n" + \
       "Parameters are:\n" + \
       "  a, b = probabilities of transition a->b, b->a\n" + \
       "         if multiple b's, b parameter is ignored\n" + \
       "  p    = proportion of B's\n" + \
       "Output is:\n" + \
       "  theoretical stationary distribution\n" + \
       "  simulation  stationary distribution"

# Default parameters:
#   n: total particles in both urns
A_DEFAULT, B_DEFAULT = 1/2, 1/3

# Limit of simulations steps
LIMIT = 10000
