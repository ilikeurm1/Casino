import time

def Bet(money):
    while True:
        print("")
        Money_Betting = int(input("How much money do you want to bet (Type '0' to go all in): "))
        if Money_Betting == 0:
            Money_Betting = money
       
        if Money_Betting > money:
            print("")
            print("You dont have that much money!!!")
            
        else:
            print("")
            print(f"ok! You are betting {Money_Betting}$")
            break

    Total = money - Money_Betting
    time.sleep(1)
    return Total, Money_Betting

def HasColor(x):
    Red_Numbers = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
    if x == 0:
        Color = "g"
    elif x in Red_Numbers:
        Color = "r"
    else:
        Color = "b"
    return Color

def Roll(Slots):
    print("")
    print(f"{Slots[0]} # #")
    time.sleep(2)
    print("")
    print(f"{Slots[0]} {Slots[1]} #")
    time.sleep(2)
    print("")
    print(f"{Slots[0]} {Slots[1]} {Slots[2]}")
    time.sleep(1)
    


WELCOME = """
What game do you want to play? 

1. Number Guesser | Rewards: 2
2. Roulette | Rewards: 2x (Color) 5x (Number) 10x (Green or 0)
3. Slots | Rewards: 2x (2 of the same) 5x (2x '7') 10x (3 of the same) 100x (3x '7')
       
You may type the name of the game or use the number assigned to it: """



ROULETTE_WELCOME = """What do you guess, pick from:
                   
Numbers: 0 - 36
Colors: Red, Black, Green

Payouts:

0 and Green = 10x your bet
Number (1 - 36) = 5x your bet
Red or Black = 2x your bet

You choose to bet on: """



def BYE(HS, HW, TW):
    return f"""
Good bye!

Thank you for playing!

Credits:

Programming: Matthijs Duhoux
                  
Fun Facts:

Your highest streak was when you won {max(HS)} time(s) in a row

Your highest winning was {max(HW)}$

In total you won {TW} time(s)!
"""



def LOST(HS, HW, TW):
    return f"""
Sorry but you have no money left! You have lost the game! You can start a new game by restarting the program!

Fun Facts:

Your highest streak was when you won {max(HS)} time(s) in a row

Your highest winning was {max(HW)}$

In total you won {TW} time(s)!
"""
