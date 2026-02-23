def merge_the_tools(string, k):
    # your code goes here
    n= len(string)//k
    a=0
    
    for i in range(n):
        s=string[a:a+k]
        a=a+k
        b=""
        for j in s:
            if j not in b:
                b=b+j
        print(b)
            
        