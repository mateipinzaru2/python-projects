"""
DRAGONS
We have written a lot of classes so far, but we haven't written much code that uses the classes and calls their methods.

The code in the test suite is largely the same code that you built in the last assignment. One key difference is the addition of a describe function that you'll be using.

ASSIGNMENT
Let's use the Dragon class to have ourselves a little dragon fight. Complete the bottom half of the main() function.

First, describe() all dragons
Next, make each dragon breathe fire with a blast center of (3,3) and pass in all of the other dragons to see who was hit.
Call describe() on all the dragons first, then have them breathe fire.

ORDER MATTERS FOR YOUR SOLUTION
Make sure to do everything in ascending index order. For example, when Black Dragon breathes fire, it should breathe fire on the other dragons in this order:

Green Dragon
Red Dragon
Blue Dragon
TIPS
COPYING A LIST
To get a new copy of a list, use the copy() method. If you don't, your new variable will just be a reference to the same list.

nums = [4, 3, 2, 1]
nums_copy = nums.copy()
# nums_copy is [4, 3, 2, 1]

DELETE FROM A LIST
nums = [4, 3, 2, 1]
del nums[1]
# nums is [4, 2, 1]
"""


def main():
    dragons = [
        Dragon("Green Dragon", 0, 0, 1),
        Dragon("Red Dragon", 2, 2, 2),
        Dragon("Blue Dragon", 4, 3, 3),
        Dragon("Black Dragon", 5, -1, 4),
    ]

    # don't touch above this line

    for dragon in dragons:
        describe(dragon)
        dragon.breathe_fire(3, 3, [d for d in dragons if d != dragon])


# don't touch below this line


def describe(dragon):
    print(f"{dragon.name} is at {dragon.pos_x}/{dragon.pos_y}")


class Unit:
    def __init__(self, name, pos_x, pos_y):
        self.name = name
        self.pos_x = pos_x
        self.pos_y = pos_y

    def in_area(self, x_1, y_1, x_2, y_2):
        return (
            self.pos_x >= x_1
            and self.pos_x <= x_2
            and self.pos_y >= y_1
            and self.pos_y <= y_2
        )


class Dragon(Unit):
    def __init__(self, name, pos_x, pos_y, fire_range):
        super().__init__(name, pos_x, pos_y)
        self.__fire_range = fire_range

    def breathe_fire(self, x, y, units):
        print(f"{self.name} breathes fire at {x}/{y} with range {self.__fire_range}")
        for unit in units:
            in_area = unit.in_area(
                x - self.__fire_range,
                y - self.__fire_range,
                x + self.__fire_range,
                y + self.__fire_range,
            )
            if in_area:
                print(f"{unit.name} is hit by the fire")


main()
