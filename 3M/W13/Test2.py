# Mock Test II

#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'findConnectedComponents' function below.
#
# The function is expected to return an INTEGER.
# The function accepts LONG_INTEGER_ARRAY d as parameter.
#
from itertools import combinations

def f(w, c=0):
    while w:
        if w&1: c+=1
        w>>=1
    return c

def findConnectedComponents(d, ans=0):
    d = list(set(d))
    for z in range(len(d)+1):
        for y in combinations(d,z):
            x,m = [],set(y)
            while m:
                s,k = m.pop(),[]
                for w in m:
                    if s&w:
                        s|=w
                        k.append(w)
                x.append(s)
                while(k): m.discard(k.pop())
            c = 0
            for w in x:
                while w:
                    if(w&1): c+=1
                    w>>=1
            ans+=len(x)-c+64
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    d_count = int(input().strip())

    d = list(map(int, input().rstrip().split()))

    components = findConnectedComponents(d)

    fptr.write(str(components) + '\n')

    fptr.close()