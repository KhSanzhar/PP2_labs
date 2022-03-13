from math import sqrt
class Point:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
    def show(self):
        print("Before:", self.x1, self.y1)
    def move(self):
        print("After:", self.x2, self.y2)
    def dist(self):
        self.d = sqrt(pow(self.x2 - self.x1, 2) + pow(self.y2 - self.y1, 2))
        print(self.d)

x1, y1, x2, y2 = map(float, input().split())
S = Point(x1, y1, x2, y2)

S.show()
S.move()
S.dist()