class Bank_Account:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def info(self):
        print(self.owner)
    def deposit(self):
        print("Your balance:", self.balance)
    def withdraw(self):
        a = float(input("How much you bring: "))
        self.balance -= a
    def add(self):
        b = float(input("How much you add: "))
        self.balance += b

Me = Bank_Account("Khalel Sanzhar", 0)

Me.info()
while True:
    s = input()
    if (s == "withdraw"):
        Me.withdraw()
        Me.deposit()
        continue
    elif (s == "add"):
        Me.add()
        Me.deposit()
        continue
    elif (s == "depo"):
        Me.deposit()
        continue
    