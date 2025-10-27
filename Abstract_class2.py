from abc import ABC,abstractmethod

class polygon(ABC):
    def __init__(self,color):
        self.color=color

    @abstractmethod
    def print_sides(self):
        pass

    def print_color(self):
        print(self.color)

class Triangle(polygon):
    def __init__(self, color):
        super().__init__(color)

    def print_sides(self):
        print("3 sides")

b=Triangle("Red")
b.print_sides()
b.print_color()