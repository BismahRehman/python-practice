#Given the names and grades for each student in a class of N students,
#  store them in a nested list and print the name(s) of any student(s)
#  having the second lowest grade.
student = []

for i in range(int(input())):
        name = input()
        score = float(input())
        student.append([])
        student[i].append(name)
        student[i].append(score)


  
sort_grade = sorted( set ( score for name , score  in student ))
second_lowest = sort_grade[1]

result =[ name for name , score in student if score == second_lowest ]
 
for name in sorted(result):
    print(name)
 