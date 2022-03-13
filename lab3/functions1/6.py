class zad:
    def come(self):
        self.str = input().split()
    def rev(self):
        self.new = self.str.reverse()
        print(self.new, sep = ' ')

s = zad()
s.come()
s.rev()