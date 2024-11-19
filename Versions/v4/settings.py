"""Settings file responsible for the creation of profiles and saving the money of the user."""

import os
import json
import base64
from random import randint
from time import sleep
from rich.console import Console
from rich.prompt import Prompt, Confirm, IntPrompt, FloatPrompt

# region CUSTUMIZABLE SETTINGS

obfuscate: bool = False
fixed_obfuscation: bool = False  # If you want to have a fixed obfuscation amount

obf_count: int = (
    5  # Max amount of times the money gets obfuscated | max is 50 -> Memory issues (thanks laptop)
) # Also the amount of times the money gets obfuscated if fixed_obfuscation is True


main_directory = (  # You can customise this field as you want
    os.getcwd() + r"\profiles\v4"
)  # Please try not to change this -> data loss | moving files manually

# endregion


# region Please dont touch :)

# region misc

# Console settings
console = Console(color_system="truecolor", tab_size=4)

# Add users file
USER_FILE_NAME = "Users.json"

save_file = os.path.join(main_directory, USER_FILE_NAME)  # Used to save users money

# Make the main directory of the game
os.makedirs(main_directory, 511, True)

# Sound settings
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"

from pygame import mixer

mixer.init()

music = mixer.music

# endregion

# region functions

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
        return deobf(
            base64.b64decode(s.encode()).decode()  # Decode the string and try again
        )  # Decode the string and try again


def get_game_profile() -> str:
    """Function to get the game profile of the user."""
    console.print()
    console.print()
    spelled_correctly: bool = False
    while not spelled_correctly:
        gp = Prompt.ask(
            "[blue]What is your username: "
        ).capitalize()  # If you have already played put in your exact name! ex. Admin

        spelled_correctly = Confirm.ask(f"[blue]Is this correct: {gp}", default=True)

    return gp


def save(user: str, to_save: int):
    """An awesome save function that takes the user and their money and adds it to the save file

    Args:
        user (str): the users name
        to_save (int): the amount of money to be saved
    """
    
    encoded = obf(str(to_save))                                 # Obfuscate the money
    data: dict = {user: {"Money": encoded}}                     # Create the data dict in case of non existing
    with console.status("Saving money...", spinner="aesthetic"):
        with open(save_file, 'r', encoding='utf-8') as rf:      # Open the file
            try:
                data = json.load(rf)                            # Get all the players (overwriting line 143)
                data[user]["Money"] = encoded                   # Update the current players value or write a new value for the user
            except json.JSONDecodeError:                        # File is empty
                console.print(
                    "[red]The users file is empty (it shouldn't be), making first entry..."
                )
            except KeyError:                                    # The user is new and isn't in the save file yet
                console.print("[blue]Unknown user, creating an entry for you :)")
                data[user] = {"Money": encoded}                 # Add the user to the users file

    with open(save_file, 'w', encoding='utf-8') as wf:          # Open the file
        json.dump(data, wf, indent=4)                           # Save the users file
    
    console.print()
    console.print(f"[blue]Saved money as: {to_save}$")


def is_admin(gp: str) -> int:
    """Function to check if the user is admin or not."""
    ADMINS: dict[str, int] = {
        "Admin": 2, 
        "Test": 1
    }
    debug = ADMINS[gp] if gp in ADMINS.keys() else 0
    (
        console.log(f"You are logged in as the debugger: {gp}")
        if debug
        else console.log("You do not have permission for debugging :)")
    )
    sleep(2)
    return debug


def get_users_money(user: str) -> int:
    """Function to get the users money

    Args:
        user (str): the user to get the money from

    Returns:
        m (int): the users money
    """
    if os.path.exists(save_file):                           # If the file exists
        with open(save_file, "r", encoding="utf-8") as rf:  # Open the file
            try:                        
                users = json.load(rf)                       # Load the users
              
                m = users[user]["Money"]                    # Get the money of the user
                money = deobf(m)                            # Decode the money back to a number int
                if money != 0:                              # If the user didn't lose their money
                    return money                            # Decode the money back to a number int

            except (
                KeyError,                                   # The user is new and isn't in the save file yet 
                json.JSONDecodeError                        # The file is empty
                ):
                pass                                        # We have to ask the user how much money they want to start with
    
    m = IntPrompt.ask("[blue]How much money do u want to start with")
    return m

# endregion

# main function
def settings_main() -> tuple[int, str]:
    """Main function for the settings."""
    gp = get_game_profile()
    
    console.print()
    console.print(f"[magenta]Hello {gp}")
    
    money = get_users_money(gp)
    
    save(gp, money)

    console.print()
    console.print(f"[blue]You are starting with {money}$, have fun!")
    # sleep(3)
    return money, gp

# endregion
