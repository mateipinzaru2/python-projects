"""
WIZARD DUEL
Let's give our wizards the ability to launch fireballs at each other.

ASSIGNMENT
Complete the cast_fireball method.

Casting a fireball costs 20 mana
If the wizard doesn't have enough mana, raise the exception {1} cannot cast fireball, where {1} is the caster's name.
Otherwise, return {1} casts fireball at {2}, where {1} is the caster's name and {2} is the target's name, then make sure the target is "fireballed"
"""


class Wizard:
    def cast_fireball(self, target):
        if self.__mana < 20:
            raise ValueError(f"{self.name} cannot cast fireball")

        self.__mana -= 20
        target.get_fireballed()
        return f"{self.name} casts fireball at {target.name}"

    # don't touch below this line

    def __init__(self, name):
        self.__mana = 45
        self.__health = 65
        self.name = name

    def get_mana(self):
        return self.__mana

    def get_health(self):
        return self.__health

    def get_fireballed(self):
        fireball_damage = 30
        self.__health -= fireball_damage
        if self.__health <= 0:
            print(f"{self.name} is dead")

    def drink_mana_potion(self):
        self.__mana += 40
