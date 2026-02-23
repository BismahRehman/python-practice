n= int (input())
n_student=list(map(int,input().split()))
b= int (input())
b_student=list(map(int,input().split()))

print(len(set(set(n_student).intersection(set(b_student)))))
