# https://www.hackerrank.com/challenges/three-month-preparation-kit-pylons/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pylons' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def pylons(k, arr, l=1, c=1):      
    for a in range(k-1,-1,-1):
        if arr[a]==1:
            l=0
            break
    if(l): return -1

    while(a<len(arr)-k):
        a,l = a+2*(k-1)+1,1
        for z in range(2*(k-1)+1):
            if arr[min(a-z,len(arr)-1)]==1:
                c,a,l = c+1,a-z,0
                break
        if(l): return -1
    return c

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = pylons(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()