class Employee:
    def __init__(self,id,name):
        self.id=id
        self.name=name

    def details(self):
        print("My id is:",self.id)
        print("My name is:",self.name)
    
class SalesEmployee(Employee):
    def __init__(self,id,name,salary):
        super().__init__(id,name)
        self.salary=salary

    def details(self):
        super().details()
        print("My salary:",self.salary)

el=[Employee(101,"Akash") , SalesEmployee(102,"Ananda",10000)]

for x in el:
    x.details()