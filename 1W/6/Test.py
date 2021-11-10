# Mock Test

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque

#
# Complete the 'bfs' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#  3. 2D_INTEGER_ARRAY edges
#  4. INTEGER s
#

def bfs(n, m, edges, s):
    g = {}
    for z in range(1, n+1): g[z] = set()
    for l,r in edges:
        g[l].add(r)
        g[r].add(l)
    x,w,d = {},{s},deque([(s,0)])
    while(d):
        cn,cc = d.popleft()
        for z in g[cn]:
            if z not in w:
                w.add(z)
                x[z] = cc+6
                d.append((z,cc+6))
    return [x.get(z,-1) for z in range(1,n+1) if(s!=z)]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        edges = []

        for _ in range(m):
            edges.append(list(map(int, input().rstrip().split())))

        s = int(input().strip())

        result = bfs(n, m, edges, s)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()