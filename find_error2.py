from math import pi


class Shape:
    def area(self):
        raise NotImplemented

    def circumference(self):
        raise NotImplemented

    def __str__(self):
        return type(self).__name__

class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        print(pi * self.r ** 2)

    def circumference(self):
        return 2 * pi * self.r


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        print(self.length * self.width)

    def circumference(self):
        return 2 * self.length + 2, self.width


class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)
shapes = [Square(10), Circle(20), Rectangle(3.4, 1.5)]
for shape in shapes:
    print(f'{shape} area is {shape.area()}')
