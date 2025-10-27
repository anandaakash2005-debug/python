from abc import ABC,abstractmethod

class polygon(ABC):
    def __init__(self,color):
        self.color=color
    
    @abstractmethod
    def print_sides(self):
        pass

class Triangle(polygon):
    def __init__(self,color):
        super().__init__(color)

    

b=Triangle("Red")
b.print_sides()