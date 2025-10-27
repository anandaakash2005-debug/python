from abc import ABC,abstractmethod
class Shape(ABC):
    def __init__(self,color):
        self.color=color

    @abstractmethod
    def get_area(self):
        pass

    def get_color(self):
        return self.color
    
class Square(Shape):
    def __init__(self,color,side):
        super().__init__(color)
        self.side=side

    def get_area(self):
        return self.side*self.side

sq=Square("Red",5)
print(sq.get_color())
print(sq.get_area())