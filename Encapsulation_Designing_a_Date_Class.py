class Date:
    def __init__(self,dd,mm,yyyy):
        self.__dd = dd
        self.__mm = mm
        self.__yyyy = yyyy

    def get(self):
        print(self.__dd)
        print(self.__mm)
        print(self.__yyyy)

d=Date(19,10,2005)
d.get()