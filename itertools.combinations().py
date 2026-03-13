# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
string= input().split()



for i in range(1,int(string[1])+1):
    a=list(combinations(sorted(string[0]),i))
    for i in a:
        print("".join(i))
