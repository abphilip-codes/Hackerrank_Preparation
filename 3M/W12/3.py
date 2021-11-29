# https://www.hackerrank.com/challenges/three-month-preparation-kit-primsmstsub/problem

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

#
# Complete the 'prims' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY edges
#  3. INTEGER start
#

def prims(n, edges, start, ans=0):
    A,B,C = {start}, defaultdict(set), defaultdict(int)
    for x,y,z in edges : 
        k = frozenset({x,y}) 
        if y in B[x]: C[k] = min(C[k], z) 
        else: 
            B[x].add(y)
            B[y].add(x)
            C[k] = z 
    while(len(A)<n): 
        a,b = min((C[frozenset({x,y})],y) for x in A for y in B[x]-A)
        ans+=a
        A.add(b)
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    edges = []

    for _ in range(m):
        edges.append(list(map(int, input().rstrip().split())))

    start = int(input().strip())

    result = prims(n, edges, start)

    fptr.write(str(result) + '\n')

    fptr.close()