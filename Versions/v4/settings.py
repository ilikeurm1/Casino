"""Settings file responsible for the creation of profiles and saving the money of the user."""

import os
import json
import base64
from time import sleep


# CUSTUMIZABLE SETTINGS
obfuscation_amount: int = (
    5  # The amount of times the money gets obfuscated | max is 50 -> Memory issues (thanks python)
)


main_directory = (  # You can customise this field as you want
    os.getcwd()
    + r"\profiles\v4"
)  # Please try not to change this -> data loss | moving files manually


# Add users file
USER_FILE_NAME = "Users.json"

save_file = os.path.join(main_directory, USER_FILE_NAME)  # Used to save users money

# Make the main directory of the game
os.makedirs(main_directory, 511, True)


def obf(s: str, a: int) -> str:
    """recursive function that obfuscates a string a of times

    Args:
        s (str): string to be obfuscated
        a (int): amount of times to be obfuscat

    Returns:
        str: obfuscated string
    """
    if a == 0:
        return s
    s = base64.b64encode(s.encode()).decode()
    return obf(s, a - 1)


def deobf(s: str, a: int):
    """Oppisite of obf() it deobfuscates the string so it gets back the same as it was given

    Args:
        s (str): string to be deobfuscated
        a (int): amount of times it was encoded
    """
    if a == 0:
        return s
    s = base64.b64decode(s.encode()).decode()
    return deobf(s, a - 1)


def get_game_profile() -> str:
    """Function to get the game profile of the user."""
    print()
    gp = input(
        "What is your username: "
    ).capitalize()  # If you have already played put in your exact name! ex. Admin

    return gp


# Save function
def save(to_save: int, gp: str) -> None:
    """Function to save the money of the user in the json file.

    Args:
        to_save (int): The amount of money to save.

    Returns:
        None
    """

    m = obf(str(to_save), obfuscation_amount)

    with open(save_file, "r", encoding="utf-8") as rf:
        usrs = json.load(rf)
        try:
            usrs[gp]["Money"] = m
            with open(save_file, "w", encoding="utf-8") as wf:
                json.dump(usrs, wf, indent=4)
            print()
            print(f"Saved money as: {to_save}$")
        except KeyError:
            print("Money not saved, unknown user!")


def settings_main() -> tuple[int, str]:
    """Main function for the settings."""
    print()
    print(f"Storing game files in path: {main_directory}")
    gp = get_game_profile()
    if os.path.exists(save_file):  # If the file exists
        print()
        print(f"Hello {gp}")
        with open(save_file, "r", encoding="utf-8") as read_file:  # Open the file
            try:  # Try to load the users
                users = json.load(read_file)
            except (
                json.decoder.JSONDecodeError,
                PermissionError,
            ):  # If the users file is empty (somehow)
                print(
                    "The users file is empty (it shouldn't be), creating a new one..."
                )
                users = {}
                money = int(
                    input("How much money do u want to start with: ")
                )  # Ask the user how much money he wants to start with
                m = obf(str(money), obfuscation_amount)  # Obfuscate the money
                users[gp] = {"Money": m}  # Add the user to the users file
                with open(save_file, "w", encoding="utf-8") as write_file:
                    json.dump(users, write_file, indent=4)  # Save the users file

            try:  # If the user has already played
                m = users[gp]["Money"]  # Get the money of the user
                money = int(
                    deobf(m, obfuscation_amount)
                )  # Decode the money back to a number int
                if money == 0:
                    print()
                    money = int(input("How much money do u want to start with: "))
                    m = obf(str(money), obfuscation_amount)
                    users[gp]["Money"] = m
                    with open(save_file, "w", encoding="utf-8") as write_file:
                        json.dump(users, write_file, indent=4)

            except (
                KeyError
            ):  # Someones has already played but a new user is trying to play
                money = int(
                    input("How much money do u want to start with: ")
                )  # Ask the user how much money he wants to start with
                m = obf(str(money), obfuscation_amount)  # Obfuscate the money
                users[gp] = {"Money": m}  # Add the user to the users file
                with open(save_file, "w", encoding="utf-8") as write_file:
                    json.dump(users, write_file, indent=4)  # Save the users file
    else:  # New game file
        money = int(
            input("How much money do u want to start with: ")
        )  # Ask the user how much money he wants to start with
        m = obf(str(money), obfuscation_amount)  # Obfuscate the money
        data = {gp: {"Money": m}}  # Add the user to the users file
        with open(save_file, "w", encoding="utf-8") as write_file:
            json.dump(data, write_file, indent=4)

    print()
    print(f"You are starting with {money}$, have fun!")
    sleep(1)
    return money, gp
