# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room, stuff = []):
        self.name = name
        self.current_room = current_room
        self.stuff = stuff
    
#__str__: intended to be human readable
    # ex) date/time: month/day/year etc.
#__repr__: explicit for development
    # ex) date/time: hours,minutes,seconds
    
    def __repr__(self):
        return f"{self.stuff}"

#CHanges made here
    def grab(self, item):
        self.stuff.append(item)
        print(f"Okay, you have picked up the {item}")
        # print(f"Your items: {self.stuff}")

    def drop(self, item):
        print(f"Item being removed: {item}")
        self.stuff.remove(item)

