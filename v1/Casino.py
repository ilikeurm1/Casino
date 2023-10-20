# This is v1 of a small game ill make in python. I might make it bigger or ill forget about it :)

# imports

import random
import math
import os
import time

# File creaton

# import Settings

# Variables 

Streak = 0
Times_Won = 0
from Settings import Money, file_path

# Lists

Highest_Streak = []
Highest_Winnings = []

# Functions 

def Bet(money):
    while True:
        print("")
        Money_Betting = int(input("How much money do you want to bet (Type '0' to go all in): "))
        if Money_Betting == 0:
            Money_Betting = money
       
        if Money_Betting > money:
            print("")
            print("You dont have that much money!!!")
            
        else:
            print("")
            print(f"ok! You are betting {Money_Betting}$")
            break

    Total = money - Money_Betting
    time.sleep(1)
    return Total, Money_Betting

def HasColor(x):
    Red_Numbers = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
    if x == 0:
        Color = "g"
    elif x in Red_Numbers:
        Color = "r"
    else:
        Color = "b"
    return Color

# Games

# Number Guesser

def Guesser(Money_Bet, Streak, Times_Won):
    while True:
        print("")
        End = int(input("The game will pick a number from 1 to x, what is x (minimum '5'): "))
        print("")
        if End < 5:
            print("You tried! Please enter a minimum of 5")
            continue
        else:
            break
    Chosen = int(input("What number is your guess: "))
    Winning_Number = random.randint(1, End)
    if Winning_Number == Chosen:
        Money_Won = Money_Bet * 2
        Streak += 1
        Times_Won += 1
        print("")
        print(f"Nice! You chose the right number, you have doubled your money bet ({Money_Won}$)!")
    else:
        Money_Won = 0
        Streak = 0
        print("")
        print(f"Sorry! The correct number was {Winning_Number} and you chose {Chosen}, better luck next time!")
        time.sleep(1)
    return Money_Won, Streak, Times_Won
        
# Roulette

def Roulette(Money_Bet, Streak, Times_Won):
    Winning_Number = random.randint(0, 36)
    Winning_Color = HasColor(Winning_Number)
    # print(Winning_Number)
    # print(Winning_Color)
    Chosen = input("""What do you guess, pick from:
                   
Numbers: 0 - 36
Colors: Red, Black, Green

Payouts:

0 and Green = 10x your bet
Number (1 - 36) = 5x your bet
Red or Black = 2x your bet

You choose to bet on: """)
    Chosen_Color = Chosen[0].lower()
    
    time.sleep(1)
    try: # A number was chosen
        Chosen = int(Chosen)
        if Winning_Number == 0: # Multiplier
            Money_Multiplier = 10
        else:
            Money_Multiplier = 5
        if Chosen == Winning_Number:
            Money_Won = Money_Bet * Money_Multiplier
            Streak += 1
            Times_Won += 1
            print("")
            print(f"Nice! You chose the right number, you have {Money_Multiplier}x your money bet ({Money_Bet * Money_Multiplier}$)!")
        else:
            Money_Won = 0
            Streak = 0
            print("")
            print(f"Sorry! The correct number was {Winning_Number} and you chose {Chosen}, better luck next time!")
            time.sleep(1)

    except: # A color was chosen
        if Winning_Color == "g": # Multiplier
            Money_Multiplier = 10
        else:
            Money_Multiplier = 2
        if Chosen_Color == Winning_Color:
            Money_Won = Money_Bet * Money_Multiplier
            Streak += 1
            Times_Won += 1
            print("")
            print(f"Nice! You chose the right color, you have {Money_Multiplier}x your money bet ({Money_Bet * Money_Multiplier}$)!")
            time.sleep(1)
        else:
            Money_Won = 0
            Streak = 0
            print("")
            print(f"Sorry! The correct color was {Winning_Color} and you chose {Chosen}, better luck next time!")
            time.sleep(1)
    
    return Money_Won, Streak, Times_Won

# The main "UI" i guess

while True:
    Game = input("""
What game do you want to play? 

1. Number Guesser (Rewards 2x)
2. Roulette (Number Guesser but harder --> does reward more. Rewards: 2x (Color) 5x (Number) 10x (Green or 0)
       
You may type the name of the game or use the number assigned to it.

""")
    
    if Game == "Number Guesser" or int(Game) == 1:
        print("")
        print("You have chosen to play Number Guesser!")
        Money, Money_Betting = Bet(Money)
        Money_Won, Streak, Times_Won = Guesser(Money_Betting, Streak, Times_Won)
        Money = Money + Money_Won
        Highest_Winnings.append(Money_Won)

    elif Game == "Roulette" or int(Game) == 2:
        print("")
        print("You have chosen to play Roulette!")
        Money, Money_Betting = Bet(Money)
        Money_Won, Streak, Times_Won = Roulette(Money_Betting, Streak, Times_Won)
        Money = Money + Money_Won
        Highest_Winnings.append(Money_Won)
        
    print("")
    print(f"You now have {Money}$ and are on a streak of {Streak}")
    Highest_Streak.append(Streak)
    time.sleep(1)

# LOSE
    if Money == 0:
        print(f"""
Sorry but you have no money left! You have lost the game! You can start a new game by restarting the program!

Fun Facts:

Your highest streak was when you won {max(Highest_Streak)} time(s) in a row

Your highest winning was {max(Highest_Winnings)}$

In total you won {Times_Won} time(s)!
""")
        os.remove(file_path)
        break

# Run again
    print("")
    again = input("Run again? (y/n): ")
    if 'y' in again:
            with open(file_path, 'w') as fp:
                fp.write(str(Money))
                print("")
                print('Money saved!')
                time.sleep(2)
            continue
    elif 'n' in again:
            with open(file_path, 'w') as fp:
                fp.write(str(Money))


            print("")
            print(f"Money saved! When you come back next time you will start with {Money}$")
            time.sleep(2)
            print(f"""
Good bye!

Thank you for playing!

Credits:

Programming: Matthijs Duhoux
                  
Fun Facts:

Your highest streak was when you won {max(Highest_Streak)} time(s) in a row

Your highest winning was {max(Highest_Winnings)}$

In total you won {Times_Won} time(s)!             
""")
            break
    else:
            print("Invalid Input, the program will now shut off")
            break
