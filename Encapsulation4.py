#Special Case: Double Underscores at the Front and End
class Test:
    def __init__(self,x,y):
        self.__X=x
        self.__Y__=y
    
    def fun(self):
        print(self.__X)
        print(self.__Y__)
        print("Hii *_*")

t=Test(5,10)
#print(t.__X)
print(t.__Y__)
t.fun()