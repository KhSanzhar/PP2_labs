class ounces:
    def __init__(self, grams):
        self.grams = grams
    def convert(self):
        print(28.3495231*self.grams)

gram = float(input())
g = ounces(gram)
g.convert()