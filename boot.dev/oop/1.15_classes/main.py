"""
ARCHERS
ASSIGNMENT
Complete the Archer class.

CONSTRUCTOR
The constructor should take and set as properties the following parameters in order:

name
health
num_arrows
GET_SHOT METHOD
Finish the method called get_shot that doesn't take any parameters.

If the current archer has health left, remove one health from the current archer. Then, if the archer's health is 0, raise the exception: {} is dead where {} is the archer's name.

SHOOT METHOD
Finish the method called shoot that takes an Archer instance as the target input.

If the shooter has no arrows left, raise the exception {} can't shoot where {} is the shooter's name. Otherwise, remove an arrow from the shooter and print {1} shoots {2} where {1} is the shooter's name and {2} is the name of the targeted archer. Next, call the target's get_shot() method.
"""


class Archer:
    def __init__(self, name, health, num_arrows):
        self.name = name
        self.health = health
        self.num_arrows = num_arrows

    def get_shot(self):
        self.health -= 1

        if self.health <= 0:
            raise ValueError(f"{self.name} is dead")

    def shoot(self, target):
        if self.num_arrows <= 0:
            raise ValueError(f"{self.name} can't shoot")

        self.num_arrows -= 1
        print(f"{self.name} shoots {target.name}")

        target.get_shot()

    # don't touch below this line

    def get_status(self):
        return self.name, self.health, self.num_arrows

    def print_status(self):
        print(f"{self.name} has {self.health} health and {self.num_arrows} arrows")
