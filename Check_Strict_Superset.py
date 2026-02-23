# Enter your code here. Read input from STDIN. Print output to STDOUT
A= set(map(int,input().split()))
n= int(input())
a=0
for i in range(n):
    B= set(map(int,input().split()))
    if A.issuperset(B):
        a=a+1

if a==n:
    print("True")
else:
    print("False")
        
        
    