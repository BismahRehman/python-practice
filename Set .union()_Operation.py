# Enter your code here. Read input from STDIN. Print output to STDOUT

n= int (input())
n_student=list(map(int,input().split()))
b= int (input())
b_student=list(map(int,input().split()))

print(len(set(set(n_student).union(set(b_student)))))
