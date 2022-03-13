class s:
    def __init__(self):
        self.s = input()
    def isPalindrome(self):
        x = ""
        for i in self.s:
            x = i + x
        
        if(self.s == x):
            print("palindrome")
        else:
            print("not")

new = s()
new.isPalindrome()