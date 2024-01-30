"""
OVERLOADING BUILT-IN METHODS
Last but not least, let's take a look at some of the built-in methods we can overload in Python. While there isn't a default behavior for the arithmetic operators like we just saw, there is a default behavior for printing a class.

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


p1 = Point(4, 5)
print(p1)
# prints "<Point object at 0xa0acf8>"

That's not super useful! Let's teach instances of our Point object to print themselves. The __str__ method (short for "string") lets us do just that. It takes no inputs but returns a string that will be printed to the console when someone passes an instance of the class to Python's print() function.

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x},{self.y})"

p1 = Point(4, 5)
print(p1)
# prints "(4,5)"

Note: the __repr__ method works in a similar way, you'll see it from time to time.

ASSIGNMENT
Dragons are egotistical creatures, let's give them a great format for announcing their presence in "Age of Dragons". When print() is called on an instance of a Dragon, the string I am {0}, the {1} dragon should be printed.

{0} is the name of the dragon.
{1} is the color of the dragon.
"""


class Dragon:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def __str__(self):
        return f"I am {self.name}, the {self.color} dragon"
