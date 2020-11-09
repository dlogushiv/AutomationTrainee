from OOP.Figures.Circle import Circle
from OOP.Figures.Ellipse import Ellipse
from OOP.Figures.Rectangle import Rectangle
from OOP.Figures.Square import Square
from OOP.Figures.Triangle import Triangle
from OOP.Figures.EquilateralTriangle import EquilateralTriangle
from OOP.Figures.IsoscelesTriangle import IsoscelesTriangle

circle1 = Circle(name='C1', colour='red', r=10)
circle1.call_me()
print('Circle perimeter and square:')
print(circle1.perimeter())
print(circle1.square())

triangle1 = Triangle(name='DifSide', colour='black', a=10, b=12, c=14)
triangle1.call_me()
print('Triangle perimeter and square:')
print(triangle1.perimeter())
print(triangle1.square())

eqTriangle1 = EquilateralTriangle(name='OneSide', colour='brown', side=12)
eqTriangle1.call_me()
print('Equilateral Triangle perimeter and square:')
print(eqTriangle1.perimeter())
print(eqTriangle1.square())

isoTriangle1 = IsoscelesTriangle(name='TwoSide', colour='orange', side=12, base=5)
isoTriangle1.call_me()
print('Isosceles Triangle perimeter and square:')
print(isoTriangle1.perimeter())
print(isoTriangle1.square())

ellipse1 = Ellipse(name='Elli', colour='indigo', width=30, height=20)
ellipse1.call_me()
print('Ellipse perimeter and square:')
print(ellipse1.perimeter())
print(ellipse1.square())

rectangle1 = Rectangle(name='Block', colour='yellow', height=3, width=4)
rectangle1.call_me()
print('Rectangle perimeter and square:')
print(rectangle1.perimeter())
print(rectangle1.square())

square1 = Square(name='Kubi', colour='blue', side=3)
square1.call_me()
print('Square perimeter and square:')
print(square1.perimeter())
print(square1.square())
