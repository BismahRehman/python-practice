#Write a function is_even(n) that returns True if a number is even.
def is_even(n):
   if n%2 == 0:
      return True
   else :
      return False
   
number = int( input ( " enter a number "))
result =is_even ( number)
print (result)