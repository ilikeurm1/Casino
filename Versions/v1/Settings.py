import os, time

# CUSTUMIZABLE SETTINGS

Main_Directory = os.getcwd() + r"\profiles\v1" # You can customise this field as you want, so you decide where your game files are stored. Please try not to change this after diciding where to store as it can result in data loss or having to move everything manually.
Game_Profile = input("Who is playing: ") # Change this to change or create profiles

# Make the main directory of the game

folder_path = os.path.join(Main_Directory, Game_Profile)
os.makedirs(folder_path, 511, True)

print("")
print(f"Storing game files in path: {folder_path}")

# Add settings file

file_name = 'Money.txt'
file_path = os.path.join(folder_path, file_name) # Used to save your money
if os.path.exists(file_path):
    print("")
    print("Hello again, setting money to last stored")
    with open(file_path, "r") as f:
        Money = int(f.readline())
    print("")
    print(f"You are starting with {Money}$")
else:
    Money = input('How much money do u want to start with: ')
    print("")
    print('Created settings file!')
    with open(file_path, 'w') as fp:
        fp.write(Money)
    Money = int(Money)

time.sleep(1)
