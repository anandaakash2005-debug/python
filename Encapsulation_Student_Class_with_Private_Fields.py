class Student:
    def __init__(self,marks):
        self.set_marks(marks)  # ✅ call setter inside constructor

    def set_marks(self,marks):
        if 0 <= marks <= 100:
            self.__marks=marks

        else:
            raise ValueError("Marks must be between o to 100")
        
    def get_marks(self):
        print(self.__marks)

s=Student(95)
s.get_marks()

s1=Student(120)
s1.get_marks()

s.set_marks(59)
s.get_marks()