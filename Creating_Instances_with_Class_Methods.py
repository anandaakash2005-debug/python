from datetime import date
class Employee:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    @classmethod
    def from_birth_year(cls,name,year):
        return cls(name,date.today().year-year)
    
e=Employee.from_birth_year("Akash",2005)
print(e.name)
print(e.age)