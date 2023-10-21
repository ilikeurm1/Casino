import time, random, Utils

# Number Guesser

def Guesser(Money_Bet, Streak, Times_Won):
    while True:
        print("")
        End = int(input("The game will pick a number from 1 to x, what is x (minimum '5'): "))
        print("")
        if End < 5:
            print("You tried! Please enter a minimum of 5")
            continue
        else:
            break
    Chosen = int(input("What number is your guess: "))
    Winning_Number = random.randint(1, End)
    if Winning_Number == Chosen:
        Money_Won = Money_Bet * 2
        Streak += 1
        Times_Won += 1
        print("")
        print(f"Nice! You chose the right number, you have doubled your money bet ({Money_Won}$)!")
    else:
        Money_Won = 0
        Streak = 0
        print("")
        print(f"Sorry! The correct number was {Winning_Number} and you chose {Chosen}, better luck next time!")
        time.sleep(1)
    return Money_Won, Streak, Times_Won
        
# Roulette

def Roulette(Money_Bet, Streak, Times_Won):
    Winning_Number = random.randint(0, 36)
    Winning_Color = Utils.HasColor(Winning_Number)
    # print(Winning_Number)
    # print(Winning_Color)
    Chosen = input(Utils.ROULETTE_WELCOME)
    Chosen_Color = Chosen[0].lower()
    time.sleep(1)
    try: # A number was chosen
        Chosen = int(Chosen)
        if Winning_Number == 0: # Multiplier
            Money_Multiplier = 10
        else:
            Money_Multiplier = 5
        if Chosen == Winning_Number:
            Money_Won = Money_Bet * Money_Multiplier
            Streak += 1
            Times_Won += 1
            print("")
            print(f"Nice! You chose the right number, you have {Money_Multiplier}x your money bet ({Money_Bet * Money_Multiplier}$)!")
        else:
            Money_Won = 0
            Streak = 0
            print("")
            print(f"Sorry! The correct number was {Winning_Number} and you chose {Chosen}, better luck next time!")
            time.sleep(1)
    except: # A color was chosen
        if Winning_Color == "g": # Multiplier
            Money_Multiplier = 10
        else:
            Money_Multiplier = 2
        if Chosen_Color == Winning_Color:
            Money_Won = Money_Bet * Money_Multiplier
            Streak += 1
            Times_Won += 1
            print("")
            print(f"Nice! You chose the right color, you have {Money_Multiplier}x your money bet ({Money_Bet * Money_Multiplier}$)!")
            time.sleep(1)
        else:
            Money_Won = 0
            Streak = 0
            print("")
            print(f"Sorry! The correct color was {Winning_Color} and you chose {Chosen}, better luck next time!")
            time.sleep(1)
    
    return Money_Won, Streak, Times_Won
