#Aaron Doss
#starting screen
def prompt():
    print("Welcome to the game!\nTo move type go then choose a cardinal direction to move in!")
    print("If you want to search the room you're in type grab and the item you spotted!")
    print("Type exit to quit the game!")

#map
rooms = {
   # 'Great Hall': {'South': 'Bedroom'},
    'Dungeon': {'East': 'Guardsroom'},
    'Guardsroom': {'West': 'Dungeon', 'South': 'Armory', 'East': 'Entrance', 'Item': 'Key'},
    'Entrance': {'West': 'Guardsroom', 'South': 'Kitchens', 'Item': 'Map'},
    'Kitchens': {'West': 'Armory', 'North': 'Entrance', 'Item': 'Cat'},
    'Armory': {'North': 'Guardsroom', 'South': 'Kings Bedroom', 'East': 'Kitchens', 'West': 'Bathroom', 'Item': 'Shield'},
    'Bathroom': {'East': 'Armory', 'Item': 'Bottle'},
    'Kings Bedroom': {'North': 'Armory', 'East': 'Throne Room', 'Item': 'Sword'},
    'Throne Room': {'West': 'Kings Bedroom', 'Boss': 'Evil Tyrant'}
}
#tracks current room
currentRoom = 'Dungeon'

#tracks inventory
inventory = []

# Result of last move
msg = ""

prompt()

#gameplay loop
while True:

    #Display info to character
    print(f"you are in the {currentRoom}\nInventory : {inventory}")

    print(msg)

    #items
    if "Item" in rooms[currentRoom].keys():

        nearbyItem = rooms[currentRoom]["Item"]

        if nearbyItem not in inventory:

            print(f"You see a {nearbyItem}")

    #boss
    if "Boss" in rooms[currentRoom].keys():
        print("You see the Evil Tyrant standing upon his throne. TIME TO FIGHT!")

        if len(inventory) != 0:

            if len(inventory) < 6:
                print(f"The {rooms[currentRoom]['Boss']} defeated you.")

            else:
                print(f"You defeated {rooms[currentRoom]['Boss']}.")
        else:
            print("This isn't a speedrun bro. Go find some items!")

    #player input
    userInput = input("Enter your move:\n")
    nextMove = userInput.split(' ')
    playerAction = nextMove[0].title()

    #checks player action
    if len(nextMove) > 1:
        item = nextMove[1:]
        direction = nextMove[1].title()

        item = ' '.join(item).title()

    #moving character
    if playerAction == 'Go':

        try:
            currentRoom = rooms[currentRoom][direction]
            msg == f"You travel {direction}."

        except:
            msg = "You can't go that way."

    #getting items
    elif playerAction == 'Grab':
        try:
            if item == rooms[currentRoom]["Item"]:
                if item not in inventory:

                    inventory.append(rooms[currentRoom]["Item"])
                    msg = f"{item} acquired."

                else:
                    msg = f"You already have the {item}."

            else:
                msg = f"Can't find {item}."
        except:
            msg = f"Can't find {item}."

    #exiting game
    elif playerAction == "Exit":
        break

    else:
        msg = "Invalid Command"




