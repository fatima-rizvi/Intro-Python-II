# Implement a class to hold room information. This should have name and
# description attributes.
import time #For better story telling effect

class Room:
    def __init__(self, name, description, stuff = []):
        self.name = name
        self.description = description
        self.stuff = [stuff]
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

    def __repr__(self):
       return f"{self.stuff}" 

    def list_items(self):
        for i in range(0, len(self.stuff)):
            time.sleep(1)
            print(f"{i + 1}. A {self.stuff[i].name}. {self.stuff[i].description}")

    def add_item(self, item):
        self.stuff.append(item)

    def remove_item(self, item):
        self.stuff.remove(item)

        # The .remove is now working, and the code below isn't working perfectly so I'm not using it.
        # print(self.stuff)
        # for i in range(0, len(self.stuff)):
        #     if self.stuff[i].name == item:
        #         self.stuff.pop(i)


    