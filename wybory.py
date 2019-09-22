#Verbatim from: https://github.com/GMIT-mmurray/Software-Programming-2018/tree/master/GroupA/Python/12.11.18
#Assignment: Simulate an election
from random import random

total_A_wins = 0
total_B_wins = 0

trials = 1000000
for trial in range(0, trials):
    A_win = 0
    B_win = 0
    if random() < .69:  # 1st region
        A_win += 1
    else:
        B_win += 1
    if random() < .65:  # 2nd region
        A_win += 1
    else:
        B_win += 1
    if random() < .14:  # 3rd region
        A_win += 1
    else:
        B_win += 1
    # determine overall election outcome
    if A_win > B_win:
        total_A_wins += 1
    else:
        total_B_wins += 1

print("A wins {} so the probability of A winning {}".format(total_A_wins, total_A_wins / trials))
print("B wins {} so the probability of B winning {}".format(total_B_wins, total_B_wins / trials))