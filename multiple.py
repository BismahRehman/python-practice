#Write a function info(*args, ****kwargs) to print all arguments and keyword arguments.
def info(*args, **kwargs):
    print (args)
    print (kwargs)
info (1, 2, 3, 4,5 , ali= 123, ahmad= 1234 )