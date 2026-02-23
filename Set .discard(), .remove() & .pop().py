n = int(input())
s = set(map(int, input().split()))
command= int(input())

for i in range(command):
     x=input().split()
     if x[0]== "pop":
        s.pop()
     if x[0]== "remove":
        s.remove(int(x[1]))
     if x[0]=="discard":
        s.discard(int(x[1]))

print(sum(s))