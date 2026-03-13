from itertools import product
A= list(set(map(int, input().split())))
B= list(set(map(int, input().split())))
l=list(product(A,B))
for i in l:
    print(i,end=" ")
