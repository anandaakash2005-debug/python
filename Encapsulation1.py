#Public Members
#every member of a Python class is public, meaning it can be accessed from anywhere. Consider the following example:
class Test:
    def __init__(self,x,y):
        self.X=x
        self.Y=10

    def fun(self):
        print(self.X)
        print(self.Y)
        print("Hii")

t=Test(5,10)
print(t.X)
print(t.Y)
t.fun()