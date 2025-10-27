class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    @staticmethod
    def isAdult(age):
        return age>18
    
    def print_details(self):
        print("Name :",self.name)
        print("Age:",self.age)
        print("voting Eligibility:",Person.isAdult(self.age))

p=Person("Akash",20)
p.print_details()