from itertools import permutations

class next:
    permlist = []
    def fis(self):
        self.str = input()
    def allpermutations(self):
        permlist = permutations(sorted(self.str))
        

        for i in permlist:
            print(''.join(i))

a = next()
a.fis()
a.allpermutations()