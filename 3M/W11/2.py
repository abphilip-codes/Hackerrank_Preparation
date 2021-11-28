# https://www.hackerrank.com/challenges/three-month-preparation-kit-common-child/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'commonChild' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#

def commonChild(s1, s2):
    a, b = len(s1), len(s2)
    p, c = [0]*(b+1), [0]*(b+1)
    for z in range(1, a+1):
        for y in range(1, b+1):
            if(s1[z-1]==s2[y-1]): c[y] = 1+p[y-1]
            else:
                if(c[y-1]>p[y]): c[y] = c[y-1]
                else: c[y] = p[y]
        c, p = p, c
    return p[b]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = commonChild(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()