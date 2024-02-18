"""
OPERATOR OVERLOADING
Another kind of built-in polymorphism in Python is the ability to override how an operator works. For example, the + operator works for built-in types like integers and strings.

print(3 + 4)
# prints "7"

print("three " + "four")
# prints "three four"

Custom classes on the other hand don't have any built-in support for those operators:

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


p1 = Point(4, 5)
p2 = Point(2, 3)
p3 = p1 + p2
# TypeError: unsupported operand type(s) for +: 'Point' and 'Point'

However, we can add our own support! If we create an __add__(self, other) method on our class, the Python interpreter will use it when instances of the class are being added with the + operator. Here's an example:

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, point):
        x = self.x + point.x
        y = self.y + point.y
        return Point(x, y)

p1 = Point(4, 5)
p2 = Point(2, 3)
p3 = p1 + p2
# p3 is (6, 8)

Now, when p1 + p2 is executed, under the hood the Python interpreter just calls p1.__add__(p2).

ASSIGNMENT
In Age of Dragons, players can upgrade their weaponry. To make "crafting" simple for other developers, we'll use operator overloading on the Sword class. The + operator should craft the swords. Note how the test suite uses the + operator to craft the swords.

Create an __add__(self, other) method on the Sword class. It will be used to "craft" two swords together to create a new sword. sword_type is just a string, one of:

bronze

iron

steel

If two "bronze" swords are crafted together, return a new "iron" sword.

If two "iron" swords are crafted together, return a new "steel" sword.

If a player tries to craft anything other than 2 bronze swords or 2 iron swords, just raise an Exception with the message "can not craft".
"""


class Sword:
    def __init__(self, sword_type):
        self.sword_type = sword_type

    def __add__(self, other):
        if self.sword_type != other.sword_type or other.sword_type not in (
            "bronze",
            "iron",
        ):
            raise ValueError("can not craft")
        if other.sword_type == "bronze":
            return Sword("iron")
        return Sword("steel")
