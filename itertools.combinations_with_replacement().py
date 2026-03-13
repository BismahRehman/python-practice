# Enter your code here. Read input from STDIN. Print output to STDOUT
#my solution
from itertools import combinations_with_replacement
string = input().split()
combinations= combinations_with_replacement(sorted(string[0]),int(string[1]))
for i in combinations:
    print("".join(i))
    # print(i)
#  when single operation are perform  using loop then used list comprehension

#gpt  best solution
# 
# from itertools import combinations_with_replacement

# s, n = input().split()
# n = int(n)

# for combo in combinations_with_replacement(sorted(s), n):
#     print("".join(combo))
