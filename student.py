class Student:
    def __init__(self, name, eng, urdu, math):
        self.name=name
        self.eng= eng
        self.urdu=urdu
        self.math=math

    def avg(self):
        avg=(self.eng + self.urdu + self.math)/3
        print (avg)
s1 = Student("ali", 50, 49, 50)

s1.avg()     
