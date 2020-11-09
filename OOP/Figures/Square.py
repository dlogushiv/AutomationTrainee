from OOP.Figures.Rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, name, colour, side):
        super().__init__(name, colour, height=side, width=side)
        self.side = side
