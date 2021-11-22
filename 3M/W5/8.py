# https://www.hackerrank.com/challenges/three-month-preparation-kit-sansa-and-xor/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sansaXor' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def sansaXor(n, arr):
    ans=arr[0]
    if(n%2!=0):
        for z in range(2,n,2): ans^=arr[z]
        return ans
    return 0

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = sansaXor(n, arr)

        fptr.write(str(result) + '\n')

    fptr.close()