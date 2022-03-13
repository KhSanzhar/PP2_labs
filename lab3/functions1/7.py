class sem:
    def come(self):
        self.nums = list(map(int, input().split()))
    def has_33(self):
        for i in range(len(self.nums) - 1):
            if(self.nums[i] == 3 & self.nums[i + 1] == 3):
                return True
        return False

l = sem()
l.come()
if l.has_33() == True:
    print(True)
else:
    print(False)
