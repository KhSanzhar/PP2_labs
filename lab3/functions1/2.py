class Celcium:
    def __init__(self, farengeit):
        self.farengeit = farengeit
    def convert(self):
        print(str((5/9)*(self.farengeit - 32)) + ' celcium')

Faregeit = float(input('farengeit: '))
C = Celcium(Faregeit)
C.convert()