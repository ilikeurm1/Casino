"""Main Casino File"""

# --> Version 4 Changelog <--
# Added:
# + Added Sleeps to make the game more readable and easier to understand
# + Made the settings file more readable and easier to understand
# + Added obfuscation to the save function (no more cheating by changing the save file, even though you still can lmao)
# + Added colors to the console output
# + Tried making the overal code more readable and easier to understand
# + Events that can happen randomly

# Removed:
# - Pylinted the code (im not going to do this again, it took me ~3 hours) (undoing this as i dont care anymore lmfao)

# region Imports

from settings import (
    # 3rd party
    sleep, # time
    console, Prompt, Confirm, # rich
    # Self-made
    settings_main,
    save,
    is_admin
    )

from utils import (
    # Funcs
    clear,
    bet,
    # Strings
    welcome,
    bye,
    LOST,
    )

from games import (
    # Well... the games
    init_game,
    guesser,
    roulette,
    slots,
    blackjack,
    baccarat,
    # Consts
    AMOUNT_OF_GAMES
    )

from events import run_random_event

# endregion

# region main

def main() -> None:
    """The casino..."""
    # Outer game loop
    while 1:
        # Initialize the game vars
        again: bool = False
        streak: int = 0
        times_won: int = 0
        DEBUG: int = 0
        highest_streak: list[int] = []
        earnings: list[int] = []

        clear()

        # Get the user and their money
        money, user = settings_main()

        # Check if the user is an admin
        DEBUG = is_admin(user)

        sleep(3)
        clear()

        # Inner game loop
        while 1: # While the user is playing
            # Ask which game the user wants to play (allow the empty string for code below)
            game = Prompt.ask(welcome(user), choices=[str(x) for x in range(1, AMOUNT_OF_GAMES + 1)] + ["quit", ""], show_choices=False)

            # If they press enter on accident clear the screen as it can get crowded
            if not game:
                clear()
                continue

            # If the user types quit, quit the game
            if game == "quit":
                break

            # Match the users input to the according game (don't need to try since Prompt takes care of verification)
            if game == "1":
                chosen_game = guesser

            elif game == "2":
                chosen_game = roulette

            elif game == "3":
                chosen_game = slots

            elif game == "4":
                chosen_game = blackjack

            elif game == "5":
                chosen_game = baccarat

            # Conformation print
            console.print()
            console.print(f"[blue]You have chosen to play {chosen_game.__name__}!")

            # Initialization process
            # Get the users bet
            money, money_betting = bet(money)
            sleep(3)
            # Initialize a game
            money_won, streak, times_won = init_game(chosen_game, money_betting, streak, times_won, DEBUG)
            sleep(5)
            # Add the money won to the users money
            money += money_won
            # Add the the players earnings and streak to corresponding the lists
            earnings.append(money_won)
            highest_streak.append(streak)

            # Try to run a random event
            money = run_random_event(user, money, DEBUG)

            # Save the users money
            save(user, money) # Save the users money

            sleep(3)

            # If the person lost (the persons money == 0)
            if money == 0:
                console.print(LOST) # Print the lost string
                console.print(bye(highest_streak, earnings, times_won)) # Print the bye string
                sleep(10) # Give the person enough time to read the paragraphs that are these strings
                clear() # Clear cuz why not
                break # Stop the casino to ask for a restart or quit

            # Otherwise continue with the game
            console.print()
            console.print(f"[blue]You now have {money}$ and are on a streak of {streak}")


            # Ask to run again in the current profile
            console.print()
            again = Confirm.ask("[blue]Play a new game?", default=True)
            if again:
                console.print("[blue]Ok! Clearing terminal for easier view!")
                sleep(3)
                clear()
                continue
            else: # Have the else here for readability (I know it's not needed)
                console.print()
                console.print(f"[blue]When you come back next time you will start with {money}$")
                sleep(3)
                console.print(bye(highest_streak, earnings, times_won))
                sleep(5)
                break

        # Only ask to restart the game when the person has 0 dollars
        if money == 0: # As if they don't but they got to this code they said no when asked to play a new game
            # Ask to restart the game
            restart = Confirm.ask("[blue]Do you want to restart (on a new profile for example)")
            if restart:
                console.print("[green]Ok! Clearing terminal for easier view!")
                sleep(3)
                clear()
                continue

        console.print("[blue]Thank you for playing! Have a great day!")
        sleep(5)
        break

if __name__ == "__main__":
    try:
        main()
        console.print("[green]Program exited successfully\nexit code: 0")

    except Exception as e:
        console.print(f"[red]An error occurred: {e}\nexit code: you choose lmao 1 ig?")

# endregion
