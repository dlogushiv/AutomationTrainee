from math import sqrt

from OOP.Figures.Figure import Figure


class EquilateralTriangle(Figure):
    def __init__(self, side):
        self.side = side

    def perimeter(self):
        return 3 * self.side

    def square(self):
        return self.side * self.side * sqrt(3) * 0.25
