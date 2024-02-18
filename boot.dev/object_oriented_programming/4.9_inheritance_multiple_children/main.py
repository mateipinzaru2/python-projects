"""
MULTIPLE CHILDREN
ASSIGNMENT
Let's extend the Hero class by adding a second child class: the Wizard. Wizard heroes are more powerful than archer heroes. They cast spells at other heroes instead of shooting them, and casting does 25 damage instead of 10 but also costs 25 mana.

Fulfill the following requirements.

Wizard should inherit from Hero
Wizard should set up the hero's name and health
Set a private "mana" variable that can be passed in as a third parameter to the constructor.
Create a cast method that takes a target hero as input. If there is not enough mana left, raise a not enough mana exception. Otherwise, remove 25 mana from the wizard and deal 25 damage to the target hero.
"""


class Hero:
    def __init__(self, name, health):
        self.__name = name
        self.__health = health

    def get_name(self):
        return self.__name

    def get_health(self):
        return self.__health

    def take_damage(self, damage):
        self.__health -= damage


class Archer(Hero):
    def __init__(self, name, health, num_arrows):
        super().__init__(name, health)
        self.__num_arrows = num_arrows

    def shoot(self, target):
        if self.__num_arrows <= 0:
            raise Exception("not enough arrows")
        self.__num_arrows -= 1
        target.take_damage(10)


class Wizard(Hero):
    def __init__(self, name, health, mana):
        super().__init__(name, health)
        self.__mana = mana

    def cast(self, target):
        if self.__mana < 25:
            raise ValueError("not enough mana")
        self.__mana -= 25
        target.take_damage(25)
