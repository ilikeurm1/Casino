import random, Utils
from time import sleep

# Number Guesser

def Guesser(Money_Bet, Streak, Times_Won):
    while True:
        print()
        End = int(input("The game will pick a number from 1 to x, what is x (minimum '5'): "))
        print()
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
        print()
        print(f"Nice! You chose the right number, you have doubled your money bet ({Money_Won}$)!")
    else:
        Money_Won = 0
        Streak = 0
        print()
        print(f"Sorry! The correct number was {Winning_Number} and you chose {Chosen}, better luck next time!")
        sleep(1)
    return Money_Won, Streak, Times_Won
        
# Roulette

def Roulette(Money_Bet, Streak, Times_Won):
    Winning_Number = random.randint(0, 36)
    Winning_Color = Utils.HasColor(Winning_Number)
    # print(Winning_Number)
    # print(Winning_Color)
    Chosen = input(Utils.ROULETTE_WELCOME)
    Chosen_Color = Chosen[0].lower()
    
    sleep(1)
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
            print()
            print(f"Nice! You chose the right number, you have {Money_Multiplier}x your money bet ({Money_Bet * Money_Multiplier}$)!")
        else:
            Money_Won = 0
            Streak = 0
            print()
            print(f"Sorry! The correct number was {Winning_Number} and you chose {Chosen}, better luck next time!")
            sleep(1)

    except: # A color was chosen
        if Winning_Color == "g": # Multiplier
            Money_Multiplier = 10
        else:
            Money_Multiplier = 2

        if Chosen_Color == Winning_Color:
            Money_Won = Money_Bet * Money_Multiplier
            Streak += 1
            Times_Won += 1
            print()
            print(f"Nice! You chose the right color, you have {Money_Multiplier}x your money bet ({Money_Bet * Money_Multiplier}$)!")
            sleep(1)
        else:
            Money_Won = 0
            Streak = 0
            print()
            print(f"Sorry! The correct color was {Winning_Color} and you chose {Chosen}, better luck next time!")
            sleep(1)
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
        print()
        print(f"Nice! The slot machine ended at {slots[0], slots[1], slots[2]} which means you {Money_Multiplier}x your bet ({Money_Bet * Money_Multiplier}$)")
        sleep(1)
    else:
        Money_Won = 0
        Streak = 0
        print()
        print(f"Sorry! The slot machine ended at {slots[0], slots[1], slots[2]} which means you lost your money ({Money_Bet}$), better luck next time!")
        sleep(1)
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
            print()
            print(f"Your hand: {player_hand}, Total: {sum(player_hand)}")
            print() 
            print(f"Dealer's hand: [{dealer_hand[0]}, ?]")
            # print(f"Dealer's hand: {dealer_hand}, Total: {sum(dealer_hand)}")
            print()

            action = input("Do you want to 'hit' or 'stand'? ").lower()
            if action == "hit":
                player_hand.append(Utils.deal_card())
                # Convert 11 to 1 if the total score is over 21
                if 11 in player_hand and sum(player_hand) > 21:
                    player_hand.remove(11)
                    player_hand.append(1)
            elif action == "stand":
                break

        # Convert 11 to 1 if the total score is over 21
        if 11 in dealer_hand and sum(dealer_hand) > 21:
            dealer_hand.remove(11)
            dealer_hand.append(1)

        while sum(dealer_hand) < 17:
            dealer_hand.append(Utils.deal_card())
            # Convert 11 to 1 if the total score is over 21
            if 11 in dealer_hand and sum(dealer_hand) > 21:
                dealer_hand.remove(11)
                dealer_hand.append(1)

        player_score = sum(player_hand)
        dealer_score = sum(dealer_hand)

        print() 
        print(f"Your hand: {player_hand}, Total: {sum(player_hand)}")
        print() 
        print(f"Dealer's hand: {dealer_hand}, Total: {sum(dealer_hand)}")

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

        print() 
        print(result)

        break

    return Money_Won, Streak, Times_Won

# Baccarat

import random

def Baccarat(Money_Bet, Streak, Times_Won):
    
    # Determine the point values of the cards
    def card_value(card):
        return card if card <= 10 else 0
    
    # Generate random cards for the player and banker
    player_cards = []
    banker_cards = []

    for x in range(2):
        player_cards.append(random.randint(1, 13))
        banker_cards.append(random.randint(1, 13))

    player_points = sum(card_value(card) for card in player_cards) % 10
    banker_points = sum(card_value(card) for card in banker_cards) % 10
        
    print()
    print(f"Your hand is: {player_cards}")
    print()
    print(f"Your total is: {player_points}")
    sleep(2)

    # Player's rule
    if player_points <= 5:
        new_card = random.randint(1, 13)
        player_cards.append(new_card)  # Draw a third card
        player_points = sum(card_value(card) for card in player_cards) % 10
        print()
        print(f"You drew a third card: {new_card}")
        print()
        print(f"Your new total is: {player_points}")
        sleep(2)

    # Banker's rule
    if len(player_cards) == 2:  # Player stood pat
        if banker_points <= 5:
            banker_cards.append(random.randint(1, 13))  # Draw a third card
            banker_points = sum(card_value(card) for card in banker_cards) % 10
            print()
            print("Banker drew a third card.")
            sleep(2)

    else:  # Player drew a third card
        # Additional rules for banker when player drew a third card
        if banker_points <= 2:
            banker_cards.append(random.randint(1, 13))
            print()
            print("Banker drew a third card.")
            sleep(2)
        elif banker_points == 3 and player_cards[2] != 8:
            banker_cards.append(random.randint(1, 13))
            print()
            print("Banker drew a third card.")
            sleep(2)
        elif banker_points == 4 and player_cards[2] in [2, 3, 4, 5, 6, 7]:
            banker_cards.append(random.randint(1, 13))
            print()
            print("Banker drew a third card.")
            sleep(2)
        elif banker_points == 5 and player_cards[2] in [4, 5, 6, 7]:
            banker_cards.append(random.randint(1, 13))
            print()
            print("Banker drew a third card.")
            sleep(2)
        elif banker_points == 6 and player_cards[2] in [6, 7]:
            banker_cards.append(random.randint(1, 13)())
            print()
            print("Banker drew a third card.")
            sleep(2)

    banker_points = sum(card_value(card) for card in banker_cards) % 10

    print()
    print(f"Your cards are: {player_cards} so your total = {player_points}")
    print()
    print(f"Bankers cards are: {banker_cards} so their total = {banker_points}")
    sleep(2)

    
    # Determine the winner
    if player_points > banker_points:
        Money_Won = Money_Bet * 3 
        Streak += 1  
        Times_Won += 1  
        print()
        print(f"Wow! You won, your bet ({Money_Bet}$) has been tripled to {Money_Won}$")
        sleep(2)
    elif banker_points > player_points:
        Money_Won = 0
        Streak = 0 
        print()
        print(f"Sorry! You lost, you lost your bet {Money_Bet}")
        sleep(2)
    else:
        Money_Won = Money_Bet
        print()
        print("Its a tie, you didnt lose any money!")
        sleep(2)

    return Money_Won, Streak, Times_Won
