from random import random


def flipcoin():

    if random() > 0.5:
        return "HEADS"
    else:
        return "TAILS"


print(flipcoin())
