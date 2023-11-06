import os, time, json

# CUSTUMIZABLE SETTINGS

Main_Directory = os.getcwd() + r"\profiles\v2" # You can customise this field as you want, so you decide where your game files are stored. Please try not to change this after diciding where to store as it can result in data loss or having to move everything manually.
Game_Profile = input("What is your username: ") # If you have 

# Make the main directory of the game

print("")
print(f"Storing game files in path: {Main_Directory}")
os.makedirs(Main_Directory, 511, True)

# Save function
def Save(Money):
    with open(file_path, "r") as read_file:
        Users = json.load(read_file)
        # print(Users)
        # print(type(Users))
        # IF user does not exist, ask the money question
        try: 
            Users[Game_Profile]["Money"] = Money
            with open(file_path, "w") as write_file:
                json.dump(Users, write_file, indent=4)
            print(f"Saved money as: {Money}")
        except KeyError:
            print("Money not saved, unknown user!")

# Add users file

file_name = 'Users.json'
file_path = os.path.join(Main_Directory, file_name) # Used to save your money

if os.path.exists(file_path):
    with open(file_path, "r") as read_file:
        print("")
        print(f"Hello {Game_Profile}")
        print("")
        Users = json.load(read_file)
        try: 
            Money = Users[Game_Profile]["Money"]
            print(Money)
            if Money == 0:
                print("")
                Money = int(input('How much money do u want to start with: '))
                print("")
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
    print("")
    Money = int(input('How much money do u want to start with: '))
    print("")
    data = {
        Game_Profile: {
            "Money": Money
        }
    }
    with open(file_path, "w") as write_file:
        json.dump(data, write_file, indent=4)
time.sleep(1)
