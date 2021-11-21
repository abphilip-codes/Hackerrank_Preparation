# https://www.hackerrank.com/challenges/three-month-preparation-kit-closest-numbers/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'closestNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def closestNumbers(a, y=0): 
    b = sorted([[a[z],a[z+1]] for z in range(len(a)-1)], key=lambda x:abs(x[1]-x[0]))
    while(b[y][1]-b[y][0]==b[0][1]-b[0][0]): y+=1
    return sum(b[:y], [])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(sorted(arr))

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()