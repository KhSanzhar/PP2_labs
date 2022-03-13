from math import pi
class volumes:
    def __init__(self):
        self.radius = float(input())
    def sphere(self):
        print((3/4)*pi*self.radius)

V = volumes()
V.sphere()