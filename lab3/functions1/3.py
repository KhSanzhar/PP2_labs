class puzzle:
    def __init__(self, numheads, numlegs):
        self.numheads = numheads
        self.numlegs = numlegs
    def calculate(self):
        print("Chickens:", int((4*self.numheads - self.numlegs)/2))
        print("Rabits:", int((self.numlegs - 2*self.numheads)/2))

h, l = map(int, input().split())
sum = puzzle(h, l)
sum.calculate()
