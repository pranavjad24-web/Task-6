class Person:
    def __init__(self, name):
        self.name = name


class Student(Person):
    def study(self):
        print(self.name, "is studying")


class Teacher(Person):
    def teach(self):
        print(self.name, "is teaching")


s = Student("Arun")
t = Teacher("Meena")

s.study()
t.teach()
