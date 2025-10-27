class Animel:
    def __init__(self,name):
        self.name=name
    
    def speak(self):
        print("Animels can make sound")

class Dog(Animel):
    def speak(self):
        print(f"{self.name} says woof!")

class Cat(Animel):
    def speak(self):
        #return super().speak()
        print(f"{self.name} says Meow!")
    
d=Dog("Buddy")
d.speak()

c=Cat("Whiskers")
c.speak()