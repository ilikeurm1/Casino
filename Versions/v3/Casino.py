# imports

import Utils, Games
from Settings import Money, Save
from time import sleep

# Init

Streak = Times_Won = 0
Highest_Streak = []
Highest_Winnings = []
All_Games = ["Number Guesser", "Roulette", "Slots", "Blackjack", "Baccarat"]

# Main game loop

while True:
    Game = input(Utils.WELCOME) or 0

    if "q" in Game:
        break

    elif Game == 0:
        continue
    
    elif Game == All_Games[0] or int(Game) == 1:
        Chosen_Game = Games.Guesser
        Game_Index = 0

    elif Game == All_Games[1] or int(Game) == 2:
        Chosen_Game = Games.Roulette
        Game_Index = 1

    elif Game == All_Games[2] or int(Game) == 3:
         Chosen_Game = Games.Slots
         Game_Index = 2
    
    elif Game == All_Games[3] or int(Game) == 4:
         Chosen_Game = Games.Blackjack
         Game_Index = 3
    
    elif Game == All_Games[4] or int(Game) == 5:
        Chosen_Game = Games.Baccarat
        Game_Index = 4

    # Initialize game

    print()
    print(f"You have chosen to play {All_Games[Game_Index]}!")
    
    Money, Money_Betting = Utils.Bet(Money)
    Money_Won, Streak, Times_Won = Chosen_Game(Money_Betting, Streak, Times_Won)
    Money = Money + Money_Won
    Highest_Winnings.append(Money_Won)
    Highest_Streak.append(Streak)
        
    Save(Money)

    # LOSE
    if Money == 0:
        print(Utils.LOST())
        print(Utils.BYE(Highest_Streak, Highest_Winnings, Times_Won))
        sleep(10)
        Utils.clear()
        break

    print()
    print(f"You now have {Money}$ and are on a streak of {Streak}")
    

    # Run again
    print()
    again = input("Run again? (y/n): ")
    if 'y' in again:
        print("Ok! Clearing terminal for easier view!")
        sleep(2)
        Utils.clear()
        continue
    elif 'n' in again:
        print()
        print(f"When you come back next time you will start with {Money}$")
        sleep(2)
        print(Utils.BYE(Highest_Streak, Highest_Winnings, Times_Won))
        sleep(10)
        Utils.clear()
        break
    else:
        continue
    