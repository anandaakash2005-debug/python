class Dog:
    def sound(self):
        return "berk!!"
    
class Cat:
    def sound(self):
        return "meow!!"
    
def make_sound(Animel):
    print(Animel.sound())
    
dog=Dog()
cat=Cat()

make_sound(dog)
make_sound(cat)