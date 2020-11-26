from room import Room
from player import Player

# Declare all the items
items = {
    
}

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
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
new_player = Player("Buzz Lightyear", room['outside'])

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
    print(new_player.current_room.description)
    print("Items in the room: ", new_player.current_room.items)

    direction = input("Where would you like to go? (n/s/e/w) OR q for quit: ")
    print()

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
#     letter = dir + '_to'
#     print(letter)
#     if not getattr(new_player.current_room, letter):
#         print("There's nothing here! I'll head back!")
#     else:
#         new_player.current_room = getattr(new_player.current_room, letter)
# player_input = input("Where would you like to go? (n/s/e/w or q to exit)")
# while player_input != 'q':
#     print(new_player.current_room.name)
#     print(new_player.current_room.description)
#     print("Items in the room: ", new_player.current_room.items)
#     room_logic(player_input)
#     player_input = input("Where would you like to go next? (n/s/e/w or q to exit)")
# print("thanks for playing")
    

