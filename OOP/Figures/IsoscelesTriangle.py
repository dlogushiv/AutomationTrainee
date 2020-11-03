from math import sqrt

from OOP.Figures.Figure import Figure


class IsoscelesTriangle(Figure):
    def __init__(self, side, base):
        self.side = side
        self.base = base

    def perimeter(self):
        if self.created:
            return 2 * self.side + self.base
        else:
            return 0

    def square(self):
        if self.created:
            return 0.25 * self.base * sqrt(4 * self.side ** 2 - self.base ** 2)
        else:
            return 0
