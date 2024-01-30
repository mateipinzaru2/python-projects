"""
CHECK IF RECTANGLES OVERLAP
ASSIGNMENT
Let's write the overlaps() method. It should check if this rectangle overlaps a given rectangle, rect. Return True or False if this rectangle overlaps any part of rect, including just touching sides.

Here are four conditions that must be True if this rectangle (A) overlaps or touches rect (B):

A's left side is on or to the left of B's right side
A's right side is on or to the right of B's left side
A's top side is on or above B's bottom side
A's bottom side is on or below B's top side
"""


class Rectangle:
    def overlaps(self, rect):
        return (
            self.get_left_x() <= rect.get_right_x()
            and self.get_right_x() >= rect.get_left_x()
            and self.get_top_y() >= rect.get_bottom_y()
            and self.get_bottom_y() <= rect.get_top_y()
        )

    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def get_left_x(self):
        return min(self.x1, self.x2)

    def get_right_x(self):
        return max(self.x1, self.x2)

    def get_top_y(self):
        return max(self.y1, self.y2)

    def get_bottom_y(self):
        return min(self.y1, self.y2)
