# https://www.hackerrank.com/challenges/three-month-preparation-kit-maximum-perimeter-triangle/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maximumPerimeterTriangle' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY sticks as parameter.
#

def maximumPerimeterTriangle(s):
    for z in range(0,len(s)-2):
        if(s[z]<s[z+1]+s[z+2]) : return [s[z+2], s[z+1], s[z]] 
    return [-1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    sticks = list(map(int, input().rstrip().split()))

    result = maximumPerimeterTriangle(sorted(sticks, reverse=True))

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()