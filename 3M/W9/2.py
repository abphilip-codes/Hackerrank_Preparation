# https://www.hackerrank.com/challenges/three-month-preparation-kit-stockmax/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'stockmax' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY prices as parameter.
#

def stockmax(p):
    k = p[len(p)-1]
    ans = 0
    for z in range(len(p)-1,-1,-1):
        k = max(k,p[z])
        ans+=(k-p[z])
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        prices = list(map(int, input().rstrip().split()))

        result = stockmax(prices)

        fptr.write(str(result) + '\n')

    fptr.close()