"""
METHODS CAN RETURN VALUES
If a normal function doesn't return anything, it's typically not a very useful function. Methods often don't return anything explicitly because they often mutate the properties of the object instead. That's exactly what we did in the last assignment.

However, they can return values as well!

class Soldier:
    armor = 2
    num_weapons = 2

    def get_speed(self):
        speed = 10
        speed -= self.armor
        speed -= self.num_weapons
        return speed

soldier_one = Soldier()
print(soldier_one.get_speed())
# prints "6"

ASSIGNMENT
Add a get_cost() method to your wall class. The cost of a wall is the product of its height and armor:

cost = armor * height
"""


class Wall:
    armor = 10
    height = 5

    def get_cost(self):
        return self.armor * self.height

    # don't touch below this line

    def fortify(self):
        self.armor *= 2
