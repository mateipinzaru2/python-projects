class Rectangle:
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
