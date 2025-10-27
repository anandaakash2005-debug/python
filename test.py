class BankAccount:
    def __init__(self,name,id,balance=0):
        self.name=name
        self.id=id
        self.__balance=balance

    def Details(self):
        print(f"Name:{self.name}")
        print(f"ID:{self.id}")
        print(f"Balance:{self.__balance}")

    def debit(self,money):
        if money <= 0:
            print("not sufficient money") 

        else:
            self.__balance+=money
            print(self.__balance)
            print("sucessfully debited")
    
    def withdraw(self,money):
        if money <= 0:
            print("can't be withdraw")

        if self.__balance < money:
            print("not sufficient money in your Accounce")

        else:
            self.__balance -= money
            print("successfully Withdrawed")
    
b=BankAccount("Akash",101,10000)
b.Details()
b.debit(100)
b.withdraw(40)
b.withdraw(2000)
b.Details()