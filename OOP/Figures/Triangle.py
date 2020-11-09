from math import sqrt

from OOP.Figures.Figure import Figure


class Triangle(Figure):
    def __init__(self, name, colour, a, b, c):
        super().__init__(name, colour)
        sides = [a, b, c]
        m = max(sides)
        sides.pop(sides.index(m))
        if m < sum(sides):
            self.a = a
            self.b = b
            self.c = c
            self.created = True
        else:
            self.created = False
            print('Impossible to create new triangle. Check the sides values.')

    def perimeter(self):
        if self.created:
            return self.a + self.b + self.c
        else:
            return 0

    def square(self):
        if self.created:
            hp = self.perimeter() // 2
            return sqrt(hp * (hp - self.a) * (hp - self.b) * (hp - self.c))
        else:
            return 0
