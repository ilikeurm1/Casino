"""Utility functions for the game"""

# region Imports

from typing import Any

from settings import (
    # 3rd party
    sleep, # time
    choice, randint, # random
    console, Text, FloatPrompt, # rich
    # Consts
    UTILS_DIR,
    ANIM_TIME
    )

# endregion

# region functions

def clear() -> None:
    """Clears the console"""
    console.clear(home=False)

def bet(money: int) -> tuple[int, int]:
    """Bet function

    Args:
        money (int): The players total money

    Returns:
        bet (tuple[int, int]): The money of the player after the bet and the money the player is betting
    """

    # While an invalid amount is given
    while 1:
        console.print()

        # Ask for the bet amount
        money_betting = FloatPrompt.ask(
            f"[green]How much do you want to bet (You have {money}$, type '0' to go all in and '0.5' to bet half)",
        )

        # Tell the player to bet a serious amount
        if money_betting > money:  # Invalid money amount
            console.print("[prompt.invalid]You don't have that much money!!!")
            continue

        # All-in
        if money_betting == 0:
            money_betting = money

        elif money_betting == 0.5:  # Half
            money_betting = money // 2

        elif money_betting < 1:
            console.print("[prompt.invalid]You can't bet less than 1$")
            continue

        # Any other valid number
        money_betting = int(money_betting)
        console.print()
        console.print(f"[blue]ok! You are betting {money_betting}$")
        break

    total = money - money_betting

    return total, money_betting

def hascolor(x: int) -> str:
    """returns if a number has a color

    Args:
        x (int): The number of which the color is wanted

    Returns:
        color (str): the color of the number
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
    """Finds the duplicate in the slot machine

    Args:
        slots (list[int]): the ended slot machine

    Returns:
        x (int | 0): the number that is found twice or 0 if there is no duplicate
    """
    # Look at the first two numbers only as if the third one is a duplicate we would have found it before
    for x in slots[: len(slots) - 1]:
        if slots.count(x) == 2:
            return x

    return 0

def roll_anim(slots: list[int]) -> None:
    """Roll animation

    Args:
        slots (list[int]): The 3 numbers that were rolled.
    """
    # Can touch but these is a good default
    frames = 1000  # Number of frames

    # Filled list to keep track of how far along we are in animation
    filled = [False, False, False]
    # The string that we will insert the numbers into
    machine: str = (
        "  _______________\n /_______________\\\n|=================|\n| ({}) | ({}) | ({}) |\n|=================|\n \\_______________/\n"
    )
    # The height of this string
    slot_machine_height = machine.count("\n") + 1

    sleep(1)

    for x in range(frames):         # For every frame
        if x == frames // 3:        # If we reached 1/3 of the total frames
            filled[0] = True        # Start showing the first number
        elif x == 2 * frames // 3:  # When we reach 2/3 of the total frames
            filled[1] = True        # Show the second number

        # Print the formatted slot machine
        console.print(
            machine.format(
                slots[0] if filled[0] else randint(1, 9), # insert the correct num if filled[0] is true
                slots[1] if filled[1] else randint(1, 9), # same but second num
                randint(1, 9),                            # always random as the last frame `frames + 1` is completely filled
            ),
            style="b magenta",                            # Make it very visible as the numbers are green
        )

        print(
            f"\033[{slot_machine_height}A", end=""
        )  # Move up `slot_machine_height` lines and don't add another newline (end="")

        # Sleep for the correct amount of time to reach a total of ~`ANIM_TIME` seconds in the end
        sleep(ANIM_TIME / frames)

    # Print the full machine when done so in the end the player looks at the correct list
    console.print(machine.format(slots[0], slots[1], slots[2]), style="b magenta")

def ascii_art_anim(ascii_art: list[Text]) -> None:
    frames = len(ascii_art)  # Number of frames (lines the ascii_art has)
    for line in ascii_art:
        console.print(line, end="")
        sleep(ANIM_TIME / frames)

def deal_card() -> int:
    """Deals a card for Blackjack"""
    #        2  3  4  5  6  7  8  9  10  J   Q   K   A
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    return choice(cards)

def random_style() -> str:
    colors = ["red", "green", "blue", "yellow", "magenta", "cyan"]
    effects = ["bold", "italic", "underline", "blink", "reverse", "strike"]
    return f"{choice(colors)} {choice(effects)}"

def DEBUG_GAME(DEBUG_MODE: int, game: str, data: dict[str, Any]) -> tuple:
    """Gives debug info depending on the game and the mode

    Args:
        DEBUG_MODE (int): the debug mode for now its 1 and 2 (1 is for play testing so it just gives the debug info, 2 is when an admin, so the game always wins)
        game (str): the game that is being played
        data (dict[str, str | int]): the data that is being used in the game

    Returns:
        vals (tuple): the debug data with the (non)adjusted values
    """

    # print the data dict no matter what debug is being used
    print(data)

    # Define vals tuple
    vals: tuple = ()

    # Values will only be changed if the debug is set to 2 (admin) as value 1 (test) is just for playtesting so no modification is necessary

    # Number guesser
    if game == "guesser":
        console.print(
            f"[blue]DEBUG PRINT: The winning number was: {data['winning_number']}"
        )

        vals = (
            (data["chosen"], data["winning_number"]) if DEBUG_MODE == 1

            else (69, 69) if DEBUG_MODE == 2

            else (data["chosen"], data["winning_number"])
        )

    # Roulette
    elif game == "roulette":
        console.print(
            f"[blue]DEBUG PRINT: The winning number was: {data['winning_number']} this had color: {data['winning_color']}"
        )

        vals = (
            (
                data["chosen_number"],
                data["chosen_color"],
                data["winning_number"],
                data["winning_color"],
            ) if DEBUG_MODE == 1

            else (0, "g", 0, "g",) if DEBUG_MODE == 2

            else (
                data["chosen_number"],
                data["chosen_color"],
                data["winning_number"],
                data["winning_color"],
            )
        )

    # Slots
    elif game == "slots":
        console.print(
            f"[blue]DEBUG PRINT: The slot machine ended at: {data["slot_machine"]}"
        )

        vals = (
            (data["slot_machine"]) if DEBUG_MODE == 1

            else (7, 7, 7) if DEBUG_MODE == 2

            else (data["slot_machine"])
        )

    # Blackjack
    elif game == "blackjack":
        console.print(
            f"[blue]DEBUG PRINT: Dealer's hand was: {data["dealer_hand"]}, Total: {sum(data["dealer_hand"])}"
        )

        vals = (
            (data["player_hand"], data["dealer_hand"]) if DEBUG_MODE == 1

            else ([10, 11], [10, 10, 2]) if DEBUG_MODE == 2

            else (data["player_hand"], data["dealer_hand"])
        )

    # Baccarat
    elif game == "baccarat":
        console.print(
            f"[blue]DEBUG PRINT: Player's hand was: {data["player_hand"]}, Banker's hand was: {data["banker_hand"]}"
        )

        vals = (
            (data["player_hand"], data["banker_hand"]) if DEBUG_MODE == 1

            else ([8, 1], [6]) if DEBUG_MODE == 2

            else (data["player_hand"], data["banker_hand"])
        )

    # Return the vals tuple
    return vals

# endregion

# region strings

def welcome(user) -> Text:
    """Welcome message"""
    WELCOME = Text(
        f"Welcome to the Casino {user}!\n\nWhat game do you want to play?\n\n1. Number Guesser | Rewards: 2x\n2. Roulette | Rewards: 2x (Color) | 5x (Number) | 10x (Green or 0)\n3. Slots | Rewards: 3x (2 of the same) | 8x (2x '7') | 8x (3 of the same) | 100x (3x '7')\n4. Blackjack | Rewards: 3x (Win) | 10x (Blackjack)\n5. Baccarat | Rewards: 3x\n\n\n(Type quit to leave the program)\n\nPlease type the number assigned to it",
        style="green"
    )
    return WELCOME

def bye(hs, hw, tw) -> Text:
    """Goodbye message"""
    BYE = Text(
        f"\nGood bye! Thanks for playing!\n\nCredits:\n\nProgramming: Matthijs Duhoux\n\nFun Facts:\nYour highest streak was when you won {max(hs)} time(s) in a row\n\nYour highest winning was {max(hw)}$\n\nIn total you won {tw} time(s)!\n",
        style="green"
    )
    return BYE

LOST = Text(
    "\nSorry but you have no money left! You have lost the game!\nYou can start a new game by restarting the program!",
    style="b red"
    )

ROULETTE_WELCOME = Text(
    "What do you want to bet on, pick from:\n\nNumbers: 0 - 36\nColors: Red, Black, Green\n\nPayouts:\n\n0 and Green = 10x your bet\nNumber (1 - 36) = 5x your bet\nRed or Black = 2x your bet\n\nYou choose to bet on",
    style="green"
    )

# region ascii art

# BLUE GRINCH:

# Get the location of the blue grinch file
blue_grinch_file = UTILS_DIR + r"\imgs\Bluegrinch.txt"

# Read the blue grinch string
with open(blue_grinch_file, "r") as rf:
    BLUE_GRINCH: list[Text] = []
    for line in rf.readlines():
        BLUE_GRINCH.append(Text(line, "b rgb(10,142,214)", justify="center", no_wrap=True))

# Sans

# Get the location of the sans file
sans_file = UTILS_DIR + r"\imgs\Sans.txt"

# Read the sans string
with open(sans_file, "r") as rf:
    SANS: list[Text] = []
    for line in rf.readlines():
        SANS.append(Text(line, "b rgb(255,255,255)", justify="center", no_wrap=True))

# Freddy

# Get the location of the freddy file
freddy_file = UTILS_DIR + r"\imgs\Freddy.txt"

# Read the freddy string
with open(freddy_file, "r") as rf:
    FREDDY: list[Text] = []
    for line in rf.readlines():
        FREDDY.append(Text(line, "b rgb(166,96,34)", justify="center", no_wrap=True))

# Get the location of the freddy jumpscare file
Freddy_jumpscare_file = UTILS_DIR + r"\imgs\Freddy_jumpscare.txt"

# Read the freddy jumpscare string
with open(Freddy_jumpscare_file, "r") as rf:
    FREDDY_JUMPSCARE: list[Text] = []
    for line in rf.readlines():
        FREDDY_JUMPSCARE.append(Text(line, "b rgb(166,96,34)", justify="center", no_wrap=True))


# endregion

# endregion


# region main

def main() -> None:
    """Main function."""
    Chars = [
        BLUE_GRINCH,
        SANS,
        FREDDY,
    ]

    # 0 = Blue Grinch, 1 = Sans, 2 = Freddy
    chosen = 1

    Char = Chars[chosen]

    ascii_art_anim(Char)

if __name__ == "__main__":
    try:
        main()
        print("Program exited successfully\nexit code: 0")

    except Exception as e:
        print(f"An error occurred: {e}\nexit code: you choose lmao 1 ig?")

# endregion
