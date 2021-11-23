# https://www.hackerrank.com/challenges/three-month-preparation-kit-magic-square-forming/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'formingMagicSquare' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY s as parameter.
#

def formingMagicSquare(s):
    k = [[a, 15-a-b, b, 5+b-a, 5, 5+a-b, 10-b, a+b-5, 10-a] for b in range(1,10) for a in range(1,10) 
          if set([a, 15-a-b, b, 5+b-a, 5, 5+a-b, 10-b, a+b-5, 10-a])==set(range(1,10))]
    return min([min(100,sum([abs([x for z in range(3) for x in s[z]][z]-p[z]) for z in range(9)])) for p in k])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()