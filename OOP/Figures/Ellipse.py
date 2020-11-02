from OOP.Figures.Figure import Figure
from math import pi, sqrt


class Ellipse(Figure):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def perimeter(self):
        a = self.width // 2
        b = self.height // 2
        return 2 * pi * sqrt(0.5 * (a * a + b * b))

    def square(self):
        a = self.width // 2
        b = self.height // 2
        return pi * a * b
