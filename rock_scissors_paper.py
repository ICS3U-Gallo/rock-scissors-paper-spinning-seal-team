"""
Rock, Scissors, Paper

Group members:
"""

import random

Draw = True

#Base code

def decider(comp, human):
    global Draw
    Win = "You win"
    Lose = "You Lose"
    Dra = "Draw"
    if comp == human:
        return Dra
    if comp == 'Rock' and human == 'Paper' or comp == 'Scissors' and human == 'Rock' or comp == 'Paper' and human == 'Scissors':
        Draw = False
        return Win
    if comp == 'Paper' and human == 'Rock' or comp == 'Rock' and human == 'Scissors' or comp == 'Scissors' and human == 'Paper':
        Draw = False
        return Lose

while Draw is True:
    inp = input('Please enter your choice: ')
    choice = int(random.randint(0, 2))
    RPS = ['Rock', 'Paper', 'Scissors']
    print(RPS[choice])
    Answer = decider(RPS[choice], inp)
    print("\n" + Answer)

