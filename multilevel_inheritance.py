class Person:
    def __init__(self,name,id):
        self.name=name
        self.id=id

    def printDetails(self):
        print(f"{self.name} is my name")
        print(f"{self.id} is my id number")

class Employee(Person):
    def __init__(self,name,id,salary):
        super().__init__(name,id)
        self.salary=salary

    def printDetails(self):
        super().printDetails()
        print(f"{self.salary}₹ LPA pls keep it secret")

class Sales_Employee(Employee):
    def __init__(self, name, id, salary,year):
        super().__init__(name, id, salary)
        self.year=year

    def printDetails(self):
        super().printDetails()
        print(f"{self.year} in this year i was joined")

sl=Sales_Employee("Akash",101,1500000,2028)

sl.printDetails()