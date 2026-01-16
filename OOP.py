class student():
  def __init__ (self, name, rollno, marks):
    self.name = name 
    self.rollno = rollno
    self.marks = marks


students=[]
number= int(input("enter the number of student you want to enter"))
for i in range(number):
  list=input("enter the name , rollno and marks")
  list=list.split()
  name = str(list[0])
  rollno = list[1]
  marks = list[2]
  s = student(name, rollno, marks)
  students.append(s)

for s in students:
    print(s.name, s.rollno, s.marks)