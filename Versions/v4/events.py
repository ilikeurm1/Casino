from settings import sleep, console, randint, Confirm

def drunk_hobo(money: int) -> int:
    console.print("You find a drunk hobo in the corner of the room, he asks you for some money")
    gave = Confirm.ask("Do you want to give him some money?")
    if gave:
        console.print("You gave the hobo 5% of you money")
        money -= round(money * 0.05)
    else:
        console.print("You didn't give the hobo any money")
        hobo_action = randint(1, 2)
        
        if hobo_action == 1:
            console.print("The hobo gets mad and attacks you")
            sleep(1)
            console.print("You lost 10% of your money")
            money -= round(money * 0.1)
        else:
            console.print("The hobo thanks you anyway and leaves you alone")
    
    return money       

def random_money(money: int) -> int:
    console.print("[magenta]SPECIAL EVENT:")
    console.print("[blue]You find a wallet on the floor, it has some money in it")
    found = randint(1, 2)
    if found == 1:
        console.print("You gained an extra 5% of your money", end="")
        money += round(money * 0.05)
    else:
        console.print("You gained an extra 10% of your money", end="")
        money += round(money * 0.1)
        
    console.print(f" and now have {money}$")
    
    return money
