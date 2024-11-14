"""Utility functions for the game"""

from random import choice
from rich.text import Text
from typing import Any

from settings import sleep, console

# region functions

def clear() -> None:
    """Clears the console"""
    console.clear(home=False)


def bet(money: int) -> tuple[int, int]:
    """Bet function

    Args:
        money (int): The players total money

    Returns:
        tuple[int, int]: The money of the player after the bet and the money the player is betting
    """
    while 1:
        console.print()
        try:
            money_betting = int(
                console.input(
                    f"[green]How much do you want to bet (You have {money}$, type '0' to go all in): [/green]"
                )
            )
        except ValueError:
            console.print()
            console.print("[red]Please type a number![/red]")
            continue

        if money_betting == 0:
            money_betting = money

        if money_betting > money:
            console.print()
            console.print("[red]You don't have that much money!!![/red]")

        else:
            console.print()
            console.print(f"[blue]ok! You are betting {money_betting}$[/blue]")
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
    console.print()
    sleep(1)
    for i in range(3):
        console.print(slots[i], end=" ", style="b blue")
        sleep(2)


def deal_card() -> int:
    """Deals a card for Blackjack"""
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    return choice(cards)


def DEBUG_GAME(DEBUG_MODE: int, game: str, data: dict[str, Any]) -> tuple:
    """Gives debug info depending on the game and the mode

    Args:
        DEBUG_MODE (int): the debug mode for now its 1 and 2 (1 is for play testing so it just gives the debug info, 2 is when an admin, so the game always wins)
        game (str): the game that is being played
        data (dict[str, str | int]): the data that is being used in the game

    Returns:
        vals tuple: the debug data with the (non)adjusted values
    """

    print(data)

    vals: tuple

    if game == "guesser":
        vals = ()
        
    elif game == "roulette":
        console.print(
            f"[blue]DEBUG PRINT: The winning number was: {data['winning_number']} this had color: {data['winning_color']}"
        )

        vals = (                    # Don't change the values if the user is playtesting
            data["chosen_number"],
            data["chosen_color"],
            data["winning_number"],
            data["winning_color"],
        ) if DEBUG_MODE == 1 else ( # Set both the chosen and winning number to 0 so the player always wins
            0,
            "g",
            0,
            "g"
        ) if DEBUG_MODE == 2 else ( # Debug mode 3 if it comes in the future
            data["chosen_number"],
            data["chosen_color"],
            data["winning_number"],
            data["winning_color"],
        )
    
    elif game == "slots":
        vals = ()
        
    elif game == "blackjack":
        vals = ()
        
    elif game == "baccarat":
        vals = ()

    return vals

# endregion

# region strings
def welcome(user) -> Text:
    """Welcome message"""
    WELCOME = Text(
        f"\nWelcome to the Casino {user}!\n\nWhat game do you want to play?\n\n1. Number Guesser | Rewards: 2x\n2. Roulette | Rewards: 2x (Color) 5x (Number) 10x (Green or 0)\n3. Slots | Rewards: 3x (2 of the same) 8x (2x '7') 8x (3 of the same) 100x (3x '7')\n4. Blackjack | Rewards: 10x (Blackjack) 3x (Win)\n5. Baccarat | Rewards: 3x\n\n\n(Type quit to leave the program)\n\nPlease type the number assigned to it: ",
        style="bold blue"
    )
    return WELCOME

def bye(hs, hw, tw) -> Text:
    """Goodbye message"""
    BYE = Text(
        f"\nGood bye! Thanks for playing!\n\nCredits:\n\nProgramming: Matthijs Duhoux, ChatGPT (tiny changes)\n\nFun Facts:\n\nYour highest streak was when you won {max(hs)} time(s) in a row\n\nYour highest winning was {max(hw)}$\n\nIn total you won {tw} time(s)!\n",
        style="green"
    )
    return BYE

LOST = Text(
    "\nSorry but you have no money left! You have lost the game!\nYou can start a new game by restarting the program!",
    style="bold red"
)

ROULETTE_WELCOME = Text(
    "What do you want to bet on, pick from:\n\nNumbers: 0 - 36\nColors: Red, Black, Green\n\nPayouts:\n\n0 and Green = 10x your bet\nNumber (1 - 36) = 5x your bet\nRed or Black = 2x your bet\n\nYou choose to bet on",
    style="green",
)

# endregion
