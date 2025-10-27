class Employee:
    compname="google"
    def __init__(self,id):
        self.id=id

    def fun(self,n):
        self.name=n
    
e=Employee(1001)
e.fun("Akash")

print(e.id)
print(e.name)
print(e.compname)

e.designation="CEO"
print(e.designation)

Employee.compadd="Noida"
print(e.compadd)