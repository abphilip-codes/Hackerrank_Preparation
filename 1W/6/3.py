# https://www.hackerrank.com/challenges/one-week-preparation-kit-jesse-and-cookies/problem

#!/bin/python3

import math
import os
import random
import re
import sys
import heapq

#
# Complete the 'cookies' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#

def cookies(k, A, z=0):
    heapq.heapify(A)
    while True:
        a = heapq.heappop(A)
        if(a>=k): return z
        if(len(A)==0): return -1
        b = heapq.heappop(A)
        heapq.heappush(A,(a+2*b))
        z+=1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    A = list(map(int, input().rstrip().split()))

    result = cookies(k, A)

    fptr.write(str(result) + '\n')

    fptr.close()