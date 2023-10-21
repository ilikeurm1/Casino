import time, random, utils

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
    # Winning_Number = Chosen
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
    Winning_Color = utils.HasColor(Winning_Number)
    print(Winning_Number)
    print(Winning_Color)
    Chosen = input(utils.ROULETTE_WELCOME)
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

# Slot machine

def Slots(Money_Bet, Streak, Times_Won):
    slots = [random.randint(1,9), random.randint(1,9), random.randint(1,9)]
    utils.Roll(slots)
    if slots[0] == slots[1] == slots[2]:
        if slots[0] == 7:
            Money_Multiplier = 100
        else:
            Money_Multiplier = 10
    elif slots[0] == slots[1] or slots[1] == slots[2] or slots[0] == slots[2]:
        if (slots[0] != 7 and slots[1] != 7) or (slots[1] != 7 and slots[2] != 7) or (slots[0] != 7 and slots[2] != 7):
            Money_Multiplier = 2
        else:
            Money_Multiplier = 5
    else:
        Money_Multiplier = 0
    if Money_Multiplier != 0:
        Money_Won = Money_Bet * Money_Multiplier
        Streak += 1
        Times_Won += 1
        print("")
        print(f"Nice! The slot machine ended at {slots[0], slots[1], slots[2]} which means you {Money_Multiplier}x your bet ({Money_Bet * Money_Multiplier}$)")
        time.sleep(1)
    else:
        Money_Won = 0
        Streak = 0
        print("")
        print(f"Sorry! The slot machine ended at {slots[0], slots[1], slots[2]} which means you lost your money ({Money_Bet}$), better luck next time!")
        time.sleep(1)
    return Money_Won, Streak, Times_Won
        
