from OOP.Figures.Triangle import Triangle


class EquilateralTriangle(Triangle):
    def __init__(self, name, colour, side):
        super().__init__(name, colour, a=side, b=side, c=side)
        self.side = side
