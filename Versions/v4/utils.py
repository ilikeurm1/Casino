"""Utility functions for the game"""

from random import choice
from rich.text import Text
from typing import Any

from settings import sleep, console, randint

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


def find_duplicates(slots: list[int]) -> int:
    for x in slots[:len(slots) - 1]:
        if slots.count(x) == 2:
            return x
    return 0


def roll_anim(slots: list[int]) -> None:
    """Roll animation

    Args:
        slots (list[int]): The 3 numbers that were rolled.
    """
    # Can touch but these are good defaults
    time = 3 # Time the animation should take in seconds (around)
    frames = 1000 # Number of frames (amount of times the machine will show random numbers)
    
    filled = [False, False, False]
    machine: str = "  _______________\n /_______________\\\n|=================|\n| ({}) | ({}) | ({}) |\n|=================|\n \\_______________/\n"
    slot_machine_height = machine.count("\n") + 1
    
    sleep(1)
    
    for x in range(frames): # Make it have some length
        if x == frames // 3:
            filled[0] = True
        elif x == 2 * frames // 3:
            filled[1] = True
        
        console.print(machine.format(slots[0] if filled[0] else randint(1,9), slots[1] if filled[1] else randint(1,9), randint(1,9)), style="b magenta")
        print(f"\033[{slot_machine_height}A", end="")  # Move up `slot_machine_height` lines
        sleep(time / frames) 
    
    console.print(machine.format(slots[0], slots[1], slots[2]), style="b magenta")
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
        console.print(
            f"[blue]DEBUG PRINT: The winning number was: {data['winning_number']}"
        )
        
        vals = (
            data["chosen"],
            data["winning_number"]
        ) if DEBUG_MODE == 1 else (
            69,
            69
        ) if DEBUG_MODE == 2 else (
            data["chosen"],
            data["winning_number"]
        )
        
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
        console.print(f"[blue]DEBUG PRINT: The slot machine ended at: {data["slot_machine"]}")
        
        vals = (
            data["slot_machine"]
        ) if DEBUG_MODE == 1 else (
            7, 7, 7
        ) if DEBUG_MODE == 2 else (
            data["slot_machine"]
        )
        
    elif game == "blackjack":
        console.print(f"[blue]DEBUG PRINT: Dealer's hand was: {data["dealer_hand"]}, Total: {sum(data["dealer_hand"])}")
        
        vals = (
            data["player_hand"],
            data["dealer_hand"]
        ) if DEBUG_MODE == 1 else (
            [10, 11],
            [10, 10, 2]
        ) if DEBUG_MODE == 2 else (
            data["player_hand"],
            data["dealer_hand"]
        )
        
    elif game == "baccarat":
        console.print(f"[blue]DEBUG PRINT: Player's hand was: {data["player_cards"]}, Banker's hand was: {data["banker_cards"]}")
        
        vals = (
            data["player_cards"],
            data["banker_cards"]
        ) if DEBUG_MODE == 1 else (
            [8,1],
            [6]
        ) if DEBUG_MODE == 2 else (
            data["player_cards"],
            data["banker_cards"]
        )

    return vals

# endregion

# region strings
def welcome(user) -> Text:
    """Welcome message"""
    WELCOME = Text(
        f"Welcome to the Casino {user}!\n\nWhat game do you want to play?\n\n1. Number Guesser | Rewards: 2x\n2. Roulette | Rewards: 2x (Color) 5x (Number) 10x (Green or 0)\n3. Slots | Rewards: 3x (2 of the same) 8x (2x '7') 8x (3 of the same) 100x (3x '7')\n4. Blackjack | Rewards: 10x (Blackjack) 3x (Win)\n5. Baccarat | Rewards: 3x\n\n\n(Type quit to leave the program)\n\nPlease type the number assigned to it",
        style="green"
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
