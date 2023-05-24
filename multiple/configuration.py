# Multiple gamblers

# Copyright 2023. Moti Ben-Ari
# Creative Commons Attribution-ShareAlike

# Global configuration constants

CLOSE = False
# False: The plot need not be closed before running again
#       Does not work is run from Thonny and IDLE
#         but does work in Visual Studio Code
# True: Plot must be closed before continuing

# Prompt string
PROMPT = "One run:  s(aved) parameters,  n(ew) parameters\n" + \
         "Multiple: g(amblers),          total c(apital)\n" + \
         "q(uit),                        h(elp)\n"

# Help string
HELP = "\nMultiple gamblers dividing the initial capital\n" + \
       "Parameters are:\n" + \
       "  g = number of gamblers\n" + \
       "  n = total capital of all gamblers\n" + \
       "Output is:\n" + \
       "  average number of steps until one gambler wins\n" + \
       "  expectation of number of steps until one gambler wins\n"

# Number of simulations
SIMS = 100

# Default parameters:
#   G = gamblers, N = total capital
G_DEFAULT, N_DEFAULT = 10, 50

# Percentages of gamblers or captial for multiple runs
PERCENTAGES = [0.2,0.4,0.6,0.8,1.0]