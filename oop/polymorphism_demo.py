import math

class Shape:
    def area(Self):
        raise NotImplementedError

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        area = self.width * self.length
        return area

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
      
    def area(self):
        area = math.pi * self.radius * self.radius
        return area