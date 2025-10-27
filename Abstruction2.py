from abc import ABC,abstractmethod

class shape(ABC):

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def get_area(self):
        pass

class rectangle(shape):

    def draw(self):
        print("Drawing rectangle")

    def get_area(self,length,breadth):
        return length*breadth
        
class circle(shape):

    def draw(self):
        print("drawing a circle")

    def get_area(self,radious):
        return 3.14*radious*radious
    
rect=rectangle()
rect.draw()
print(rect.get_area(4,5))

cir=circle()
cir.draw()
print(cir.get_area(5))