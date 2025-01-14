"""Settings file responsible for the creation of profiles and saving the money of the user."""

# region Imports

import os
import json
import base64
from random import randint, choice, random
from time import sleep

from rich.console import Console
from rich.prompt import Prompt, Confirm, IntPrompt, FloatPrompt
from rich.text import Text

# endregion

# region CUSTUMIZABLE SETTINGS

# The main directories of the game
# Please try not to change this -> data loss | moving files manually
MAIN_DIR = os.getcwd()

VERSION_DIR = MAIN_DIR + r"\Versions\v4"

SAVE_DIR = MAIN_DIR + r"\profiles\v4"

UTILS_DIR = VERSION_DIR + r"\Utils"

# Obfuscation settings
obfuscate: bool = False
fixed_obfuscation: bool = False  # If you want to have a fixed obfuscation amount

obf_count: int = (
    5  # Max amount or amount (fixed_obf = True) of times the money gets obfuscated | max is ~50 -> Memory issues (you don't need more than 5 normally)
)

# Misc
USE_SOUND: bool = True  # If you want to use sound or not

# endregion

# region Please dont touch :)

# region misc

# Console settings
console = Console(color_system="truecolor", tab_size=4)

# Add users file
USER_FILE_NAME = "Users.json"

save_file = os.path.join(SAVE_DIR, USER_FILE_NAME)  # Used to save users money

# Make the main directory of the game
os.makedirs(SAVE_DIR, 511, True)

# Sound settings
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"

# Import the mixer
from pygame import mixer  # noqa: E402

# Initialize the mixer
mixer.init()

# And set the music var to the music module in pygame.mixer
music = mixer.music

# endregion

# region functions

def convert_number_to_string(n: int) -> str:
    """Converts a large number to a readable format so the user knows how much they have.

    Args:
        n (int): number to convert to a string

    Returns:
        str: the number in a readable string
    """

    number_strings = {
        1: "$",
        10**2: "hundred",
        10**3: "thousand",
        10**6: "million",
        10**9: "billion",
        10**12: "trillion",
        10**15: "quadrillion",
        10**18: "quintillion",
        10**21: "sextillion",
        10**24: "septillion",
        10**27: "octillion",
        10**30: "nonillion",
        10**33: "decillion",
    }

    end_string = ""

    if n < 100:
        return f"{n}$"

    for value, name in sorted(number_strings.items(), reverse=True):
        count = n // value
        if count > 0:
            end_string += f"{count} {name} "
            n -= count * value

    return end_string.strip()

def convert_string_to_number(s: str) -> int:
    """Undoes the convert_number_to_string function and turns a string back into an int

    Args:
        s (str): the string to be reconverted to an int

    Returns:
        int: the string in the form of an int
    """

    string_numbers = {
        "$": 1,
        "hundred": 10**2,
        "thousand": 10**3,
        "million": 10**6,
        "billion": 10**9,
        "trillion": 10**12,
        "quadrillion": 10**15,
        "quintillion": 10**18,
        "sextillion": 10**21,
        "septillion": 10**24,
        "octillion": 10**27,
        "nonillion": 10**30,
        "decillion": 10**33,
    }

    end_number = 0
    parts = s.split(" ")

    for i in range(0, len(parts), 2):
        num = int(parts[i])
        unit = parts[i + 1]
        end_number += num * string_numbers[unit]

    return end_number

def obf(s: str) -> str:
    """recursive function that obfuscates a string a of times

    Args:
        s (str): string to be obfuscated

    Returns:
        str: obfuscated string
    """
    if obfuscate:
        if fixed_obfuscation:
            for _ in range(obf_count):
                s = base64.b64encode(s.encode()).decode()
            return s

        for _ in range(randint(1, obf_count)):
            s = base64.b64encode(s.encode()).decode()

    return s

def deobf(s: str) -> int:
    """Oppisite of obf() it deobfuscates the string so it gets back the same as it was given

    Args:
        s (str): string to be deobfuscated

    Returns:
        s (int): deobfuscated string
    """
    try:
        return int(s)  # If the string is a number
    except ValueError:
        return deobf( # Decode the string and try again
            base64.b64decode(s.encode()).decode()
        )

def get_game_profile() -> str:
    """Function to get the game profile of the user."""
    spelled_correctly: bool = False
    while not spelled_correctly:
        gp = Prompt.ask(
            "[blue]What is your username"
        ).capitalize()  # If you have already played put in your exact name! ex. Admin

        spelled_correctly = Confirm.ask(f"[blue]Is this correct: {gp}", default=True)

    return gp

def is_admin(gp: str) -> int:
    """Function to check if the user is admin or not.
    
    Args:
        gp (str): The users name

    Returns:
        int: Admin level
    """
    ADMINS: dict[str, int] = {
        "Admin": 2,
        "Test": 1
    }

    debug = ADMINS[gp] if gp in ADMINS.keys() else 0

    if debug:
        console.log(f"You are logged in as the debugger: {gp} (debug level: {debug})")
    else:
        console.log("You do not have permission for debugging :)")

    return debug

def get_users_money(user: str) -> int:
    """Function to get the users money

    Args:
        user (str): the user to get the money from

    Returns:
        m (int): the users money
    """
    if os.path.exists(save_file):  # If the file exists
        with open(save_file, "r", encoding="utf-8") as rf:  # Open the file
            try:
                users = json.load(rf)    # Load the users

                m = users[user]["Money"] # Get the money of the user
                money = deobf(m)         # Decode the money back to a number int
                if money != 0:           # If the user didn't lose their money
                    return money         # Return the players

            # If the user is new and not in save file (KeyError) or the file is empty (jsonError)
            except (
                KeyError,
                json.JSONDecodeError,
                ):
                pass  # We have to ask the user how much money they want to start with

    correct_amount: bool = False
    
    while not correct_amount:
        m = IntPrompt.ask("[blue]How much money do u want to start with")

        correct_amount = Confirm.ask(f"[blue]This means you will start with: {convert_number_to_string(m)}\nIs this correct?", default=True)

    return m

def save(user: str, to_save: int):
    """An awesome save function that takes the user and their money and adds it to the save file

    Args:
        user (str): the users name
        to_save (int): the amount of money to be saved
    """

    encoded = obf(str(to_save))  # Obfuscate the money
    data: dict = {user: {"Money": encoded}}  # Create the data dict in case of non existing
    with console.status("Saving money...", spinner="aesthetic"):
        with open(save_file, "r", encoding="utf-8") as rf:  # Open the file
            try:
                data = json.load(rf)  # Get all the players (overwriting line 143)
                data[user]["Money"] = encoded  # Update the current players value or write a new value for the user
            except json.JSONDecodeError:  # File is empty
                console.print(
                    "[red]The users file is empty (it shouldn't be), making first entry..."
                )
            except KeyError:  # The user is new and isn't in the save file yet
                console.print("[blue]Unknown user, creating an entry for you :)")
                data[user] = {"Money": encoded}  # Add the user to the users file

        with open(save_file, "w", encoding="utf-8") as wf:  # Open the file
            json.dump(data, wf, indent=4)  # Save the users file

        sleep(1.5) # add artificial lag show the nice spinner :)

        console.print()
        console.print(f"[blue]Saved money as: {to_save}$")
        console.print()

# endregion

# Main settings function

def settings_main() -> tuple[int, str]:
    """Main function for the settings."""
    # Title print
    console.print()
    console.print("--------------- LOGIN ---------------", style="bold rgb(191,84,8)")
    console.print()
    # Get the users username
    gp = get_game_profile()

    console.print()
    console.print(f"[magenta]Hello {gp}")

    # Get their stored money or ask for how much if they are new
    money = get_users_money(gp)

    # Save the persons money so if they're new they are now in the file
    save(gp, money)

    console.print(f"[blue]You are starting with {money}$, have fun!")
    console.print()

    return money, gp

# endregion
