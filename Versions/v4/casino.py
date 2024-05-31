"""Main Casino File"""

# --> Version 4 Changelog <--
# Pylinted the code (im not going to do this again, it took me ~3 hours)
# Added Sleeps to make the game more readable and easier to understand
# Made the settings file more readable and easier to understand
# Added obfuscation to the save function (no more cheating by changing the save file)

from time import sleep
import games
from utils import welcome, bet, clear, bye, LOST
from settings import settings_main, save


def main() -> None:
    """Main function."""
    # Outer game loop
    while 1:
        # Initialize the game settings for every new game
        streak: int = 0
        times_won: int = 0
        again: str = ""
        highest_streak: list[int] = []
        highest_winnings: list[int] = []
        all_games: list[str] = [
            "Number Guesser",
            "Roulette",
            "Slots",
            "Blackjack",
            "Baccarat",
        ]

        money, user = settings_main() # Get the user and their money
        # Inner game loop
        while 1:
            game = input(welcome(user))

            if not game:
                clear()
                continue

            if "q" in game:
                break

            try:
                if int(game) == 1:
                    chosen_game = games.guesser

                elif int(game) == 2:
                    chosen_game = games.roulette

                elif int(game) == 3:
                    chosen_game = games.slots

                elif int(game) == 4:
                    chosen_game = games.blackjack

                elif int(game) == 5:
                    chosen_game = games.baccarat

                else:
                    print()
                    print("Sorry but that isn't a recognized input!")

                gi = int(game) - 1
            except ValueError:
                print()
                print("That isn't a valid input please input a number or quit!")
                sleep(3)
                clear()
                continue

            # Initialize game

            print()
            print(f"You have chosen to play {all_games[gi]}!")

            money, money_betting = bet(money)
            sleep(3)
            clear()
            money_won, streak, times_won = chosen_game(money_betting, streak, times_won)
            sleep(5)
            money = money + money_won
            highest_winnings.append(money_won)
            highest_streak.append(streak)

            save(money, user)

            sleep(3)
            clear()

            # LOSE
            if money == 0:
                print(LOST)
                print(bye(highest_streak, highest_winnings, times_won))
                sleep(10)
                clear()
                break

            print()
            print(f"You now have {money}$ and are on a streak of {streak}")

            # Run again in the current profile
            print()
            again = input("Play a new game? (y/n): ")
            if "y" in again:
                print("Ok! Clearing terminal for easier view!")
                sleep(3)
                clear()
                continue
            if "n" in again:
                print()
                print(f"When you come back next time you will start with {money}$")
                sleep(3)
                print(bye(highest_streak, highest_winnings, times_won))
                sleep(10)
                clear()
                break
            continue

        if "n" not in again: # only ask to restart the game when the person has 0 dollars.
            # Restart the game
            restart = input("Do you want to restart (on a new profile)? (y/n): ")
            if "y" in restart:
                print("Ok! Clearing terminal for easier view!")
                sleep(3)
                clear()
                continue
        print("Thank you for playing! Have a great day!")
        sleep(3)
        clear()
        break


if __name__ == "__main__":
    main()
