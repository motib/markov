# Two-state Markov chain

# Copyright 2023. Moti Ben-Ari
# Creative Commons Attribution-ShareAlike

# Global configuration constants

# Prompt string
PROMPT = "s(aved) parameters,  n(ew) parameters\n" + \
         "q(uit),              h(elp)\n"

# Help string
HELP = "Two-state Markov chain\n" + \
       "Parameters are:\n" + \
       "  a, b = probabilities of transition a->b, b->a\n" + \
       "Output is:\n" + \
       "  theoretical stationary distribution\n" + \
       "  simulation  stationary distribution"

# Default parameters:
#   n: total particles in both urns
A_DEFAULT, B_DEFAULT = 1/2, 1/3

# Limit of simulations steps
LIMIT = 10000
