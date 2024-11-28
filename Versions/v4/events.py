# region Imports

from msvcrt import getch

from settings import (
    # 3rd party
    sleep, # time
    randint, choice, # random
    console, Prompt, Confirm, # rich
    )

from utils import random_style

# endregion

# region Helper funcs

def fifty_fifty() -> int:
    return randint(0,1)

# endregion

# region events

def drunk_hobo(money: int) -> int:
    console.print("You find a drunk hobo in the corner of the room, he asks you for some money")
    # Ask the player if they want to give him some money
    gave = Confirm.ask("[green]Do you want to give him some money?")
    # If the user agrees they give the hobo 5% if their money
    if gave:
        console.print("[blue]You gave the hobo 5% of you money")
        money -= round(money * 0.05)

    # The user doesn't give the hobo any money
    else:
        console.print("[blue]You didn't give the hobo any money")
        # Get the hobo's action
        hobo_action = randint(1, 2) # Not 50-50 as maybe in future new actions

        # Attacks (-10% of users money)
        if hobo_action == 1:
            console.print("[blue]The hobo gets mad and attacks you")
            sleep(3)
            # See if the hobo has a knife
            knife = fifty_fifty()
            if knife:
                # Long ass text explaining what's happening
                console.print("[blue]The crazy bastard pulls out a knife and starts swinging it at you")
                sleep(4)
                console.print(f"[blue]You dodge the knife and tell him you'll give him {round(money * .1)}$ if he stops swinging")
                sleep(4)
                console.print("[blue]He calms down and tell you to give him it, knife still in his hand")
                sleep(3)
                console.print("[blue]You give him the money and make your way back into the casino...")
                sleep(3)
                console.print("[blue]You lost 10% of your money")
                money -= round(money * .1)
            else:
                # Long ass text explaining what's happening
                console.print("[blue]The crazy dude start punching at you and you tell him to stop as you don't want to hurt him")
                sleep(4)
                console.print("[blue]But the hobo doesn't stop and you are forced to defend yourself")
                sleep(3)
                console.print("[blue]You punch the hobo once and he is knocked out instantly")
                sleep(3)
                console.print("[blue]You're on your way back inside the casino but see some money in the hobo's inner pocket")
                sleep(3)
                console.print(f"[blue]You find around {round(money * .1)} in the old dudes pocket and think to yourself why he got so angry?")
                sleep(4)
                console.print("[blue]You take the money and go back inside")
                money += round(money * .1)

        # Stays calm and leaves the user alone
        if hobo_action == 2:
            console.print("[blue]The hobo thanks you anyway and leaves you alone")

    return money

def random_money_on_floor(money: int) -> int:
    console.print("[blue]You find a wallet on the floor, it has some money in it")
    # 50/50 for 5% or 10% money gain
    found = fifty_fifty()
    sleep(1)
    if found:
        console.print("[blue]You gained an extra 5% of your money", end="")
        money += round(money * 0.05)
    else:
        console.print("[blue]You gained an extra 10% of your money", end="")
        money += round(money * 0.1)

    console.print(f" and now have {money}$")

    return money

def tax_evasion(money: int) -> int:
    # Define the hiding places
    hiding_places = ["window","vip lounge"]
    console.print("[blue]The feds have broken down the casino door ran up to you to confront you about your tax evasion")
    # Ask the user if they want to surrender
    surrender = Confirm.ask("[green]Do you want to confess and surrender?", default=False)
    sleep(1)

    # The user gives themselves up
    if surrender:
        chill_feds = fifty_fifty()
        if chill_feds:
            console.print("[blue]The feds really appreciate your honesty and let you of with a warning")
        else:
            # The feds aren't nice and takwe 60% of the users money
            console.print("[blue]You give yourself up and they charge you 60% of your total money")
            money -= round(money * .6)
    else:
        # Ask where the user wants to go
        hiding_place = Prompt.ask("[green]You dont give yourself up and start running where do you go?", case_sensitive=False, choices=hiding_places)
        # Determine if the user is gonna get cought
        cought = fifty_fifty()
        # The user chooses to go to the window
        if hiding_place == "window":
            if cought:
                console.print("[blue]You try to run to the window but get shot in the leg")
                sleep(3)
                console.print("[blue]They fine you 60% of your money for the tax evasion and another 30% extra for running away")
                money -= round(money * .9)

            else:
                console.print("[blue]You run to the window, smash it and look out")
                sleep(3)
                # Spawn a random umbrella?
                Umbrella = fifty_fifty()
                if Umbrella:
                    console.print("[blue]Out of the corner of your eye you see a random Umbrella flying towards you")
                    sleep(3)
                    console.print("[blue]You leap forward and catch the umbrella which get you safely towards the floor")
                else:
                    console.print("[blue]You jump out and fall very far and break your legs, you have managed to escape the feds but the medical bill comes out to 70% of your money")
                    sleep(3)
                    money -= round(money * .7)

        elif hiding_place == "vip lounge":
            if cought:
                console.print("[blue]You run to the lounge as fast as you can but the feds are fast and catch you")
                sleep(3)
                console.print("[blue]They fine you 60% of your money for the tax evasion and another 30% extra for running away")
                money -= round(money * .9)

            else:
                console.print("You run to the VIP lounge and pay the bouncer 10% of your money")
                money -= round(money * .1)
                sleep(3)
                console.print("The feds don't find you and you manage to escape")

    return money

def weird_substance(money: int) -> int:
    console.print("[blue]A weird man looking an awful lot like Walter offers you a weird substance")
    take = Confirm.ask("[green]Do you want to take it?")
    if take:
        bad_trip = fifty_fifty()
        action = Prompt.ask("[green]You take the substance, what do you want to do with it?", choices=["eat", "sniff"], case_sensitive=False)
        if action == "eat":
            if bad_trip:
                console.print("[blue]You eat the stuff and start tripping balls")
                sleep(1)
                console.print("[blue]You lose 20% of your money due to your horrible plays")
                money -= round(money * .2)
            else:
                console.print("[blue]You have an awesome experience and start winning a shit ton of money")
                sleep(1)
                console.print("[blue]You gain 20% of your money due to your excellent gambling skills")
                money += round(money * .2)

        elif action == "sniff":
            if bad_trip:
                wait = fifty_fifty()
                if not wait:
                    console.print("[blue]You sniff it and start having a horrible trip you lose 40% of your money due to bad plays in the casino")
                    money -= round(money * .4)
                else:
                    console.print("[blue]You sniff the substance and have a bad trip")
                    sleep(1)
                    console.print("[blue]Instead of continuing to gamble you go sit down and wait till everything is over")

            else:
                console.print("[blue]You sniff the substance and win a bunch of money due to you locking in")
                sleep(1)
                console.print("[blue]You win 20% of your money")
                money += round(money * .2)

    else:
        console.print("[blue]You don't take the substance and ")

    return money

def joe(money: int) -> int:
    who_str = "who?"
    sleep(1)
    console.print("[green]Joe? Joe", end=" ")

    for x in range(4):
        getch()
        console.print(f"[green]{who_str[x]}", end="")

    sleep(.5)

    console.print("")

    for _ in range(20):
        console.print("JOE MAMA", style=random_style())
        sleep(.1)

    sleep(1)
    console.print("[green]He took 90% of your money, womp womp")

    money -= round(money * .9)
    return money

# endregion

# region main event function

def run_random_event(user: str, money: int) -> int:
    """A function that tries to run a random event

    Args:
        user (str): the users name
        money (int): the money they have when the event starts

    Returns:
        money (int): the money the user has after the event is over
    """
    console.print()

    # chances dictionary that stores how rare each event should be
    chances: dict[str, int] = {
        # Syntax:
        # "Name_game": chance
        # chance = 1 in chance
        "drunk_hobo": 20,
        "random_money_on_floor": 10,
        "tax_evasion": 100,
        "weird_substance": 50,
        "joe": 1000,
    }

    possible_events: list = []

    # Generate the random chances
    hobo_chance = randint(1, chances["drunk_hobo"])                      # 5%
    random_money_chance = randint(1, chances["random_money_on_floor"])   # 10%
    taxevasion_chance = randint(1, chances["tax_evasion"])               # 1%
    weird_substance_chance = randint(1, chances["weird_substance"])      # 2%
    joe_chance = randint(1, chances["joe"])

    # Add all the possible events to the possible events list
    # the numbers that they have to be equal to are just some I picked out... I didn't want all them to just say 1
    if hobo_chance == 14:
        possible_events.append(drunk_hobo)

    if random_money_chance == 3:
        possible_events.append(random_money_on_floor)

    if taxevasion_chance == 86:
        possible_events.append(tax_evasion)

    if weird_substance_chance == 23:
        possible_events.append(weird_substance)

    if joe_chance == 827:
        possible_events.append(joe)

    # If the possible events list contains at least 1 event
    if possible_events:
        # Tell the user an event is happening
        console.print(f"[b magenta]{user}! YOU HAVE TRIGGERED A SPECIAL EVENT:", end=" ")
        # Sort the possible events list according to the rarity (so if a 1% triggers it will run above the 10% which may also have been possible)
        possible_events.sort(key=lambda f: chances[f.__name__])
        # Choose the rarest event
        event = possible_events[0]
        # Tell the user which event they are running
        console.print(event.__name__)
        # Run it
        return event(money)

    # No event = no change in money
    return money

# endregion

# region TESTING

def main() -> int:
    """Main function."""
    def clear() -> None:
        """Clears the console"""
        console.clear(home=False)

    try:
        again = True

        events = [
            drunk_hobo,
            random_money_on_floor,
            tax_evasion,
            weird_substance,
            joe,
        ]

        while again:
            clear()
            money = 1000
            chosen = Confirm.ask("[green]Do you want to choose an event?", default=True)
            if not chosen:
                event = choice(events)

                # console.print(f"Your money before the event: {money}")
                money = event(money)
                # console.print(f"Your money after the event: {money}")
                sleep(4)
                clear()
            else:
                index = Prompt.ask(f"[green]choose which event (number in list starting with 1): {[f.__name__ for f in events]}",choices=[str(x) for x in range(1, len(events) + 1)])
                event = events[int(index) - 1]
                console.print(f"Your money before the event: {money}")
                money = event(money)
                console.print(f"Your money after the event: {money}")

            again = Confirm.ask("[green]Wanna go again?", default=True)

    except Exception as e:
        print(f"An error occurred: {e}")
        return 1

    return 0

if __name__ == "__main__":
    exit_code = main()

    if exit_code != 0:
        print(f"An error occurred.\nexit code: {exit_code}")

    else:
        print(f"Program exited successfully\nexit code: {exit_code}")

# endregion
