# Enter your code here. Read input from STDIN. Print output to STDOUT
m= int(input())
a= list(map(int,input().split()))
n=int(input())
b= list(map(int,input().split()))
list1=[]
for i in a :
    if i not in b:
        list1.append(i)
for i in b:
    if i not in a:
        list1.append(i)
list2=list(set(list1))
list2.sort()
for i in list2:
    print (i)