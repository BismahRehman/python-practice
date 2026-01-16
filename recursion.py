#Write a function factorial(n) using normal recursion.

def fac (n):
    if n==0:
       return 1
    return n *fac(n-1)
number = int ( input (  " Enter a number "))
 
result = fac( number)
print ( result)
