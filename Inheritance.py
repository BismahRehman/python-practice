class Person:
    def __init__(self,name,age):
       self.name=name 
       self.age=age
    
    def show_info(self):
        print(self.name)
        print(self.age)

class Student(Person):
    def __init__(self,student_id,name,age):
       super().__init__(name,age) 
       self.student_id=student_id
        

    def study(self):
        print (f"Student {self.name} is studying")

    def show_info(self):
        print (self.student_id)

class Teacher(Person):
        def __init__(self,subject,name,age):
          self.subject=subject
          super().__init__(name,age)  

        def teach(self):
           print( f"Teacher {self.name} is teaching {self.subject}")

s=Student(1,"ali",5)
t= Teacher("eng","ahmad",23)
s.study()
s.show_info()
t.teach()
t.show_info()
