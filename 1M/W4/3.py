# https://www.hackerrank.com/challenges/one-month-preparation-kit-lego-blocks/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'legoBlocks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#

def legoBlocks(n, m, M=1000000007):
    a=[0,1,2,4,8]
    for z in range(5,m+1):  a.append((a[z-1]+a[z-2]+a[z-3]+a[z-4])%M)
    for z in range(m+1): a[z] = pow(a[z],n,M)
    r = [a[z] for z in range(m+1)]
    for z in range(1,m+1):
        for y in range(1,z): r[z]-=(r[y]*a[z-y])
        r[z] = r[z]%M
    return r[m]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        result = legoBlocks(n, m)

        fptr.write(str(result) + '\n')

    fptr.close()