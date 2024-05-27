"""Settings file responsible for the creation of profiles and saving the money of the user."""

import os
import json
from time import sleep

# CUSTUMIZABLE SETTINGS
main_directory = (  # You can customise this field as you want
    os.getcwd()
    + r"\profiles\v4"  # Please try not to change this -> data loss | moving files manually
)


# Ask for profile
def get_full_dir() -> tuple[str, str]:
    """Function to get the full directory of the game."""
    print()
    gp = input(
        "What is your username: "
    ).capitalize()  # If you have already played put in your exact name! ex. Admin

    # Make the main directory of the game
    print()
    print(f"Storing game files in path: {main_directory}")
    os.makedirs(main_directory, 511, True)

    # Add users file
    file_name = "Users.json"
    fp = os.path.join(main_directory, file_name)  # Used to save your money
    return gp, fp


# Save function
def save(to_save: int) -> None:
    """Function to save the money of the user in the json file."""
    with open(file_path, "r", encoding="utf-8") as rf:
        usrs = json.load(rf)
        try:
            usrs[game_profile]["Money"] = to_save
            with open(file_path, "w", encoding="utf-8") as wf:
                json.dump(usrs, wf, indent=4)
            print()
            print(f"Saved money as: {to_save}$")
        except KeyError:
            print("Money not saved, unknown user!")


game_profile, file_path = get_full_dir()

if os.path.exists(file_path):
    with open(file_path, "r", encoding="utf-8") as read_file:
        print()
        print(f"Hello {game_profile}")
        try:
            users = json.load(read_file)
        except json.decoder.JSONDecodeError:  # If the users file is empty (somehow)
            os.remove(file_path)  # Delete the file
        # IF user does not exist, ask the money question
        try:
            money = users[game_profile]["Money"]
            if money == 0:
                print()
                money = int(input("How much money do u want to start with: "))
                with open(file_path, "w", encoding="utf-8") as write_file:
                    json.dump(users, write_file, indent=4)
        except KeyError:  # Someones has already played but a new user is trying to play
            money = int(input("How much money do u want to start with: "))
            users[game_profile] = {"Money": money}
            with open(file_path, "w", encoding="utf-8") as write_file:
                json.dump(users, write_file, indent=4)
else:
    # New game file
    print(f"Hello {game_profile}")
    print()
    money = int(input("How much money do u want to start with: "))
    data = {game_profile: {"Money": money}}
    with open(file_path, "w", encoding="utf-8") as write_file:
        json.dump(data, write_file, indent=4)

print()
print(f"You are starting with {money}$, have fun!")
sleep(1)
