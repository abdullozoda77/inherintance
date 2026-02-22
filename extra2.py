class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    @property
    def owner(self):
        return self.__owner
    @property
    def balance(self):
        return self.__balance
    @owner.setter
    def owner(self ,value):
        if not value:
            print("EMPTY")
        else:
            self.__owner = value
    @balance.setter
    def balance(self, value):
        if value < 0 :
            print("Minus")
        else:
            self.__balance = value
ba_owner = input("enter owner --> ")
while True:
    ba_balance = int(input("enter balance --> "))
    if  ba_balance  >= 0:
        break
    print("Too less enter another number --> ")
ba1 = BankAccount(ba_owner, ba_balance)
print(ba_owner)
print(ba_balance)

