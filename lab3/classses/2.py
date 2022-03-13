class Shape:
    def area(S = 0):
        print(S)
class Square(Shape):
    def __init__(self, length):
        self.length = length
    def area(self):
        print(self.length * self.length)


l = float(input())
a = Square(l)
a.area()
