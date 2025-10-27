#Private Members
#The third rule uses double underscores before a member name to make it private. This restricts access to the member from outside the class by performing name mangling.
class Test:
    def __init__(self,x,y):
        self.__X=x
        self.Y=y
    
    def fun(self):
        print(self.__X)
        print(self.Y)
        print("Hii")

t=Test(5,10)
#print(t.__X)
print(t.Y)
t.fun()