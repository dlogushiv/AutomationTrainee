from OOP.Figures.Circle import Circle
from OOP.Figures.Ellipse import Ellipse
from OOP.Figures.Rectangle import Rectangle
from OOP.Figures.Square import Square
from OOP.Figures.Triangle import Triangle
from OOP.Figures.EquilateralTriangle import EquilateralTriangle
from OOP.Figures.IsoscelesTriangle import IsoscelesTriangle

circle1 = Circle(r=10)
print('Circle perimeter and square:')
print(circle1.perimeter())
print(circle1.square())

triangle1 = Triangle(10, 12, 30)
print('Triangle perimeter and square:')
print(triangle1.perimeter())
print(triangle1.square())

eqTriangle1 = EquilateralTriangle(12)
print('Equilateral Triangle perimeter and square:')
print(eqTriangle1.perimeter())
print(eqTriangle1.square())

isoTriangle1 = IsoscelesTriangle(12, 5)
print('Isosceles Triangle perimeter and square:')
print(isoTriangle1.perimeter())
print(isoTriangle1.square())

ellipse1 = Ellipse(30, 20)
print('Ellipse perimeter and square:')
print(ellipse1.perimeter())
print(ellipse1.square())

rectangle1 = Rectangle(3, 4)
print('Rectangle perimeter and square:')
print(rectangle1.perimeter())
print(rectangle1.square())

square1 = Square(3)
print('Square perimeter and square:')
print(square1.perimeter())
print(square1.square())
