class student:
    collage_name="MAKAUT"

    def __init__(self,name,roll):
        self.name=name
        self.roll=roll

    def details(self):
        print(f"Name:{self.name}")
        print(f"Roll:{self.roll}")

    @classmethod
    def change_collage(cls,clg):
        cls.collage_name=clg

    @staticmethod
    def ispass(marks):
        return marks > 40
    
s1=student("Akash",101)
s2=student("Ananda",102)
s1.details()
s2.details()
s1.change_collage("TBIT")
print(s1.collage_name)
print(s2.collage_name)
print(s1.ispass(45))
print(s2.ispass(45))