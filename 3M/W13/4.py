# https://www.hackerrank.com/challenges/three-month-preparation-kit-journey-to-the-moon/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'journeyToMoon' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY astronaut
#

def journeyToMoon(n, astronaut, k=[]):
    for z in range(len(astronaut)):
        a,b = astronaut[z]
        s,t = 0,set()
        
        while(s<len(k)):
            if a in k[s] or b in k[s]:
                t = t.union(k[s])
                del k[s]
            else: s+=1
        t = t.union([a, b])
        k.append(t)
        
    ans = n*(n-1)/2
    for z in k: ans-=(len(z)*(len(z)-1)/2)
    return int(ans)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    p = int(first_multiple_input[1])

    astronaut = []

    for _ in range(p):
        astronaut.append(list(map(int, input().rstrip().split())))

    result = journeyToMoon(n, astronaut)

    fptr.write(str(result) + '\n')

    fptr.close()