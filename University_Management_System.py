class Person:
    university_name = "ABC University" 

    def __init__ (self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

    @classmethod
    def change_university(cls, new_name):
        cls.university_name = new_name


class Student(Person):
    def __init__(self, name, age, cgpa):
        super().__init__(name, age)
        self.__cgpa = cgpa

    @property
    def cgpa(self):
        if  0 < self.__cgpa < 4:
            return self.__cgpa
        print("Your CGPA is invalid")
        return None

    def study(self):
        print(f"{self.name} is studying")


class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def teach(self):
        print(f"{self.name} teaches {self.subject}")


class Researcher:
    def do_research(self):
        print(f"{self.name} is doing research")


class TeachingAssistant(Student, Researcher):
    def __init__(self, name, age, cgpa):
        Student.__init__(self, name, age, cgpa)


# Create objects
s = Student("Ali", 22, 3.0)
t = Teacher("Ahmad", 30, "English")
ta = TeachingAssistant("Sara", 24, 3.5)

# Call methods
s.show_info()
s.study()
print(f"CGPA: {s.cgpa}\n")

t.show_info()
t.teach()


ta.show_info()
ta.study()
ta.do_research()
print(f"CGPA: {ta.cgpa}\n")

# University info
print("Before change:")
print(s.university_name)
print(t.university_name)
print(ta.university_name)

Person.change_university("XYZ University")

print("\nAfter change:")
print(s.university_name)
print(t.university_name)
print(ta.university_name)
