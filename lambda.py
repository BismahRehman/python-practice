#Use lambda to square all elements in a list using map().
number = [1, 2, 3, 4, 5, 6 ]
square = list(map(lambda number : number * number,number))
print (square)

#Use lambda to filter all odd numbers from a list using filter().
number = [1, 2, 3, 4, 5, 6 ]
square = list(filter(lambda number : (number%2)==0,number))
print (square)
#Write a higher-order function apply_func(func, value) that applies a function to value.
