from room import Room
from player import Player
import random
import time # For dramatic pauses and helping the flow of the story
from item import Item

# Declare all the items
stuff = {
    'thing': Item("thing", "Not to sure what it is. Might be useful, might be trash."),
    'sword': Item("sword", "Pretty sharp and sturdy."),
    'potion': Item("potion", "It's blue, so there's a 50/50 chance that it's either healing or poisonous."),
    'dagger': Item("dagger", "Rather ornate, might be decorative?"),
    'gun': Item("gun", "More specifically, a Tokarev TT-30"),
    'shield': Item("shield", "Unfortunately, it's not Zeus's famed aegis. That would've been nice."),
    'cornucopia': Item("cornucopia", "Hmm, you might be able to use this for food"),
    'staff': Item("staff", "Is it like Gandalf's? Or is it just a big stick?"),
    'torch': Item("torch", "Nice, a light source! That'll be handy.")
}

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",
                     stuff[random.choice(list(stuff.keys()))]),

                     # stuff[random.choice(list(stuff.keys()))])
                     # Explanation of this snippet:
                     # This grabs the keys of the stuff dictionary and turning them into a list. Then using the choice method in the random module it randomly selects an item from that list (which is a key in the stuff dictionary). Then it calls the dictionary value at the randomly selected key by passing the item into the stuff dictionary

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""",
stuff[random.choice(list(stuff.keys()))]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
stuff[random.choice(list(stuff.keys()))]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",
stuff[random.choice(list(stuff.keys()))]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",
stuff[random.choice(list(stuff.keys()))]),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
# new_player = Player("Buzz Lightyear", room['outside'])
player_name = input("Hello adventurer! What is you name?: ")
new_player = Player(player_name, room['outside'])
print(f"Good luck on your quest, {new_player.name}...\n")
time.sleep(2)
print("... You might need it\n")
time.sleep(1.5)

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

direction = ""
while direction != "q":
    print("Your current location: ", new_player.current_room.name)
    time.sleep(1)
    print(f"{new_player.current_room.description}\n")

    access_inventory = ''
    while access_inventory.lower() != "pass":
        time.sleep(1)
        print(f"This is what you are currently holding: \n{new_player.stuff}\n")

        time.sleep(1)

        if len(new_player.current_room.stuff) > 0:
            print(f"You see something on the ground. It looks like")
            new_player.current_room.list_items()
        else: # If all items have already been removed from the room, then nothing would print when list_items() is called, so this meesage below just notifies the player that the room is empty.
            print("There is nothing in this room")

        time.sleep(1)

        print("\nWhat would you like to do?")

        time.sleep(1)
        
        access_inventory = input("""
    If you would like to pick up an item from the room, type 'get [ITEM_NAME]'
    If you would like to drop an item from your inventory, type 'drop [ITEM_NAME]'
    
    If you don't want to do anything, type 'PASS'
    
    Your choice, adventurer: """)

        choice = access_inventory.split(" ")
        # By splitting it, the first item in the list (choice[0]) will be either "get", "drop", or "pass", and I can work directly with the action the player wants to take. choice[1], if it exists, will be the item the player wants to interact with.
        
        if len(choice) > 1:
            # This will make sure the item name is in lowercase and stripped of any extra spaces.
            active_item = choice[1].lower().strip()

        print() # Printing a blank line before any messages from actions can be printed

        if choice[0].lower() == 'get':
            new_player.grab(stuff[active_item]) #Accessing the item dictionary with the name of the active item as the key so that we are passing in the whole item to any methods
            new_player.current_room.remove_item(stuff[active_item])
        elif choice[0].lower() == 'drop':
            new_player.drop(stuff[active_item])
            new_player.current_room.add_item(stuff[active_item])
        elif choice[0].lower() == 'pass':
            print("Okay, you chose not to add or drop any items.\n")
        else: # In case invalid input is given 
            print("Hmm, I don't think that's an option")


    direction = input("Where would you like to go? (n/s/e/w) OR q for quit: ")
    print()
# command shift down and alt shift down to copy and paste
    if direction == "n":
        if new_player.current_room.n_to == None:
            print("There is no room to the north")
        else:
            new_player.current_room = new_player.current_room.n_to

    elif direction == "s":
        if new_player.current_room.s_to == None:
            print("There is no room to the south")
        else:
            new_player.current_room = new_player.current_room.s_to

    elif direction == "e":
        if new_player.current_room.e_to == None:
            print("There is no room to the east")
        else:
            new_player.current_room = new_player.current_room.e_to

    elif direction == "w":
        if new_player.current_room.w_to == None:
            print("There is no room to the west")
        else:
            new_player.current_room = new_player.current_room.w_to
            
    elif direction == "q":
        print("Thank you for playing!")

    else:
        print("That option doesn't exist, try again")

#Sam's streamlined code
# def room_logic(dir):
#     if dir == "grab":
#         new_player.grab(dir)
#     else:
#         letter = dir + '_to'
#         print(letter)
#         if not getattr(new_player.current_room, letter):
#             print("There's nothing here! I'll head back!")
#         else:
#             new_player.current_room = getattr(new_player.current_room, letter)
# player_input = input("Where would you like to go? (n/s/e/w or q to exit)")
# while player_input != 'q':
#     print(new_player.current_room.name)
#     print(new_player.current_room.description)
#     print("Items in the room: ", new_player.current_room.items)
#     room_logic(player_input)
#     player_input = input("Where would you like to go next? (n/s/e/w or q to exit)")
# print("thanks for playing")
    

# My chopped code:

# print(f"You see something on the ground. It looks like a {new_player.current_room.stuff.name}. {new_player.current_room.stuff.description}")

# take_item = input(f"Do you want to take the {new_player.current_room.stuff.name}? (y/n) ")
    # if take_item.lower() == "y":
    #     new_player.grab(new_player.current_room.stuff)
    #     new_player.current_room.remove_item(new_player.current_room.stuff.name) #For some reason this is accessing the item class instead of the room class, throwing an error
    # else:
    #     print(f"Okay, you are leaving the {new_player.current_room.stuff.name} behind.")

# drop_item = input(f"Would you like to drop an item? (y/n) ")
    # if drop_item.lower() == "y":
    #     item_to_drop = str(input(f"What would you like to drop? {new_player.stuff}: "))
    #     new_player.drop(item_to_drop.lower().strip())
