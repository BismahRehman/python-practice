n = int(input())
arr = list(map(int, input().split()))

m = arr[0]
r = arr[0]

for x in range(len(arr)):
    if  m < arr[x]:
        m = arr[x]
    if  arr[x] < r:
        r = arr[x]
for x in range(len(arr)):
    
    if   arr[x]  >r :
       if arr[x] <m :
          r = arr[x]
    
print ( r)