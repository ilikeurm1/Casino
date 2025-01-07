"""Utility functions for the game"""

# region Imports

from typing import Any

from settings import (
    # 3rd party
    sleep, # time
    choice, randint, # random
    console, Text, Prompt, Confirm, # rich
    music, # pygame
    # Self-made
    # Funcs
    convert_number_to_string,
    # Consts
    UTILS_DIR,
    )

# endregion

# region functions

def clear() -> None:
    """Clears the console"""
    console.clear(home=False)

def get_money_from_string(s: str, m: int) -> int:
    """Converts a string typed by the user to an int

    An example of the input could be:
        "999k": 999000
        "10m": 10000000
        "10b": 10000000000
        "10b 10m": 10010000000

    Args:
        s (str): the string that is in the format of a number
        m (int): the users money, this is needed for some comparisons

    Returns:
        int: the number that the string represents
    """

    VALS: dict[str, int] = {
        "k": 10**3,
        "m": 10**6,
        "b": 10**9,
        "t": 10**12,
        "quad": 10**15,
        "quint": 10**18,
        "sext": 10**21,
        "sept": 10**24,
        "o": 10**27,
        "n": 10**30,
        "d": 10**33,
    }

    n: int = 0

    # Lower the string so we can check for the keys
    s = s.lower()

    # Split the string into the number and the suffix
    parts = s.split()

    # All-in / Half in check
    if len(parts) == 1:
        if s == "0":
            return m
        elif s in (".5", "0.5"):
            return m // 2

    # Go through the parts and add the number to the total
    for part in parts:
        # If the part is a digit, add it to the total
        if part.isdigit():
            n += int(part)
        else:
            # Go through the dictionary and find the key that matches the suffix
            for key, value in VALS.items():
                # If the last character of the part is the key
                if part[-1] == key:
                    # Add the number to the total
                    count = int(part[:-1]) if part[:-1].isdigit() else 1
                    n += count * value
                    break

    # Checks
    # Tell the player to bet a serious amount
    if n > m:  # Invalid money amount
        console.print("[prompt.invalid]You don't have that much money!!!")
        return 0

    if n < 1: # Invalid
        console.print("[prompt.invalid]You can't bet less than 1$")
        return 0

    return n

def bet(money: int) -> tuple[int, int]:
    """Bet function

    Args:
        money (int): The players total money

    Returns:
        bet (tuple[int, int]): The money of the player after the bet and the money the player is betting
    """

    # While an invalid amount is given
    while 1:
        # Ask for the bet amount
        m = Prompt.ask(
            f"[green]How much do you want to bet?\n"
            f"You have {money}$, that is: {convert_number_to_string(money)}\n"
            "Type '0' to go all in and '0.5' to bet half)"
        )

        # Get the money the user has bet through the string alg
        money_betting = get_money_from_string(m, money)

        # See if an invalid amount was given
        if money_betting == 0:
            continue

        # Check if the person really wants to bet this amount
        if Confirm.ask(
            f"[blue]This means you will be betting {convert_number_to_string(money_betting)}\n"
            f"That will leave you with {money - money_betting}$ ({convert_number_to_string(money - money_betting)})\n\n"
            "Are you sure this is what you want to bet?",
            default=True):
            break

    # Valid number
    console.print()
    console.print(f"[blue]ok! You are betting {money_betting}$")
    console.print()

    return money - money_betting, money_betting

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
    # Can touch but this is a good default
    frames = 1000  # Number of frames

    # Filled list to keep track of how far along we are in animation
    filled = [False, False, False] # Third one not needed but is nice to show what this means
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

        # Sleep for the correct amount of time to reach a total of ~3 seconds in the end
        sleep(3 / frames)

    # Print the full machine when done so in the end the player looks at the correct list
    console.print(machine.format(slots[0], slots[1], slots[2]), style="b magenta")

def ascii_art_anim(ascii_art: list[Text], t: int = 3) -> None:
    """An asciiart animation that goes on for ~t seconds

    Args:
        ascii_art (list[Text]): The list of strings that make up the ascii art
        t (int, optional): The time the animation should take in seconds. Defaults to 3.
    """
    frames = len(ascii_art)  # Number of frames (lines the ascii_art has)
    for line in ascii_art:
        console.print(line, end="")
        sleep(t / frames)

def play_sound(f: str, v: float = .5, wait: bool=False):
    """Plays the sound with name f at volume v

    Args:
        f (str): the name of the file *ONLY NEED THE FILE NAME NO MP3* and no \\
        v (float, optional): Volume to be played at. Defaults to .5.
        wait (bool, optional): If the program should wait until the sound is done playing. Defaults to False
    """
    music.set_volume(v)
    music.load(UTILS_DIR + "\\sounds\\" + f + ".mp3")
    music.play()
    if wait:
        while music.get_busy():
            sleep(0.1)

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
        f"Welcome to the Casino {user}!\n"
        "\n"
        "What game do you want to play?\n"
        "\n"
        "1. Number Guesser | Rewards: 2x\n"
        "2. Roulette | Rewards: 2x (Color) | 5x (Number) | 10x (Green or 0)\n"
        "3. Slots | Rewards: 3x (2 of the same) | 8x (2x '7') | 8x (3 of the same) | 100x (3x '7')\n"
        "4. Blackjack | Rewards: 3x (Win) | 10x (Blackjack)\n"
        "5. Baccarat | Rewards: 3x\n"
        "\n"
        "\n"
        "(Type quit to leave the program)\n"
        "\n"
        "Please type the number assigned to it",
        style="green"
    )
    return WELCOME

def bye(hs, hw, tw) -> Text:
    """Goodbye message"""
    BYE = Text(
        f"\nGood bye! Thanks for playing!\n\nCredits:\n\nProgramming: Matthijs Duhoux\n\nFun Facts:\nYour highest streak was when you won {hs} time(s) in a row\n\nYour highest winning was {hw}$\n\nIn total you won {tw} time(s)!\n",
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
with open(UTILS_DIR + r"\imgs\Bluegrinch.txt", "r") as rf:
    BLUE_GRINCH: list[Text] = []
    for line in rf.readlines():
        BLUE_GRINCH.append(Text(line, "b rgb(10,142,214)", justify="center", no_wrap=True))

# Sans
with open(UTILS_DIR + r"\imgs\Sans.txt", "r") as rf:
    SANS: list[Text] = []
    for line in rf.readlines():
        SANS.append(Text(line, "b rgb(255,255,255)", justify="center", no_wrap=True))

# Freddy
with open(UTILS_DIR + r"\imgs\Freddy.txt", "r") as rf:
    FREDDY: list[Text] = []
    for line in rf.readlines():
        FREDDY.append(Text(line, "b rgb(166,96,34)", justify="center", no_wrap=True))

# Freddy jumpscare
with open(UTILS_DIR + r"\imgs\Freddy_jumpscare.txt", "r") as rf:
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
