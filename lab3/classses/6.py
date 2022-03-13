from math import sqrt
class filter:
    def __init__(self, number):
        self.number = number
        
    def is_Prime(self):
        self.ans = True
        for i in range(2, int(sqrt(self.number)) + 1):
            if self.number % i == 0:
                self.ans = False
                break
        
        if(self.ans == False):
            print('No')
        else:
            print('Yes')
    

while True:
    n = int(input())
    ans = filter(n)
    ans.is_Prime()
