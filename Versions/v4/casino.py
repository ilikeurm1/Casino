"""Main Casino File"""

# --> Version 4 Changelog <--
# Added:
# + Added Sleeps to make the game more readable and easier to understand
# + Made the settings file more readable and easier to understand
# + Added obfuscation to the save function (no more cheating by changing the save file, even though you still can lmao)
# + Added colors to the console output
# + Tried making the overal code more readable and easier to understand


# Removed:
# - Pylinted the code (im not going to do this again, it took me ~3 hours) (undo this as i dont care anymore lmfao)

# Importing modules
from games import init_game, guesser, roulette, slots, blackjack, baccarat
from utils import welcome, bet, clear, bye, LOST, run_random_events
from settings import console, Prompt, Confirm, settings_main, save, sleep, is_admin

def main() -> None:
    """Main function."""
    # Outer game loop
    while 1:
        # Initialize the game settings for every new game
        streak: int = 0
        times_won: int = 0
        again: bool = False
        DEBUG: int = 0
        highest_streak: list[int] = []
        highest_winnings: list[int] = []
        all_games: list[str] = [
            "Number Guesser",
            "Roulette",
            "Slots",
            "Blackjack",
            "Baccarat",
        ]
        
        clear()
        
        # Get the user and their money
        money, user = settings_main()

        # Check if the user is an admin
        DEBUG = is_admin(user)
        clear()

        # Inner game loop
        while 1:
            game = Prompt.ask(welcome(user), choices=[str(x) for x in range(1,len(all_games) + 1)] + ["quit"], show_choices=False)

            if not game:
                clear()
                continue

            if "q" in game:
                break

            try:
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

                else:
                    console.print()
                    console.print("[red]Sorry but that isn't a recognized input!")

                gi = int(game) - 1
            except ValueError:
                console.print()
                console.print("[red]That isn't a valid input please input a number or quit!")
                sleep(3)
                clear()
                continue

            # Initialize game

            console.print()
            console.print(f"[blue]You have chosen to play {all_games[gi]}!")

            money, money_betting = bet(money)
            sleep(3)
            money_won, streak, times_won = init_game(chosen_game, money_betting, streak, times_won, DEBUG)
            sleep(5)
            money = money + money_won
            highest_winnings.append(money_won)
            highest_streak.append(streak)

            save(user, money) # Save the users money

            sleep(3)

            # LOSE
            if money == 0:
                console.print(LOST)
                console.print(bye(highest_streak, highest_winnings, times_won))
                sleep(10)
                clear()
                break

            console.print()
            console.print(f"[blue]You now have {money}$ and are on a streak of {streak}")
            
            # Try to run a random event
            run_random_events(user, money)

            # Run again in the current profile
            console.print()
            again = Confirm.ask("[blue]Play a new game?", default=True)
            if again:
                console.print("[blue]Ok! Clearing terminal for easier view!")
                sleep(3)
                clear()
                continue
            elif not again:
                console.print()
                console.print(f"[blue]When you come back next time you will start with {money}$")
                sleep(3)
                console.print(bye(highest_streak, highest_winnings, times_won))
                sleep(5)
                break

        if money == 0: # only ask to restart the game when the person has 0 dollars.
            # Ask to restart the game
            restart = Confirm.ask("[blue]Do you want to restart (on a new profile for example)")
            if restart:
                console.print("[green]Ok! Clearing terminal for easier view!")
                sleep(3)
                clear()
                continue
        console.print("[blue]Thank you for playing! Have a great day!")
        sleep(3)
        break

if __name__ == "__main__":
    main()
