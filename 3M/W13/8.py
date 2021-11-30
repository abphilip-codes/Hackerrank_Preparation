# https://www.hackerrank.com/challenges/three-month-preparation-kit-minimum-loss/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumLoss' function below.
#
# The function is expected to return an INTEGER.
# The function accepts LONG_INTEGER_ARRAY price as parameter.
#

def minimumLoss(p):
    k = sorted(zip(p,range(len(p))))[::-1]
    return min([k[z][0]-k[z+1][0] for z in range(len(p)-1) if(k[z][1]<k[z+1][1])])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    price = list(map(int, input().rstrip().split()))

    result = minimumLoss(price)

    fptr.write(str(result) + '\n')

    fptr.close()