import os, json
from time import sleep

# CUSTUMIZABLE SETTINGS

Main_Directory = os.getcwd() + r"\profiles\v3" # You can customise this field as you want, so you decide where your game files are stored. Please try not to change this after diciding where to store as it can result in data loss or having to move everything manually.
print()
Game_Profile = input("What is your username: ").capitalize() # If you have already played put in your exact name! ex. Admin

# Make the main directory of the game
print()
print(f"Storing game files in path: {Main_Directory}")
os.makedirs(Main_Directory, 511, True)

# Save function
def Save(Money):
    with open(file_path, "r") as read_file:
        Users = json.load(read_file)
        try: 
            Users[Game_Profile]["Money"] = Money
            with open(file_path, "w") as write_file:
                json.dump(Users, write_file, indent=4)
            print()
            print(f"Saved money as: {Money}$")
        except KeyError:
            print("Money not saved, unknown user!")

# Add users file
file_name = 'Users.json'
file_path = os.path.join(Main_Directory, file_name) # Used to save your money

if os.path.exists(file_path):
    with open(file_path, "r") as read_file:
        print()
        print(f"Hello {Game_Profile}")
        Users = json.load(read_file)
        # IF user does not exist, ask the money question
        try: 
            Money = Users[Game_Profile]["Money"]
            if Money == 0:
                print()
                Money = int(input('How much money do u want to start with: '))
                Save(Money)
        except KeyError:
            Money = int(input('How much money do u want to start with: '))
            Users[Game_Profile] = {            
                "Money": Money
            }
            with open(file_path, "w") as write_file:
                json.dump(Users, write_file, indent=4)
else:
    # New game file
    print(f"Hello {Game_Profile}")
    print()
    Money = int(input('How much money do u want to start with: '))
    data = {
        Game_Profile: {
            "Money": Money
        }
    }
    with open(file_path, "w") as write_file:
        json.dump(data, write_file, indent=4)

print()
print(f"You are starting with {Money}$, have fun!")
sleep(1)
