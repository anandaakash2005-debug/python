class person:
    def __init__(self,id,name):
        self.id=id
        self.name=name

class Employee(person):
    def __init__(self,id,name,salary):
        #super().__init__(id,name)
        self.salary=salary

    def details(self):
        print(self.id)
        print(self.name)
        print(self.salary)

class Student(person):
    def __init__(self,id,name,marks):
        #super().__init__(id,name)
        self.marks=marks

    def details(self):
        print(self.id)
        print(self.name)
        print(self.marks)

s=Student(101,"Akash",89)
s.details()

e=Employee(41,"ananda",10000)
e.details()