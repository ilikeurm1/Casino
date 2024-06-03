"""Utility functions for the game"""

import os
from random import choice
from time import sleep


def clear() -> None:
    """Clears the conlose"""
    os.system("cls")


def bet(money: int) -> tuple[int, int]:
    """Bet function

    Args:
        money (int): The players total money

    Returns:
        tuple[int, int]: The money of the player after the bet and the money the player is betting
    """
    while 1:
        print()
        try:
            money_betting = int(
                input(
                    f"How much do you want to bet (You have {money}$, type '0' to go all in): "
                )
            )
        except ValueError:
            print()
            print("Please type a number!")
            continue

        if money_betting == 0:
            money_betting = money

        if money_betting > money:
            print()
            print("You dont have that much money!!!")

        else:
            print()
            print(f"ok! You are betting {money_betting}$")
            break

    total = money - money_betting

    return total, money_betting


def hascolor(x: int) -> str:
    """returns if a number has a color

    Args:
        x (int): The number of which the color is wanted

    Returns:
        str: the color of the number
    """

    red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
    if x == 0:
        color = "g"
    elif x in red:
        color = "r"
    else:
        color = "b"
    return color


def roll(slots: list[int]) -> None:
    """Roll animation

    Args:
        slots (list[int]): The 3 numbers that were rolled.
    """
    print()
    sleep(1)
    for i in range(3):
        print(slots[i], end=" ", flush=True)
        sleep(2)


def deal_card() -> int:
    """Deals a card for Blackjack"""
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    return choice(cards)


def welcome(user) -> str:
    """Welcome message"""
    return f"""
Welcome to the Casino {user}!

What game do you want to play? 

1. Number Guesser | Rewards: 2x
2. Roulette | Rewards: 2x (Color) 5x (Number) 10x (Green or 0)
3. Slots | Rewards: 3x (2 of the same) 8x (2x '7') 8x (3 of the same) 100x (3x '7')
4. Blackjack | Rewards: 10x (Blackjack) 3x (Win)
5. Baccarat | Rewards: 3x
       

(Type quit to leave the program)

Please type the number assigned to it: """


LOST = """
Sorry but you have no money left! You have lost the game! 
You can start a new game by restarting the program!"""


ROULETTE_WELCOME = """What do you guess, pick from:
                   
Numbers: 0 - 36
Colors: Red, Black, Green

Payouts:

0 and Green = 10x your bet
Number (1 - 36) = 5x your bet
Red or Black = 2x your bet

You choose to bet on: """


def bye(hs, hw, tw) -> str:
    """Goodbye message"""
    return f"""
Good bye! Thanks for playing!

Credits:

Programming: Matthijs Duhoux, ChatGPT (tiny changes)
                  
Fun Facts:

Your highest streak was when you won {max(hs)} time(s) in a row

Your highest winning was {max(hw)}$

In total you won {tw} time(s)!
"""
