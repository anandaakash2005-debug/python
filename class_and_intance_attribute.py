class Employee:
    compname="gfg"
    def __init__(self,id):
        self.id=id

e1=Employee(1001)
e2=Employee(1002)

Employee.compname="geeksforgeeks"

print(e1.id)
print(e1.compname)
print(e2.id)
print(e1.compname)
print(Employee.compname)