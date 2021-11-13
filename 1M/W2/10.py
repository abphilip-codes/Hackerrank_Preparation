# https://www.hackerrank.com/challenges/one-month-preparation-kit-sherlock-and-array/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'balancedSums' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def balancedSums(n, arr):
    a,b = 0,int(sum(arr[2:]))
    for z in range(1,n+1):
        if(a==b): return 'YES'
        a,b = a+arr[z],b-arr[z+1]
    else: return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = balancedSums(n, [0]+arr+[0])

        fptr.write(result + '\n')

    fptr.close()