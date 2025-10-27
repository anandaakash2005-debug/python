class BankAccount:
    def __init__(self,Owner,Balance=0):
        self.Owner=Owner
        self.__Balance=Balance

    def get_Balance(self):
        print(self.Owner)
        print(self.__Balance)

    def deposite(self,Amount):
        if Amount > 0:
            self.__Balance+=Amount
            print("updated Balance is:",self.__Balance)
        
        else:
            raise ValueError("Amount must be greater than 0")
        
    def withdraw(self,Amount):
        if Amount <= 0:
            raise ValueError("Amount must be greater than 0")
        if self.__Balance < Amount:
            raise ValueError("Insufficient Balance")
        else:
            self.__Balance-=Amount
            print("updated Balance is:",self.__Balance)

    def Account_Summery(self):
        print("Account Owner:",self.Owner)
        print("Account Balance:",self.__Balance)

acc=BankAccount("Alice",1000)
acc.get_Balance()
acc.deposite(500)
acc.withdraw(2000)
acc.Account_Summery()