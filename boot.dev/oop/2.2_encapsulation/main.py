"""
WIZARD DUEL
Let's add some more features to our Wizard class and have ourselves a Wizard duel.

ASSIGNMENT
Add the following methods to the Wizard class.

GET_FIREBALLED()
This method operates on the instance of the class and takes no inputs as parameters. It should remove 30 health from the class instance.

DRINK_MANA_POTION()
This method operates on the instance of the class and takes no inputs as parameters. It should add 40 to the current mana value of the wizard.
"""


class Wizard:
    def __init__(self, name):
        self.__mana = 45
        self.__health = 65
        self.name = name

    def get_mana(self):
        return self.__mana

    def get_health(self):
        return self.__health

    def get_fireballed(self):
        self.__health -= 30

    def drink_mana_potion(self):
        self.__mana += 40
