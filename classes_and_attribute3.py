class Employee:
    compadd="noida"
    compname="gfg"
    def __init__(self,id):
        self.id=id

#Employee.compadd="noida"
e=Employee(1001)
e.compadd="india"
print(e.id)
print(Employee.compadd)
print(e.compadd)
print(e.compname)