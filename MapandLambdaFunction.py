cube = lambda x: x*x*x # complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    a= 0
    b=1
    li=[]
    for i in range(n):
        li.append(a)
        tem=a+b
        a=b
        b=tem
    return li
        
if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
