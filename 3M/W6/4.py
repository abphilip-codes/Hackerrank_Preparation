# https://www.hackerrank.com/challenges/three-month-preparation-kit-an-interesting-game-1/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gamingArray' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def gamingArray(arr, c=0, m=0):
    for z in arr:
        if(z>c): c,m=z,m+1
    return "ANDY" if(m%2==0) else "BOB"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input().strip())

    for g_itr in range(g):
        arr_count = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = gamingArray(arr)

        fptr.write(result + '\n')

    fptr.close()