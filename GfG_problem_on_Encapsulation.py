class People:
    def __init__(self):
        self.__name="Geeks"
        self.__age=10

    def set_name(self,name):
        self.__name=name

    def set_age(self,age):
        self.__age=age

    def get_name(self):
        return self.__name
    
    def get_age(self):
        return str(self.__age)
    
p=People()
ans=[]
ans.append(p.get_name())
p.set_name("Akash")
p.set_age(20)
ans.append(p.get_name())
ans.append(p.get_age())
print("".join(ans))