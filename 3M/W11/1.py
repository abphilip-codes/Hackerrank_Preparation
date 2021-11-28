# https://www.hackerrank.com/challenges/three-month-preparation-kit-queries-with-fixed-length/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER_ARRAY q
#

def solve(arr, q, ans=[]):
    for z in range(len(q)):
        x = m = 0
        for y in range(len(arr)):
            m = max(arr[y],m)
            if((y>=q[z]) and (arr[y-q[z]]==m)): 
                m = max(arr[y-q[z]+1:y+1])
            if((y>=q[z]-1) and (x==0 or x>m)): x = m
        ans.append(x)
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    queries = []

    for _ in range(q):
        q_item = int(input().strip())
        queries.append(q_item)

    result = solve(arr, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()