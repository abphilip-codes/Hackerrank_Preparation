# https://www.hackerrank.com/challenges/three-month-preparation-kit-cube-summation/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cubeSum' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING_ARRAY operations
#

def cubeSum(n, ops):
    ans = []
    base = dict()
    for a in ops:
        a = a.split()
        if(a[0]=="UPDATE"):
            x,y,z,w = [int(p) for p in a[1:]]
            base[(x,y,z)] = w
        else:
            r = [int(p) for p in a[1:]]
            X,Y,Z = [range(r[z],r[z+3]+1) for z in range(3)]
            ans.append(sum(base[(x,y,z)] for x,y,z in base if(x in X and y in Y and z in Z)))
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        first_multiple_input = input().rstrip().split()

        matSize = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        ops = []

        for _ in range(m):
            ops_item = input()
            ops.append(ops_item)

        res = cubeSum(matSize, ops)

        fptr.write('\n'.join(map(str, res)))
        fptr.write('\n')

    fptr.close()