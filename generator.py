# #Write a generator fib(n) to yield first n Fibonacci numbers. 
def fib(n):
   
    a=0 
    b= 1
    for i in range(n):
       
        yield a
        tem=b+a
        a=b
        b = tem  

n =int(input("enter a number "))



for i in fib(n):
    print (i)







