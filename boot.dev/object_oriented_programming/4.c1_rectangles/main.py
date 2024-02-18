"""
RECTANGLES
You discovered that while working on a math project, you needed to calculate the area and perimeter of squares and rectangles of various sizes. With a long list of shapes to process, you decided to write a program to automate the calculations instead of wasting time pounding buttons on your calculator.

To be efficient, you decided it would be best to use classes that inherit features, which allows you to write less code to accomplish the same task.

CHALLENGE
Finish implementing the empty methods of the Rectangle and Square classes.

Keep in mind that a square is just a rectangle where the length and width are equal. You shouldn't have to duplicate any code between the two classes.
"""


class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def get_area(self):
        return self.__length * self.__width

    def get_perimeter(self):
        return 2 * (self.__length + self.__width)


class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)
