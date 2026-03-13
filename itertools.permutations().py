# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations
l= input().split()
a=sorted(list(permutations(l[0],int(l[1]))))
for i in a:
    print("".join(i))