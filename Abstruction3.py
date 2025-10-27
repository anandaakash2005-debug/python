from abc import ABC,abstractmethod

class Employee(ABC):
    def __init__(self,name,id):
        self.Name=name
        self.id=id

    @abstractmethod
    def raise_salary(self):
        pass

    @abstractmethod
    def change_dept(self):
        pass

class sales_Employee(Employee):
    def raise_salary(self):
        print("Raise salary based on sales performance")

    def change_dept(self,new_dept):
        print(f"changing deperment to {new_dept}")

class software_Employee(Employee):
    def raise_salary(self):
        print("Raise salary based on code contribution")

    def change_dept(self,new_dept):
        print(f"changing deprtment to {new_dept}")

sales_emp=sales_Employee("Rahul",101)
sales_emp.raise_salary()
sales_emp.change_dept("Marketing")

software_emp=software_Employee("priya",102)
software_emp.raise_salary()
software_emp.change_dept("AI Development")