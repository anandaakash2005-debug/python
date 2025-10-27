#Protected Members
#The second rule involves prefixing a variable name with a single underscore. This indicates that the member is intended for internal use within the class or its subclasses, but Python does not enforce this restriction.
class Test:
    def __init__(self,x,y):
        self._X=x
        self.Y=y

    def fun(self):
        print(self._X)
        print(self.Y)
        print("Hii")

t=Test(5,10)
print(t._X)
print(t.Y)
t.fun()