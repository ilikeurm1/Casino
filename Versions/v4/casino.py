"""Main Casino File"""

from time import sleep
import utils
import games
from settings import money, save

streak: int = 0
times_won: int = 0
highest_streak: list[int] = []
highest_winnings: list[int] = []
all_games: list[str] = ["Number Guesser", "Roulette", "Slots", "Blackjack", "Baccarat"]


# Outer game loop
while 1:
    # Inner game loop
    while 1:
        game = input(utils.WELCOME) or "0"

        if "quit" in game:
            break

        if game == "0":
            continue

        if game == all_games[0] or int(game) == 1:
            Chosen_game = games.guesser
            GI = 0

        elif game == all_games[1] or int(game) == 2:
            Chosen_game = games.roulette
            GI = 1

        elif game == all_games[2] or int(game) == 3:
            Chosen_game = games.slots
            GI = 2

        elif game == all_games[3] or int(game) == 4:
            Chosen_game = games.blackjack
            GI = 3

        elif game == all_games[4] or int(game) == 5:
            Chosen_game = games.baccarat
            GI = 4

        # Initialize game

        print()
        print(f"You have chosen to play {all_games[GI]}!")

        money, money_betting = utils.bet(money)
        money_won, streak, times_won = Chosen_game(money_betting, streak, times_won)
        money = money + money_won
        highest_winnings.append(money_won)
        highest_streak.append(streak)

        save(money)

        # LOSE
        if money == 0:
            print(utils.LOST)
            print(utils.bye(highest_streak, highest_winnings, times_won))
            sleep(10)
            utils.clear()
            break

        print()
        print(f"You now have {money}$ and are on a streak of {streak}")

        # Run again
        print()
        again = input("Run again? (y/n): ")
        if "y" in again:
            print("Ok! Clearing terminal for easier view!")
            sleep(2)
            utils.clear()
            continue
        if "n" in again:
            print()
            print(f"When you come back next time you will start with {money}$")
            sleep(2)
            print(utils.bye(highest_streak, highest_winnings, times_won))
            sleep(10)
            utils.clear()
            break
        continue
    break # Just a break for now this will changed to a function that will ask if you want to play again on a new profile...
