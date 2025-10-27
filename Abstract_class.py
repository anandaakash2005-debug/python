from abc import ABC,abstractmethod
class polygon(ABC):
    def __init__(self,color):
        self.color=color
    
    @abstractmethod
    def printside(self):
        pass

class Triangle(polygon):
    def __init__(self, color):
        super().__init__(color)

    def printside(self):
        print("There are three sides")

b=Triangle("Red")
b.printside()