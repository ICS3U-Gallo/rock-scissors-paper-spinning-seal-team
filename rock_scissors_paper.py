"""
Rock, Scissors, Paper

Group members: Patrick, Chrisaanth, 
"""

import random

def gcf(r, p, s): #Finds greatest common denominator.
    found = False
    perclist = [r, p, s]
    perclist.sort()
    largest = perclist[-1]
    num = largest
    while found is False:
        num -= 1
        if r%num == 0 and p%num == 0 and s%num == 0:
            return num

def quitquest(yesno): #Program quitting logic.
    global draw
    if yesno == 'Yes':
        draw = False

def decider(comp, human): #Basic logic; determines rock paper scissors hierarchy.
    global score_comp, score_hum
    win = "You win"
    lose = "You Lose"
    dra = "Draw"
    if comp == human:
        return dra
    if comp == 'Rock' and human == 'Paper' or comp == 'Scissors' and human == 'Rock' or comp == 'Paper' and human == 'Scissors':
        score_hum += 1
        return win
    if comp == 'Paper' and human == 'Rock' or comp == 'Rock' and human == 'Scissors' or comp == 'Scissors' and human == 'Paper':
        score_comp += 1
        return lose

def predict_choice(rock, paper, scissors): #Computer determines whether to play rock paper or scissors depending on player's past data.
    total = rock + paper + scissors

    percrock = int((rock/total)*100)
    percpaper = int((paper/ total)*100)
    percscissors = int((scissors/total)*100)

    greatestcf = gcf(percrock, percpaper, percscissors)
    lowrock = int(percrock/greatestcf)
    lowscissors = int(percscissors/greatestcf)
    lowpaper = int(percpaper/greatestcf)

    perclist = []
    finalnumlist = [lowrock, lowscissors, lowpaper]

    for i in range(3):
        for i2 in range(finalnumlist[i]):
            if i == 0:
                perclist.append('Rock')
            if i == 1:
                perclist.append('Scissors')
            if i == 2:
                perclist.append('Paper')

    answer = random.choice(perclist)
    answerop = ''
    if answer == 'Rock':
        answerop = 'Paper'
    if answer == 'Paper':
        answerop = 'Scissors'
    if answer == 'Scissors':
        answerop = 'Rock'
    return answerop


while Draw is True:
    inp = input("\n" + "\n" + 'Please enter your choice (Rock, Paper, or Scissors): ')
    if inp == 'Rock':
        rock_played += 1
    if inp == 'Scissors':
        scissors_played += 1
    if inp == 'Paper':
        paper_played += 1

    if rock_played > 6:
        rock_played = 1
    if scissors_played > 6:
        scissors_played = 1
    if paper_played > 6:
        paper_played = 1

    choice = predict_choice(rock_played, paper_played, scissors_played)
    print("Computer response:", choice)
    answer = decider(choice, inp)
    print("\n" + answer)
    print("\n"+"Human score:", score_hum)
    print("Computer score:", score_comp)
    quit = input("\n"+'Quit? (Yes or No): ')
    quitquest(quit)

