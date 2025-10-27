class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def info(self):
        print(f"My name:{self.name} and my age:{self.age}")

class EmployeeDetails:
    def __init__(self,salary,pos):
        self.salary=salary
        self.position=pos

    def job_info(self):
        print(f"i got {self.salary}₹ LPA and my position {self.position}")

class Employee(Person,EmployeeDetails):
    def __init__(self, name, age,salary,pos):
        Person.__init__(self,name, age)
        EmployeeDetails.__init__(self,salary,pos)

    def details(self):
        self.info()
        self.job_info()

e=Employee("Akash",20,1500000,"Software Engineer")
e.details()