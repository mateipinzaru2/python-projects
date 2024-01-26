"""
CONSTRUCTORS (OR INITIALIZERS)
It's quite rare in the real world to see a class that defines properties in the way we've been doing it.

class Soldier:
    armor = 2
    num_weapons = 2

It's much more practical to use a constructor. In Python, the constructor is the init() method, and it is called when a new object is created.

So, with a constructor, the code would look like this.

class Soldier:
    def __init__(self):
        self.armor = 2
        self.num_weapons = 2

However, because the constructor is a method, we can now make the starting armor and number of weapons configurable with some parameters.

class Soldier:
    def __init__(self, armor, num_weapons):
        self.armor = armor
        self.num_weapons = num_weapons

soldier = Soldier(5, 10)
print(soldier.armor)
# prints "5"
print(soldier.num_weapons)
# prints "10"

ASSIGNMENT
Add a constructor to our Wall class. It should take depth, height and width as parameters, in that order, and set them as properties. It should also compute an additional property called volume. Volume is the width times height times depth.
"""


class Wall:
    def __init__(self, depth, height, width):
        self.depth = depth
        self.height = height
        self.width = width
        self.volume = self.width * self.height * self.depth
