# region Imports

from msvcrt import getch

from settings import (
    # 3rd party
    sleep, # time
    randint, choice, random, # random
    console, Prompt, Confirm, # rich
    music, USE_SOUND, # Pygame
    # Consts
    UTILS_DIR,
    )

from utils import (
    # Funcs
    random_style,
    ascii_art_anim,
    # Strings
    BLUE_GRINCH,
    SANS,
    FREDDY,
    FREDDY_JUMPSCARE,
    )

# endregion

# region Helper funcs

def fifty_fifty() -> bool:
    return random() <= .5

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
    take = Confirm.ask("[green]Do you want to take it?", default=True)
    if take:
        bad_trip = fifty_fifty()
        action = Prompt.ask("[green]You take the substance, what do you want to do with it?", choices=["eat", "sniff"], case_sensitive=False)
        if action == "eat":
            if bad_trip:
                for _ in range(100):
                    console.print("You eat the stuff and start tripping balls", style=random_style(), end="\r")
                    sleep(.02)

                console.print("You eat the stuff and start tripping balls", style=random_style())

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
                    for _ in range(100):
                        console.print("You sniff it and start having a horrible trip you lose 40% of your money due to bad plays in the casino", style=random_style(), end="\r")
                        sleep(.02)

                    console.print("You sniff it and start having a horrible trip you lose 40% of your money due to bad plays in the casino", style=random_style())

                    money -= round(money * .4)
                else:
                    for _ in range(100):
                        console.print("You sniff the substance and have a bad trip", style=random_style(), end="\r")
                        sleep(.02)

                    console.print("You sniff the substance and have a bad trip", style=random_style())

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

def knee_surgery(money: int) -> int:
    """Yea this is happening"""
    console.print("[blue]A nearby gambler loses all his life savings on by them on black")
    sleep(3)
    console.print("[blue]He is so angy he throws his chair at you and hits you in the knee")
    sleep(3)
    console.print("[blue]You have to go to the hospital and get knee surgery")
    sleep(3)
    console.print("[blue]You start having a certain feeling")
    sleep(3)
    console.print("[blue]It must be...")
    sleep(3)
    console.print("[blue]That feeling when knee surgery is tomorrow")
    sleep(3)
    ascii_art_anim(BLUE_GRINCH)
    sleep(3)
    console.print("[blue]You have to pay 30% of your money for the surgery")
    money -= round(money * .3)

    return money

def sans(money: int) -> int:
    console.print("[blue]You've got a feeling like you're going to have a bad time...")
    sleep(3)
    ascii_art_anim(SANS)
    Sans_dialog = "Sans: Hey, kid. You know that gambling is an addiction right?"
    for c in Sans_dialog:
        console.print(f"[blue]{c}", end="")
        if USE_SOUND:
            music.load(UTILS_DIR + r"\sounds\sans_speaking.mp3")
            music.play()
        sleep(.075)

    console.print()

    sleep(3)
    action = Prompt.ask("[green]What do you want to do?", choices=["fight", "act", "mercy"], case_sensitive=False)
    if action == "fight":
        console.print("[blue]You try to fight Sans but he dodges all your attacks")
        sleep(3)
        console.print("[blue]He hits you with a bone and you lose 50% of your money")
        money -= round(money * .5)
    elif action == "act":
        console.print("[blue]You tell Sans a pun, and he leaves you alone")

    elif action == "mercy":
        console.print("[blue]There is no mercy with an addiction kid!")
        sleep(3)
        console.print("[blue]He hits you with his BIG bone and you lose 50% of your money")
        money -= round(money * .5)

    return money

def freddy(money: int) -> int:
    console.print("[blue]You're starting to get a little hungry")
    sleep(2)
    console.print("[blue]You go to the pizza place to try and order a pizza")
    sleep(2)
    console.print("[blue]Suddenly what seems to be an mechanical bear approaches you")
    sleep(2)
    ascii_art_anim(FREDDY)
    console.print("Freddy: Hey there you look hungry, want some of my pizza?")
    pizza = Confirm.ask("[green]Do you a piece of freddy's the pizza?", default=True)
    if pizza:
        poison = fifty_fifty()
        console.print("[blue]You take a slice of his pizza and start eating it")
        sleep(3)
        if poison:
            freaky = fifty_fifty()
            console.print("[blue]You start feeling a little weird")
            sleep(2)
            console.print("[blue]You start feeling a really weird")
            sleep(2)
            console.print("[blue]You turn to ask Freddy what's on the pizza but it's too late...", end=' ')
            sleep(2)
            console.print("[blue]You are already asleep...")
            sleep(5)
            if freaky:
                console.print("[blue]You wake up feeling a sharp continuing pain in your rear")
                if USE_SOUND:
                    console.print("[blue]You suddenly notice the loud sound coming from behind you")
                    music.load(UTILS_DIR + r"/sounds/freddy_smash.mp3")
                    music.play()
                sleep(2)
                console.print("[blue]You beg Freddy to stop but he keeps going...")
                sleep(2)
                console.print("[blue]After hes done he tells you you're a good boy...")
                sleep(2)
                console.print("[blue]Freddy pays you 50% of your money to keep your mouth shut")
                money += round(money * .5)

            else:
                console.print("[blue]You find yourself in a dark cellar after having just woken up")
                sleep(2)
                console.print("[blue]Your entire body hurts")
                sleep(2)
                console.print("[blue]You wonder what Freddy did to you")
                sleep(2)
                console.print("[blue]Freddy comes out of the corner and tells you he will let you free unless you tell people")
                sleep(3)
                console.print("[blue]You swear you won't tell and he lets you out")
                sleep(2)
                console.print("[blue]For some reason right before you go, Freddy gives you some money...")
                sleep(2)
                console.print("[blue]You really start to wonder what happened while you were asleep")
                money += round(money * .3)

        else:
            console.print("[blue]You really like it and tell Freddy who is happy to hear it")
            sleep(3)
            console.print("[blue]You finish your slice, thank Freddy and go back to gambling")

    else:
        console.print("[blue]You don't take Freddy's pizza and turn to go continue gambling")
        angy = fifty_fifty()
        if angy:
            console.print("[blue]But Freddy stops you... he looks a little mad ")
            sleep(4)
            console.print("[b megenta]JUMPSCARE TIME :)")
            if USE_SOUND:
                music.set_volume(1)
                music.load(UTILS_DIR + r"\sounds\freddy_scream.mp3")
                music.play()
            for line in FREDDY_JUMPSCARE:
                console.print(line, end="")

            sleep(2)
            console.print("[blue]You lose 50% of your money")
            money -= round(money * .5)

        else:
            console.print("[blue]Freddy stops you and tells you he wants a thanks")
            sleep(2)
            console.print("[blue]You say thanks and get out of there... feeling a little disturbed by Freddy's attitude")

    return money

# endregion

# region main event function

def run_random_event(user: str, money: int, DEBUG: int) -> int:
    """A function that tries to run a random event

    Args:
        user (str): the users name
        money (int): the money they have when the event starts
        DEBUG (int): the debug level

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
        "knee_surgery": 20,
        "sans": 50,
        "freddy": 50
    }

    possible_events: list = []

    # Generate the random chances
    hobo_chance = randint(1, chances["drunk_hobo"])                      # 5%
    random_money_chance = randint(1, chances["random_money_on_floor"])   # 10%
    taxevasion_chance = randint(1, chances["tax_evasion"])               # 1%
    weird_substance_chance = randint(1, chances["weird_substance"])      # 2%
    joe_chance = randint(1, chances["joe"])                              # 0.1%
    knee_surgery_chance = randint(1, chances["knee_surgery"])            # 5%
    sans_chance = randint(1, chances["sans"])                            # 2%
    freddy_chance = randint(1, chances["freddy"])                        # 2%

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

    if knee_surgery_chance == 6:
        possible_events.append(knee_surgery)

    if sans_chance == 39:
        possible_events.append(sans)

    if freddy_chance == 95:
        possible_events.append(freddy)

    # If the possible events list contains at least 1 event
    if possible_events:
        # Sort the possible events list according to the rarity (so if a 1% triggers it will run above the 10% which may also have been possible)
        possible_events.sort(key=lambda f: chances[f.__name__])

        # Choose the rarest event
        event = possible_events[0]

        if DEBUG:
            # Tell the user an event is happening
            console.print(f"[b magenta]{user.upper()}! YOU HAVE TRIGGERED A SPECIAL EVENT: {event.__name__}")

        # Run it
        return event(money)

    if DEBUG:
        # Tell the user no event is happening
        console.print(f"[b magenta]{user}! no special event this time")

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
            knee_surgery,
            sans,
            freddy
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
