from abc import ABC,abstractmethod

class Vehical(ABC):
    @abstractmethod
    def start_engine(self):
        pass

class car(Vehical):
    def start_engine(self):
        print("Engine started by key or button")

my_car=car()
my_car.start_engine()