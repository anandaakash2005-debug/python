class Employee:
    def fun(self):
        print("fun() is an Employee")

class Customer:
    def fun(self):
        print("fun() is a customer")

l=[Employee(),Customer()]

for x in l:
    x.fun()