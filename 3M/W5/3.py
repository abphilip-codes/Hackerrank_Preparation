# https://www.hackerrank.com/challenges/three-month-preparation-kit-dynamic-array/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamicArray(n, queries):
    s,last,ans = [[] for z in range(n)],0,[]
    for q in queries:
        i = (q[1] ^ last) % n
        if q[0]!=1:
            pos = q[2] % len(s[i])
            last = s[i][pos]
            ans.append(last)
        else: s[i].append(q[2])
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()