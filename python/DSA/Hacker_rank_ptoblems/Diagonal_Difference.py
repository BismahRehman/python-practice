#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    primary_diagonl= 0
    secondary_diagonal =0
    for i in range(len(arr[0])):
        for j in range(len(arr)):
            if i==j:
                primary_diagonl +=arr[i][j]
        for j in range(len(arr)):
            if i+j== len(arr)-1:
                secondary_diagonal +=arr[i][j]
                
    difference = primary_diagonl- secondary_diagonal
    if difference <0:
        difference = - difference
    
    return difference
             
            
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
