from OOP.Figures.Triangle import Triangle


class IsoscelesTriangle(Triangle):
    def __init__(self, name, colour, side, base):
        super().__init__(name, colour, a=side, b=side, c=base)
        if base <= 2 * side:
            self.side = side
            self.base = base
            self.created = True
        else:
            self.created = False
            print('Impossible to create new triangle. Check the sides values.')
