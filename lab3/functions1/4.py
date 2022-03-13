from math import sqrt

class prime:
    def come(self):
        self.numbers = list(map(int, input().split()))
    def identification(self):
        for i in self.numbers:
            for j in range(2,int(sqrt(i)) + 1):
                if i % j == 0:
                    self.numbers.remove(i)
    def p(self):
        print(self.numbers)

l = prime()
l.come()
l.identification()
l.p()
    