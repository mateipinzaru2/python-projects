class Unit:
    def __init__(self, name, pos_x, pos_y):
        self.name = name
        self.pos_x = pos_x
        self.pos_y = pos_y

    def in_area(self, x_1, y_1, x_2, y_2):
        pass


class Dragon(Unit):
    def __init__(self, name, pos_x, pos_y, height, width, fire_range):
        super().__init__(name, pos_x, pos_y)
        self.fire_range = fire_range
        self.height = height
        self.width = width
        self.__hit_box = Rectangle(
            pos_x - width / 2, pos_y - height / 2, pos_x + width / 2, pos_y + height / 2
        )

    def in_area(self, x_1, y_1, x_2, y_2):
        area = Rectangle(x_1, y_1, x_2, y_2)
        return self.__hit_box.overlaps(area)


# Don't touch below this line


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
