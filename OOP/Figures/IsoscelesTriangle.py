from math import sqrt

from OOP.Figures.Figure import Figure


class IsoscelesTriangle(Figure):
    def __init__(self, side, base):
        self.side = side
        self.base = base

    def perimeter(self):
        return 2 * self.side + self.base

    def square(self):
        return 0.25 * self.base * sqrt(4 * self.side ** 2 - self.base ** 2)
