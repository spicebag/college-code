# Random Dice Roll
# Simulates a dice rolling and gives you the figure that is rolled.
# 21/10/2022
# @Author : Killian

import random

# Generate a random number between 1 and 2.
coin=random.randint(1,2)

if coin==1:
    print("Heads") # 1 means heads.
    print(coin)
else:
    print("Tails") # 2 means tails.
    print(coin)