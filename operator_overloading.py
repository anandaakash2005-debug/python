class point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __add__(self,other):
        return point(self.x+other.x , self.y+other.y)
    
    def __str__(self):
        return f"{self.x},{self.y}"
    
p1=point(4,5)
p2=point(9,13)

p3=p1+p2

print(p3)