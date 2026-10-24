class Account:
    def setAmount(self,amount):
        self.amount = amount

    def getAmount(self):
        return self.amount

    def setName(self,name):
        self.name = name

    def getName(self):
        return self.name


obj = Account()

name = input("Enter your name:")
amount = int(input("Enter amount:"))

obj.setName(name)
obj.setAmount(amount)

print(obj.getName())
print(obj.getAmount())