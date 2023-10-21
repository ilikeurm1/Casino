# imports

import time, Utils, Games
from Settings import Money, Save

# Init

Streak = Times_Won = 0
Highest_Streak = []
Highest_Winnings = []
All_Games = ["Number Guesser", "Roulette"]

# Main game loop

while True:
    Game = input(Utils.WELCOME) or 0

    if Game == 0:
        continue
    
    if Game == All_Games[0] or int(Game) == 1:
        Chosen_Game = Games.Guesser
        Game_Index = 0

    elif Game == All_Games[1] or int(Game) == 2:
        Chosen_Game = Games.Roulette
        Game_Index = 1
    print("")
    print(f"You have chosen to play {All_Games[Game_Index]}!")
    Money, Money_Betting = Utils.Bet(Money)
    Money_Won, Streak, Times_Won = Chosen_Game(Money_Betting, Streak, Times_Won)
    Money = Money + Money_Won
    Highest_Winnings.append(Money_Won)
    print("")
    print(f"You now have {Money}$ and are on a streak of {Streak}")
    Highest_Streak.append(Streak)
    Save(Money)

# LOSE
    if Money == 0:
        print(Utils.LOST(Highest_Streak, Highest_Winnings, Times_Won))
        break

# Run again
    print("")
    again = input("Run again? (y/n): ")
    if 'y' in again:
        time.sleep(1)
        continue
    elif 'n' in again:
            print("")
            print(f"When you come back next time you will start with {Money}$")
            time.sleep(2)
            print(Utils.BYE(Highest_Streak, Highest_Winnings, Times_Won))
            break
    else:
            print("Invalid Input, the program will now shut off")
            break
