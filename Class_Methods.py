class Employee:
    comp_name="GfG"
    def __init__(self,name,id):
        self.name=name
        self.id=id
    @classmethod
    def setcomp_name(cls,comp):
        cls.comp_name=comp

Employee.setcomp_name("Google")
print(Employee.comp_name)

e=Employee("sandeep",41)
print(e.comp_name)