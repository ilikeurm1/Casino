"""All the games"""

# region Imports

from settings import (
    # 3rd party
    # os, # os
    sleep, # time
    randint, # random
    console, Prompt, IntPrompt, Confirm, # rich
    # Self-made
    # Consts
    USE_SOUND,
    )

from utils import (
    # Funcs
    clear,
    bet,
    deal_card,
    hascolor,
    find_duplicates,
    roll_anim,
    play_sound,
    DEBUG_GAME,
    # Strings
    ROULETTE_WELCOME,
    )

# endregion

# Consts to keep track of amount of games
AMOUNT_OF_GAMES = 5

# region Games

# Number Guesser
def guesser(money_bet: int, DEBUG: int) -> int:
    """Number Guesser game

    Args:
        money_bet (int): The money the player has bet
        DEBUG (int): debug level of user

    Returns:
        money_won (int): The money the user won
    """
    # While the input isn't above 5
    while 1:
        end = IntPrompt.ask(
            "[green]The game will pick a number from [b]1[/b] to [b]x[/b], what is x (minimum '5')",
            default=5,
        )
        console.print()
        if end < 5:
            console.print("[prompt.invalid]:pile_of_poo: number must be atleast 5")
            continue
        break

    # Generate the winning number
    winning_number = randint(1, end)
    # Ask the user for a number
    chosen = IntPrompt.ask(
        "[green]What number is your guess",
        choices=[str(x) for x in range(1, end + 1)],
        show_choices=False,
    )

    # Debug stuff
    if DEBUG:
        data = {
            "chosen": chosen,
            "winning_number": winning_number,
        }
        chosen, winning_number = DEBUG_GAME(DEBUG, "guesser", data)

    # Winning logic
    if winning_number == chosen:
        money_won = money_bet * 2
        console.print()
        console.print(f"[blue]Nice! You chose the right number, you have doubled your money bet ({money_won}$)!")
    else:
        money_won = 0
        console.print()
        console.print(
            f"[red]Sorry! The correct number was {winning_number} and you chose {chosen}, better luck next time!"
        )

    return money_won

# Roulette
def roulette(money_bet: int, DEBUG: int) -> int:
    """Roulette game

    Args:
        money_bet (int): The money the player has bet
        DEBUG (int): debug level of user

    Returns:
        money_won (int): The money the user won
    """

    # Define the color names:
    color_names = {
        "r": "red",
        "b": "black",
        "g": "green"
    }

    # Generate a random number and get the color of that number
    winning_number = randint(0, 36)
    winning_color = hascolor(winning_number)

    # Ask the user for a number or color
    chosen_number = Prompt.ask(
        ROULETTE_WELCOME,
        choices=[str(x) for x in range(37)] + ["red", "green", "black", "r", "g", "b"],
        show_choices=False,
    )
    chosen_color = chosen_number[0].lower()

    # Debug stuff
    if DEBUG:
        data = {
            "chosen_number": chosen_number,
            "chosen_color": chosen_color,
            "winning_number": winning_number,
            "winning_color": winning_color,
        }
        chosen_number, chosen_color, winning_number, winning_color = DEBUG_GAME(
            DEBUG, "roulette", data
        )

    sleep(2)

    # Winning logic
    try:  # A number was chosen
        chosen_number = int(chosen_number)  # type: ignore
        if chosen_number == winning_number:
            # Multiplier logic
            if winning_number == 0:
                money_multiplier = 10
            else:
                money_multiplier = 5

            money_won = money_bet * money_multiplier
            console.print()
            console.print(
                f"[blue]Nice! You chose the right number, you have {money_multiplier}x your money bet ({money_bet * money_multiplier}$)!"
            )
        else:
            money_won = 0
            console.print()
            console.print(
                f"[red]Sorry! The correct number was {winning_number} and you chose {chosen_number}, better luck next time!"
            )

    except ValueError:  # A color was chosen
        if winning_color == "g":  # Multiplier
            money_multiplier = 10
        else:
            money_multiplier = 2

        if chosen_color == winning_color:
            money_won = money_bet * money_multiplier
            console.print()
            console.print(
                f"[blue]Nice! You chose the right color ({winning_color}), (the number was: {winning_number}) you have {money_multiplier}x your money bet ({money_bet * money_multiplier}$)!"
            )
        else:
            money_won = 0
            console.print()
            console.print(
                f"[red]Sorry! The correct color was {color_names[winning_color]} (number was: {winning_number}) and you chose {color_names[chosen_color]}, better luck next time!"
            )

    return money_won

# Slot machine
def slots(money_bet: int, DEBUG: int) -> int:
    """Slots game

    Args:
        money_bet (int): The money the player has bet
        DEBUG (int): debug level of user

    Returns:
        money_won (int): The money the user won
    """

    # Generate a slotmachine
    slot_machine = [randint(1, 9), randint(1, 9), randint(1, 9)]

    # Debug stuff
    if DEBUG:
        data = {
            "slot_machine": slot_machine,
        }
        slot_machine = list(DEBUG_GAME(DEBUG, "slots", data))

    # Do the roll animation
    roll_anim(slot_machine)

    # Winning logic
    if slot_machine[0] == slot_machine[1] == slot_machine[2]:  # All the same
        # Play the winning sound
        if USE_SOUND:
            play_sound("slotmachine", .5, True)

        if slot_machine[0] == 7:  # All sevens
            money_multiplier = 100
        else:  # Other numbers
            money_multiplier = 8
    # Two of the same
    elif len(set(slot_machine)) == 2:  # Two the same
        if find_duplicates(slot_machine) == 7:  # Two sevens
            money_multiplier = 8
        else:
            money_multiplier = 3  # Other numbers

    else:
        money_multiplier = 0  # Nothing is the same

    if money_multiplier != 0:
        money_won = money_bet * money_multiplier
        console.print()
        console.print(
            f"[blue]Nice! The slot machine ended at {slot_machine[0], slot_machine[1], slot_machine[2]} which means you {money_multiplier}x your bet ({money_bet * money_multiplier}$)"
        )
    else:
        money_won = 0
        console.print()
        console.print(
            f"[red]Sorry! The slot machine ended at {slot_machine[0], slot_machine[1], slot_machine[2]} which means you lost your money ({money_bet}$), better luck next time!"
        )

    return money_won

# Blackjack
def blackjack(money_bet: int, DEBUG: int) -> int:
    """Blackjack game

    Args:
        money_bet (int): The money the player has bet
        DEBUG (int): debug level of user

    Returns:
        money_won (int): The money the user won
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
        player_hand.append(deal_card())
        dealer_hand.append(deal_card())

    # Debug stuff
    if DEBUG:
        data = {
            "player_hand": player_hand,
            "dealer_hand": dealer_hand,
        }
        player_hand, dealer_hand = DEBUG_GAME(DEBUG, "blackjack", data)

    # See if anyone has blackjack
    if sum(player_hand) == 21:
        player_blackjack = True

    if sum(dealer_hand) == 21:
        dealer_blackjack = True

    # Check if neither has blackjack
    if not player_blackjack and not dealer_blackjack:
        # Players turn
        while sum(player_hand) < 21:
            console.print(f"[blue]Your hand: {player_hand}, Total: {sum(player_hand)}")
            console.print()
            console.print(f"[blue]Dealer's hand: [{dealer_hand[0]}, ?]")
            console.print()

            # Ask the person what action they want to do
            action = Prompt.ask(
                "[green]What do you want to do?\n\n1. hit\n2. stand\n\nNumber or action",
                choices=["1", "2", "hit", "stand", "h", "s"],
                show_choices=False
            ).lower()
            # If the player hits give them a card
            if action in ("h", "hit", "1"):
                player_hand.append(deal_card())
                # Convert 11 to 1 if the total score is over 21
                convert_elevens(player_hand)
            # Otherwise break the loop
            elif action in ("s", "stand", "2"):
                break

            sleep(2)
            clear()

        # Dealer's turn
        while sum(dealer_hand) < 17:
            dealer_hand.append(deal_card())
            # Convert 11 to 1 if the total score is over 21
            convert_elevens(dealer_hand)

    console.print()
    console.print(f"[blue]Your hand: {player_hand}, Total: {sum(player_hand)}")
    console.print()
    console.print(f"[blue]Dealer's hand: {dealer_hand}, Total: {sum(dealer_hand)}")

    # Make the result string
    if player_blackjack and dealer_blackjack:
        result = "[blue]It's a push (tie). Your bet is returned."
    elif player_blackjack:
        result = "[green]Blackjack! You win!"
    elif dealer_blackjack:
        result = "[red]Dealer has a blackjack. You lose."
    elif sum(player_hand) > 21:
        result = "[red]Bust! You lose."
    elif sum(dealer_hand) > 21:
        result = "[green]Dealer busts! You win!"
    elif sum(player_hand) > sum(dealer_hand):
        result = "[green]You win!"
    elif sum(player_hand) < sum(dealer_hand):
        result = "[red]You lose."
    else:
        result = "[blue]It's a push (tie). Your bet is returned."

    # Winning logic
    if "Blackjack" in result:  # "Blackjack! You win!"
        money_won = money_bet * 10
    elif "win" in result:  # "You win!", "Dealer busts! You win!"
        money_won = money_bet * 3

    elif ("lose" in result):  # "You lose.", "Dealer has a blackjack. You lose.", "Bust! You lose.":
        money_won = 0
    else:
        money_won = money_bet # "It's a push (tie). Your bet is returned."

    console.print()
    console.print(result)

    return money_won

# Baccarat
def baccarat(money_bet: int, DEBUG: int) -> int:
    """Baccarat game

    Args:
        money_bet (int): The money the player has bet
        DEBUG (int): debug level of user

    Returns:
        money_won (int): The money the user won
    """

    # Determine the point values of the cards
    def card_value(card):
        return card if card <= 10 else 0

    # Initialize the banker and players hand
    player_hand = []
    banker_hand = []

    # Give the player and banker random cards
    for _ in range(2):
        player_hand.append(randint(1, 13))
        banker_hand.append(randint(1, 13))

    # Calculate each players points
    player_points = sum(card_value(card) for card in player_hand) % 10
    banker_points = sum(card_value(card) for card in banker_hand) % 10

    # Debug stuff
    if DEBUG:
        data = {
            "player_hand": player_hand,
            "banker_hand": banker_hand,
        }
        player_hand, banker_hand = DEBUG_GAME(DEBUG, "baccarat", data)

    console.print(f"[blue]Your hand is: {player_hand} Total: {player_points}")
    sleep(3)

    # Player's rule
    if player_points <= 5:
        player_hand.append(randint(1, 13))  # Draw a third card
        player_points = sum(card_value(card) for card in player_hand) % 10
        console.print()
        console.print(f"[blue]You drew a third card: {player_hand[2]}")
        console.print()
        console.print(f"[blue]Your new total is: {player_points}")
        sleep(3)

    # Banker's rule
    if len(player_hand) == 2:  # Player stood pat (didn't get a third card)
        if banker_points <= 5:
            banker_hand.append(randint(1, 13))  # Draw a third card
            banker_points = sum(card_value(card) for card in banker_hand) % 10
            console.print()
            console.print("[blue]Banker drew a third card.")

    else:  # Player drew a third card
        # Additional rules for banker when player drew a third card
        if banker_points <= 2:
            banker_hand.append(randint(1, 13))
            console.print()
            console.print("[blue]Banker drew a third card.")
        elif banker_points == 3 and player_hand[2] != 8:
            banker_hand.append(randint(1, 13))
            console.print()
            console.print("[blue]Banker drew a third card.")
        elif banker_points == 4 and player_hand[2] in [2, 3, 4, 5, 6, 7]:
            banker_hand.append(randint(1, 13))
            console.print()
            console.print("[blue]Banker drew a third card.")
        elif banker_points == 5 and player_hand[2] in [4, 5, 6, 7]:
            banker_hand.append(randint(1, 13))
            console.print()
            console.print("[blue]Banker drew a third card.")
        elif banker_points == 6 and player_hand[2] in [6, 7]:
            banker_hand.append(randint(1, 13))
            console.print()
            console.print("[blue]Banker drew a third card.")
    sleep(3)

    banker_points = sum(card_value(card) for card in banker_hand) % 10

    console.print()
    console.print(
        f"[blue]Your cards are: {player_hand} so your total = {player_points}"
    )
    console.print()
    console.print(
        f"[blue]Bankers cards are: {banker_hand} so their total = {banker_points}"
    )
    sleep(3)

    # Winning logic
    if player_points > banker_points:
        money_won = money_bet * 3
        console.print()
        console.print(
            f"[green]Nice! You won, your bet ({money_bet}$) has been tripled to {money_won}$"
        )
    elif banker_points != player_points:
        money_won = 0
        console.print()
        console.print(f"[red]Sorry! You lost, you lost your bet {money_bet}")
    else:
        money_won = money_bet
        console.print()
        console.print("[blue]Its a tie, you didnt lose any money!")

    return money_won

# Game init function
def init_game(
    game, money: int, tw: int, cur_s: int, max_s: int, max_earn: int, DEBUG: int
    ) -> tuple[int, int, int, int, int]:
    """Inits a game also does some logic

    Args:
        game (function): The game function that the user chose
        money (int): The users money
        tw (int): The amount of times the users has won
        cur_s (int): The users current streak
        max_s (int): The users highest streak
        max_earn (int): The maximum amount of money the user has earned in one game
        DEBUG (int): DEBUG LVL

    Returns:
        tuple[int, int, int, int, int]: Accordingly updated values in format
        t: money, times_won, streak, max_s, max_earn
    """

    # Get the users bet
    money, money_betting = bet(money)

    sleep(3)
    
    # Section for the game
    console.print()
    console.print("--------------- GAME ---------------", style="bold rgb(191,84,8)")
    console.print()

    # Initialize a game
    money_won = game(money_betting, DEBUG)

    # Add the money won to the users money
    money += money_won

    # Update all the variables accordingly

    # If the user won nothing
    if money_won == 0:
        cur_s = 0

    # The user won money
    elif money_won != money_betting:
        cur_s += 1
        tw += 1
        # See if the user has a new highscore
        max_earn = money_won if money_won > max_earn else max_earn
        max_s = cur_s if cur_s > max_s else max_s


    return money, tw, cur_s, max_s, max_earn

# endregion

# region TESTING

# Main function for testing
def main() -> None:
    """Main function -> for play testing"""

    # DEBUG bool
    d: int = 0  # 0 for player 1 for play tester 2 for admin

    # Fake profile setup
    mw: int = 100
    tw: int = 0
    cur_s: int = 100
    max_s: int = 5
    max_earn: int = 2

    # Change this to the game you want to test
    game = slots

    # Play again
    again: bool = True

    # Warn print
    console.print(
        f"[b red]YOU ARE RUNNING THE GAMES FILE NOT THE MAIN GAME \nTesting game: {game.__name__}\nDebug is set to {d}"
    )

    console.print(
        f"[b magenta]The starting values are as follows:\n\nMoney: {mw or 100}\nTimes won: {tw}\nStreak: {cur_s}\nMax Streak: {max_s}\nMax earnings: {max_earn}"
    )

    while again:
        # Add function to test here
        mw, tw, cur_s, max_s, max_earn = init_game(game, mw or 100, tw, cur_s, max_s, max_earn, d)
        console.print(f"Money won: {mw} \nTimes won: {tw}\nStreak: {cur_s}\nMax Streak: {max_s}\nHighest Earning: {max_earn}")
        again = Confirm.ask("Do you want to play again?", default=False)
        if again: # Only clear when testing another game
            clear()

if __name__ == "__main__":
    main()

# endregion
