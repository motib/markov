# Ballot box

# Copyright 2023. Moti Ben-Ari
# Creative Commons Attribution-ShareAlike

import configuration as C
import ballot_box_plot as bp
import random
import numpy as np

a_save, b_save = C.A_DEFAULT, C.B_DEFAULT

def count_votes(a, b):
    # Count of simulations where A is not always leading
    failures = 0

    for i in range(C.SIMS):
        votes_a = votes_b = 0
        for j in range(a+b):
            # If all votes for A counted, enter vote for B
            if votes_a == a:
                votes_b += 1
            # If all votes for B counted, enter vote for A
            elif votes_b == b:
                votes_a += 1
            else:
                # Compute the probability of a vote for A
                #   from the remaining A votes (a-votes_a)
                #   divided by the remaining votes (a+b-(votes_a+votes_b))
                prob_a = (a-votes_a) / (a+b-(votes_a+votes_b))
                if random.random() < prob_a:
                    votes_a += 1
                else:
                    votes_b += 1

            # Failure is A is not leading
            if votes_a <= votes_b:
                failures += 1
                break

    print('For a = {:2d}, b = {:2d}:'.format(a,b))
    print('Probability of A always leading = {:.4f}'.\
           format((a-b)/(a+b)))
    print('Proportion  of A always leading = {:.4f}'.\
           format((C.SIMS-failures)/C.SIMS))

    return (a-b)/(a+b), (C.SIMS-failures)/C.SIMS

# Get new parameters
# Check for validity of type and range
def get_parameters():
    while (True):
        try:
            a = int(input("Votes for A = "))
            if a > 0: break
            else: print("Must be a > 0")
        except: print("Must be integer")

    while (True):
        try:
            b = int(input("Votes for B = "))
            if b > 0 and b < a: break
            else: print("Must be 0 < b < a")
        except: print("Must be integer")
    return a, b

def main():
    global a_save, b_save

    while True:
        r = input(C.PROMPT)
        if   r == 'q': break
        elif r == 'h': input(C.HELP)
        elif r == 's':
            count_votes(a_save, b_save)

        elif r == 'n':
            a_save, b_save = get_parameters()
            count_votes(a_save, b_save)

        # For a fixed number of A votes
        #   simulate for multiple values of B votes
        elif r == 'm':
            probabilities = []
            proportions   = []
            for i in range(0, a_save, C.DELTA_B):
                prob, prop = count_votes(a_save, i)
                probabilities.append(prob)
                proportions.append(prop)
            bp.generate_vlines(a_save, np.array(probabilities), np.array(proportions))

if __name__ == '__main__':
    main()
