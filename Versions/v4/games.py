"""All the games"""

from time import sleep
import random
import utils
from settings import console

# Disable line too long for the games as the print statements that explain the game are long
# pylint: disable=line-too-long

# Number Guesser
def guesser(money_bet: int, streak: int, times_won: int, DEBUG: bool) -> tuple[int, int, int]:
    """Number Guesser game

    Args:
        money_bet (int): The money the player has bet
        streak (int): The players current streak
        times_won (int): The amount of times the player has won this session

    Returns:
        tuple[int, int, int]: All the updated argument values
    """

    while 1:
        console.print()
        end = int(
            console.input("[green]The game will pick a number from 1 to x, what is x (minimum '5'): [/green]")
        )
        console.print()
        if end < 5:
            console.print("[red]You tried! Please enter a minimum of 5[/red]")
            continue
        break

    winning_number = random.randint(1, end)
    chosen = int(console.input("[green]What number is your guess: [/green]"))
    
    if DEBUG:
        console.print(f"[blue]DEBUG PRINT: The winning number was: {winning_number}[/blue]")
        winning_number = chosen
    
    if winning_number == chosen:
        money_won = money_bet * 2
        streak += 1
        times_won += 1
        console.print()
        console.print(
            f"[blue]Nice! You chose the right number, you have doubled your money bet ({money_won}$)![/blue]"
        )
    else:
        money_won = 0
        streak = 0
        console.print()
        console.print(
            f"[red]Sorry! The correct number was {winning_number} and you chose {chosen}, better luck next time![/red]"
        )

    return money_won, streak, times_won


# Roulette
def roulette(money_bet: int, streak: int, times_won: int, DEBUG: bool) -> tuple[int, int, int]:
    """Roulette game

    Args:
        money_bet (int): The money the player has bet
        streak (int): The players current streak
        times_won (int): The amount of times the player has won this session

    Returns:
        tuple[int, int, int] -- All the updated argument values
    """

    winning_number = random.randint(0, 36)
    winning_color = utils.hascolor(winning_number)
    
    if DEBUG:
        console.print(f"[blue]DEBUG PRINT: The winning number was: {winning_number} this had color: {winning_color}[/blue]")
        winning_number = 0
        winning_color = "g"
    
    chosen = console.input(f"[green]{utils.ROULETTE_WELCOME}[/green]")
    chosen_color = chosen[0].lower()

    sleep(3)
    try:  # A number was chosen
        chosen = int(chosen)  # type: ignore
        if winning_number == 0:  # Multiplier
            money_multiplier = 10
        else:
            money_multiplier = 5
        if chosen == winning_number:
            money_won = money_bet * money_multiplier
            streak += 1
            times_won += 1
            console.print()
            console.print(
                f"[blue]Nice! You chose the right number, you have {money_multiplier}x your money bet ({money_bet * money_multiplier}$)![/blue]"
            )
        else:
            money_won = 0
            streak = 0
            console.print()
            console.print(
                f"[red]Sorry! The correct number was {winning_number} and you chose {chosen}, better luck next time![/red]"
            )

    except ValueError:  # A color was chosen
        if winning_color == "g":  # Multiplier
            money_multiplier = 10
        else:
            money_multiplier = 2

        if chosen_color == winning_color:
            money_won = money_bet * money_multiplier
            streak += 1
            times_won += 1
            console.print()
            console.print(
                f"[blue]Nice! You chose the right color, (the number was: {winning_number}) you have {money_multiplier}x your money bet ({money_bet * money_multiplier}$)![/blue]"
            )
        else:
            money_won = 0
            streak = 0
            console.print()
            console.print(
                f"[red]Sorry! The correct color was {winning_color} (number was: {winning_number}) and you chose {chosen}, better luck next time![/red]"
            )

    return money_won, streak, times_won


# Slot machine
def slots(money_bet: int, streak: int, times_won: int, DEBUG: bool) -> tuple[int, int, int]:
    """Slots game

    Args:
        money_bet (int): The money the player has bet
        streak (int): The players current streak
        times_won (int): The amount of times the player has won this session

    Returns:
        tuple[int, int, int]: All the updated argument values
    """

    slot_machine = [random.randint(1, 9), random.randint(1, 9), random.randint(1, 9)]

    if DEBUG:
        console.print(f"[blue]DEBUG PRINT: The slot machine ended at: {slot_machine}[/blue]")
        slot_machine = [7, 7, 7]
    
    utils.roll(slot_machine)
    if slot_machine[0] == slot_machine[1] == slot_machine[2]:
        if slot_machine[0] == 7:
            money_multiplier = 100
        else:
            money_multiplier = 8
    elif (
        slot_machine[0] == slot_machine[1]
        or slot_machine[1] == slot_machine[2]
        or slot_machine[0] == slot_machine[2]
    ):
        if (
            (slot_machine[0] != 7 and slot_machine[1] != 7)
            or (slot_machine[1] != 7 and slot_machine[2] != 7)
            or (slot_machine[0] != 7 and slot_machine[2] != 7)
        ):
            money_multiplier = 3
        else:
            money_multiplier = 8
    else:
        money_multiplier = 0
    if money_multiplier != 0:
        money_won = money_bet * money_multiplier
        streak += 1
        times_won += 1
        console.print()
        console.print(
            f"[blue]Nice! The slot machine ended at {slot_machine[0], slot_machine[1], slot_machine[2]} which means you {money_multiplier}x your bet ({money_bet * money_multiplier}$)[/blue]"
        )
    else:
        money_won = 0
        streak = 0
        console.print()
        console.print(
            f"[red]Sorry! The slot machine ended at {slot_machine[0], slot_machine[1], slot_machine[2]} which means you lost your money ({money_bet}$), better luck next time![/red]"
        )
    return money_won, streak, times_won


# Blackjack
def blackjack(money_bet: int, streak: int, times_won: int, DEBUG: bool) -> tuple[int, int, int]:
    """Blackjack game

    Args:
        money_bet (int): The money the player has bet
        streak (int): The players current streak
        times_won (int): The amount of times the player has won this session

    Returns:
        tuple[int, int, int]: All the updated argument values
    """

    # Helper func
    def convert_elevens(hand: list[int]) -> list[int]:
        """Converts 11 to 1 if the total score is over 21

        Args:
            hand (list[int]): a hand of cards

        Returns:
            list[int]: the converted hand
        """
        for _ in range(hand.count(11)):
            if sum(hand) > 21:
                hand.remove(11)
                hand.append(1)
        return hand

    # Initialize the player and dealer hands
    player_hand = []
    dealer_hand = []
    player_blackjack = False
    dealer_blackjack = False

    # Deal two cards to the player and dealer

    for _ in range(2):
        player_hand.append(utils.deal_card())
        dealer_hand.append(utils.deal_card())

    if DEBUG:
        player_hand = [11, 10]
        console.print(f"[blue]DEBUG PRINT: Dealer's hand was: {dealer_hand}, Total: {sum(dealer_hand)}[/blue]")
        dealer_hand = [1, 1]

    if sum(player_hand) == 21:
        player_blackjack = True

    if sum(dealer_hand) == 21:
        dealer_blackjack = True

    while sum(player_hand) < 21:
        console.print()
        console.print(f"[blue]Your hand: {player_hand}, Total: {sum(player_hand)}[/blue]")
        console.print()
        console.print(f"[blue]Dealer's hand: [{dealer_hand[0]}, ?][/blue]")
        console.print()
        
        action = console.input("[green]What do you want to do?\n\n1. hit\n2. stand\n\nNumber or action: [/green]").lower()
        if action in ("h", "hit", "1"):
            player_hand.append(utils.deal_card())
            # Convert 11 to 1 if the total score is over 21
            convert_elevens(player_hand)
        elif action in ("s", "stand", "2"):
            break
        else:
            utils.clear()
            continue

        sleep(1)
        utils.clear()

    while sum(dealer_hand) < 17:
        dealer_hand.append(utils.deal_card())
        # Convert 11 to 1 if the total score is over 21
        convert_elevens(dealer_hand)

    console.print()
    console.print(f"[blue]Your hand: {player_hand}, Total: {sum(player_hand)}[/blue]")
    console.print()
    console.print(f"[blue]Dealer's hand: {dealer_hand}, Total: {sum(dealer_hand)}[/blue]")

    if player_blackjack and dealer_blackjack:
        result = "[blue]It's a push (tie). Your bet is returned.[/blue]"
    elif player_blackjack:
        result = "[green]Blackjack! You win![/green]"
    elif dealer_blackjack:
        result = "[red]Dealer has a blackjack. You lose.[/red]"
    elif sum(player_hand) > 21:
        result = "[red]Bust! You lose.[/red]"
    elif sum(dealer_hand) > 21:
        result = "[green]Dealer busts! You win![/green]"
    elif sum(player_hand) > sum(dealer_hand):
        result = "[green]You win![/green]"
    elif sum(player_hand) < sum(dealer_hand):
        result = "[red]You lose.[/red]"
    else:
        result = "[blue]It's a push (tie). Your bet is returned.[/blue]"

    if "Blackjack" in result: # "Blackjack! You win!"
        money_won = money_bet * 10
        streak += 1
        times_won += 1
    elif "win" in result: # "You win!", "Dealer busts! You win!"
        money_won = money_bet * 3
        streak += 1
        times_won += 1
    elif "lose" in result: # "You lose.", "Dealer has a blackjack. You lose.", "Bust! You lose.":
        money_won = 0
        streak = 0
    else:
        money_won = money_bet

    console.print()
    console.print(result)

    return money_won, streak, times_won


# Baccarat
def baccarat(money_bet: int, streak: int, times_won: int, DEBUG: bool) -> tuple[int, int, int]:
    """Baccarat game

    Args:
        money_bet (int): The money the player has bet
        streak (int): The players current streak
        times_won (int): The amount of times the player has won this session

    Returns:
        tuple[int, int, int]: All the updated argument values
    """

    # Determine the point values of the cards
    def card_value(card):
        return card if card <= 10 else 0

    # Generate random cards for the player and banker
    player_cards = []
    banker_cards = []

    for _ in range(2):
        player_cards.append(random.randint(1, 13))
        banker_cards.append(random.randint(1, 13))

    player_points = sum(card_value(card) for card in player_cards) % 10
    banker_points = sum(card_value(card) for card in banker_cards) % 10

    if DEBUG:
        console.print(f"[blue]DEBUG PRINT: Player's hand was: {player_cards}, Total: {player_points}[/blue]")
        player_cards = [8,1]
        banker_cards = [6]

    console.print()
    console.print(f"[blue]Your hand is: {player_cards} Total: {player_points}[/blue]")
    sleep(3)

    # Player's rule
    if player_points <= 5:
        new_card = random.randint(1, 13)
        player_cards.append(new_card)  # Draw a third card
        player_points = sum(card_value(card) for card in player_cards) % 10
        console.print()
        console.print(f"[blue]You drew a third card: {new_card}[/blue]")
        console.print()
        console.print(f"[blue]Your new total is: {player_points}[/blue]")
        sleep(3)

    # Banker's rule
    if len(player_cards) == 2:  # Player stood pat
        if banker_points <= 5:
            banker_cards.append(random.randint(1, 13))  # Draw a third card
            banker_points = sum(card_value(card) for card in banker_cards) % 10
            console.print()
            console.print("[blue]Banker drew a third card.[/blue]")

    else:  # Player drew a third card
        # Additional rules for banker when player drew a third card
        if banker_points <= 2:
            banker_cards.append(random.randint(1, 13))
            console.print()
            console.print("[blue]Banker drew a third card.[/blue]")
        elif banker_points == 3 and player_cards[2] != 8:
            banker_cards.append(random.randint(1, 13))
            console.print()
            console.print("[blue]Banker drew a third card.[/blue]")
        elif banker_points == 4 and player_cards[2] in [2, 3, 4, 5, 6, 7]:
            banker_cards.append(random.randint(1, 13))
            console.print()
            console.print("[blue]Banker drew a third card.[/blue]")
        elif banker_points == 5 and player_cards[2] in [4, 5, 6, 7]:
            banker_cards.append(random.randint(1, 13))
            console.print()
            console.print("[blue]Banker drew a third card.[/blue]")
        elif banker_points == 6 and player_cards[2] in [6, 7]:
            banker_cards.append(random.randint(1, 13))
            console.print()
            console.print("[blue]Banker drew a third card.[/blue]")
    sleep(3)

    banker_points = sum(card_value(card) for card in banker_cards) % 10

    console.print()
    console.print(f"[blue]Your cards are: {player_cards} so your total = {player_points}[/blue]")
    console.print()
    console.print(f"[blue]Bankers cards are: {banker_cards} so their total = {banker_points}[/blue]")
    sleep(3)

    # Determine the winner
    if player_points > banker_points:
        money_won = money_bet * 3
        streak += 1
        times_won += 1
        console.print()
        console.print(
            f"[green]Nice! You won, your bet ({money_bet}$) has been tripled to {money_won}$[/green]"
        )
    elif banker_points > player_points:
        money_won = 0
        streak = 0
        console.print()
        console.print(f"[red]Sorry! You lost, you lost your bet {money_bet}[/red]")
    else:
        money_won = money_bet
        console.print()
        console.print("[blue]Its a tie, you didnt lose any money![/blue]")

    return money_won, streak, times_won


# MAIN INIT FUNCTION
def init_game(game, money_bet: int, streak: int, times_won: int, DEBUG: bool = False) -> tuple[int, int, int]:
    """Inits a game also does some logic

    Args:
        game (function): the game to be played
        money_bet (int): the amount of money the player has bet
        streak (int): the current players streak
        times_won (int): the amount of times the player has won this session
        DEBUG (bool, optional): Admin toggle to get info prints while playing. Defaults to False.

    Returns:
        tuple[int, int, int]: returns the updated values of money_bet, streak and times_won
    """

    console.print()


    return game(money_bet, streak, times_won, DEBUG)



# Main function for testing
def main() -> None:
    """Main function -> for play testing"""
    
    # DEBUG bool
    d: bool = 0 # type: ignore

    # Fake profile setup
    mw: int = 100
    s: int = 100
    t: int = 0

    # Change this to the game you want to test
    game = blackjack

    # Play again
    again: str = "y"

    # Warn print
    console.print(f"[bold red]YOU ARE RUNNING THE GAMES FILE NOT THE MAIN GAME \nTesting game: {game.__name__}\nDebug is set to {d}[/bold red]")

    while "y" in again:
        # Add function to test here
        mw, s, t = init_game(game, mw, s, t, d)
        console.print(f"Money won: {mw} \nStreak: {s} \nTimes won: {t}")
        again = input("Do you want to play again? (y/n): ")
        utils.clear()


if __name__ == "__main__":
    main()
