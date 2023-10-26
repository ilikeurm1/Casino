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

# Slot machine

def Slots(Money_Bet, Streak, Times_Won):
    slots = [random.randint(1,9), random.randint(1,9), random.randint(1,9)]
    # slots = [7, 7, 7]
    Utils.Roll(slots)
    if slots[0] == slots[1] == slots[2]:
        if slots[0] == 7:
            Money_Multiplier = 100
        else:
            Money_Multiplier = 8
    elif slots[0] == slots[1] or slots[1] == slots[2] or slots[0] == slots[2]:
        if (slots[0] != 7 and slots[1] != 7) or (slots[1] != 7 and slots[2] != 7) or (slots[0] != 7 and slots[2] != 7):
            Money_Multiplier = 3
        else:
            Money_Multiplier = 8
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

# Blackjack

def Blackjack(Money_Bet, Streak, Times_Won):

    while True:
        player_hand = []
        dealer_hand = []
        player_score = 0
        dealer_score = 0
        player_blackjack = False
        dealer_blackjack = False

        # Deal two cards to the player and dealer

        for _ in range(2):
            player_hand.append(Utils.deal_card())
            dealer_hand.append(Utils.deal_card())

        if sum(player_hand) == 21 and len(player_hand) == 2:
            player_blackjack = True

        if sum(dealer_hand) == 21 and len(dealer_hand) == 2:
            dealer_blackjack = True

        while sum(player_hand) < 21:
            print("")
            print(f"Your hand: {player_hand}, Total: {sum(player_hand)}")
            print("") 
            print(f"Dealer's hand: [{dealer_hand[0]}, ?]")
            # print(f"Dealer's hand: {dealer_hand}, Total: {sum(dealer_hand)}")
            print("")

            action = input("Do you want to 'hit' or 'stand'? ").lower()
            if action == "hit":
                player_hand.append(Utils.deal_card())
                # Convert 11 to 1 if the total score is over 21
                if 11 in player_hand and sum(player_hand) > 21:
                    player_hand.remove(11)
                    player_hand.append(1)
            elif action == "stand":
                break

        while sum(dealer_hand) < 17:
            dealer_hand.append(Utils.deal_card())
            # Convert 11 to 1 if the total score is over 21
            if 11 in dealer_hand and sum(dealer_hand) > 21:
                dealer_hand.remove(11)
                dealer_hand.append(1)

        player_score = sum(player_hand)
        dealer_score = sum(dealer_hand)

        print("") 
        print(f"Your hand: {player_hand}")
        print("") 
        print(f"Dealer's hand: {dealer_hand}")

        if player_blackjack and dealer_blackjack:
            result = "It's a push (tie). Your bet is returned."
        elif player_blackjack:
            result = "Blackjack! You win!"
        elif dealer_blackjack:
            result = "Dealer has a blackjack. You lose."
        elif player_score > 21:
            result = "Bust! You lose."
        elif dealer_score > 21:
            result = "Dealer busts! You win!"
        elif player_score > dealer_score:
            result = "You win!"
        elif player_score < dealer_score:
            result = "You lose."
        else:
            result = "It's a push (tie). Your bet is returned."

        if "Blackjack" in result: # result == "You win!" or result == "Blackjack! You win!" or result == "Dealer busts! You win!":
            Money_Won = Money_Bet * 10
            Streak += 1
            Times_Won += 1
        elif "win" in result:
            Money_Won = Money_Bet * 3
            Streak += 1
            Times_Won += 1
        elif "lose" in result: # result == "You lose." or result == "Dealer has a blackjack. You lose." or result == "Bust! You lose.":
            Money_Won = 0
            Streak = 0
        else:
            Money_Won = Money_Bet

        print("") 
        print(result)

        break

    return Money_Won, Streak, Times_Won
