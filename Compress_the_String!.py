from itertools import groupby
string= input()
for key,group in groupby(string):
    print(f"({sum(1 for _ in group)}, {key})",end=" ")