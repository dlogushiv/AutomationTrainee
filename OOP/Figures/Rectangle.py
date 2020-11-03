from OOP.Figures.Figure import Figure


class Rectangle(Figure):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def perimeter(self):
        return 2 * self.height + 2 * self.width

    def square(self):
        return self.height * self.width
