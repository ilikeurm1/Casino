"""Settings file responsible for the creation of profiles and saving the money of the user."""

import os
import json
from time import sleep


# CUSTUMIZABLE SETTINGS
main_directory = (  # You can customise this field as you want
    os.getcwd()
    + r"\profiles\v4"  # Please try not to change this -> data loss | moving files manually
)

# Add users file
USER_FILE_NAME = "Users.json"

save_file = os.path.join(main_directory, USER_FILE_NAME)  # Used to save users money

# Make the main directory of the game
os.makedirs(main_directory, 511, True)


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

    with open(save_file, "r", encoding="utf-8") as rf:
        usrs = json.load(rf)
        try:
            usrs[gp]["Money"] = to_save
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
    if os.path.exists(save_file):
        with open(save_file, "r", encoding="utf-8") as read_file:
            print()
            print(f"Hello {gp}")
            try:
                users = json.load(read_file)
            except json.decoder.JSONDecodeError:  # If the users file is empty (somehow)
                os.remove(save_file)  # Delete the file
            # IF user does not exist, ask the money question
            try:
                money = users[gp]["Money"]
                if money == 0:
                    print()
                    money = int(input("How much money do u want to start with: "))
                    with open(save_file, "w", encoding="utf-8") as write_file:
                        json.dump(users, write_file, indent=4)
            
            except (KeyError):  # Someones has already played but a new user is trying to play
                money = int(input("How much money do u want to start with: "))
                users[gp] = {"Money": money}
                with open(save_file, "w", encoding="utf-8") as write_file:
                    json.dump(users, write_file, indent=4)
    else:
        # New game file
        print(f"Hello {gp}")
        print()
        money = int(input("How much money do u want to start with: "))
        data = {gp: {"Money": money}}
        with open(save_file, "w", encoding="utf-8") as write_file:
            json.dump(data, write_file, indent=4)

    print()
    print(f"You are starting with {money}$, have fun!")
    sleep(1)
    return money, gp
