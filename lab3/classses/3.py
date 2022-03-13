class Shape:
    def area(S = 0):
        print(S)
class Square(Shape):
    def __init__(self, length):
        self.length = length
    def area(self):
        print(self.length * self.length)
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        print(self.length * self.width)


l = float(input())
w = float(input())
a = Rectangle(l, w)
a.area()
