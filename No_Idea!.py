number = map(int, input().split())

n = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))
a=0
for i in n:
    if i in A and i not in B:
        a=a+1
    elif i in B  and i not in A:
        a= a-1 
    
print(a)       
 