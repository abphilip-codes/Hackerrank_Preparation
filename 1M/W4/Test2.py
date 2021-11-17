# Mock Test II

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'componentsInGraph' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts 2D_INTEGER_ARRAY gb as parameter.
#

def componentsInGraph(gb):
    def p(k, z):
        if k[z] != z:
            k[z] = p(k, k[z])
        return k[z]
    k = list(range(len(gb)*2+1))
    for a, b in gb:
        p1, p2 = p(k,a), p(k,b)        
        k[p1] = k[p2] = k[a] = k[b] = min(p1, p2)
    c = Counter()
    for z in k: c[p(k,z)]+=1
    ans = [z for z in c.values() if(z>1)]
    return min(ans), max(ans)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    gb = []

    for _ in range(n):
        gb.append(list(map(int, input().rstrip().split())))

    result = componentsInGraph(gb)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()