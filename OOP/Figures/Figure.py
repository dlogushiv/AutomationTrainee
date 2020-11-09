class Figure:
    def __init__(self, name, colour):
        self.name = name
        self.colour = colour

    def call_me(self):
        print('Hello, I am a %s.' % self.name, 'My favorite colour is %s.' % self.colour)

    def perimeter(self):
        pass

    def square(self):
        pass
