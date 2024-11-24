# region Imports

from settings import (
    # 3rd party
    sleep, # time
    randint, choice, # random
    console, Prompt, Confirm, # rich
)

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
            sleep(1)
            # See if the hobo has a knife
            knife = fifty_fifty()
            if knife:
                # Long ass text explaining what's happening
                console.print("[blue]The crazy bastard pulls out a knife and starts swinging it at you")
                sleep(2)
                console.print(f"[blue]You dodge the knife and tell him you'll give him {round(money * .1)}$ if he stops swinging")
                sleep(2)
                console.print("[blue]He calms down and tell you to give him it, knife still in his hand")
                sleep(1)
                console.print("[blue]You give him the money and make your way back into the casino...")
                sleep(1)
                console.print("[blue]You lost 10% of your money")
                money -= round(money * .1)
            else:
                # Long ass text explaining what's happening
                console.print("[blue]The crazy dude start punching at you and you tell him to stop as you don't want to hurt him")
                sleep(2)
                console.print("[blue]But the hobo doesn't stop and you are forced to defend yourself")
                sleep(1)
                console.print("[blue]You punch the hobo once and he is knocked out instantly")
                sleep(1)
                console.print("[blue]You're on your way back inside the casino but see some money in the hobo's inner pocket")
                sleep(1)
                console.print(f"[blue]You find around {round(money * .1)} in the old dudes pocket and think to yourself why he got so angry?")
                sleep(2)
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

def tax_evasion(money: int):
    # Define the hiding places
    hiding_places = ["window","vip lounge"]
    console.print("[blue]The feds have broken down the casino door ran up to you to confront you about your tax evasion")
    # Ask the user if they want to surrender
    surrender = Confirm.ask("Do you want to confess and surrender?", default=False)
    sleep(1)

    # The user gives themselves up
    if surrender:
        chill_feds = fifty_fifty()
        if chill_feds:
            console.print("The feds really appreciate your honesty and let you of with a warning")
            pay_feds = Confirm.ask("Do you want to give the feds some money to show your gratitude?", default=True, show_default=False)
            if pay_feds:
                console.print("You pay the feds 5% of your money and they leave")
                money -= round(money * .05)
            else:
                console.print("The feds leave")
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
                sleep(1)
                console.print("[blue]They fine you 60% of your money for the tax evasion and another 30% extra for running away")
                money -= round(money * .9)
                
            else:    
                console.print("[blue]You run to the window, smash it and look out")
                sleep(1)
                # Spawn a random umbrella?
                Umbrella = fifty_fifty()
                if Umbrella:
                    console.print("[blue]Out of the corner of your eye you see a random Umbrella flying towards you")
                    sleep(1)
                    console.print("[blue]You leap forward and catch the umbrella which get you safely towards the floor")
                else:
                    console.print("[blue]You jump out and fall very far and break your legs, you have managed to escape the feds but the medical bill comes out to 70% of your money")
                    sleep(1)
                    money -= round(money * .7)

        elif hiding_place == "vip lounge":
            if cought:
                console.print("[blue]You run to the lounge as fast as you can but the feds are fast and catch you.")
                sleep(1)
                console.print("[blue]They fine you 60% of your money for the tax evasion and another 30% extra for running away")
                money -= round(money * .9)

            else:
                console.print("You run to the VIP lounge and pay the bouncer 10% of your money")
                money -= round(money * .1)
                sleep(1)
                console.print("The feds don't find you and you manage to escape")

    return money

def weird_substance(money: int):
    console.print("[blue]A weird man looking an awful lot like Walter offers you a weird substance")
    take = Confirm.ask("Do you want to take it?")

# endregion



# region TESTING

def main() -> int:
    """Main function."""
    def clear() -> None:
        """Clears the console"""
        console.clear(home=False)
    
    try:
        events = [
            drunk_hobo,
            random_money_on_floor,
            tax_evasion,
            weird_substance
        ]
        
        while Confirm.ask("Do you want to run a random event?", default=True):
            
            chosen = choice(events)
            money = 1000
            
            console.print(f"Your money before the event: {money}")
            money = chosen(money)
            console.print(f"Your money after the event: {money}")
            sleep(4)
            clear()
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
