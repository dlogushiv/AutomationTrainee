from OOP.Figures.Figure import Figure


class Square(Figure):
    def __init__(self, side):
        self.side = side

    def perimeter(self):
        return 4 * self.side

    def square(self):
        return self.side ** 2
