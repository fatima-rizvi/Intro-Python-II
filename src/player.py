# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room, stuff = []):
        self.name = name
        self.current_room = current_room
        self.stuff = stuff
    
    def __repr__(self):
        return f"{self.stuff}"

    def grab(self, item):
        self.stuff.append(item.name)
        print(f"Okay, you have picked up the {item.name}")
        print(f"Your items: {self.stuff}")

    def drop(self, item):
        print(f"Item being removed: {item}")
        self.stuff.remove(item)

#__str__: intended to be human readable
    # ex) date/time: month/day/year etc.
#__repr__: explicit for development
    # ex) date/time: hours,minutes,seconds
