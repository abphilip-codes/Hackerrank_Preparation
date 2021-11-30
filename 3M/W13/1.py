# https://www.hackerrank.com/challenges/three-month-preparation-kit-find-the-running-median/problem

#!/bin/python3

import math
import os
import random
import re
import sys
import bisect

#
# Complete the 'runningMedian' function below.
#
# The function is expected to return a DOUBLE_ARRAY.
# The function accepts INTEGER_ARRAY a as parameter.
#

def runningMedian(a):
    b,c,l = [],[],0
    for z in range(len(a)):
        l+=1
        bisect.insort(b,a[z])
        if(l%2==1): c.append(b[l//2])
        else: c.append((b[l//2]+b[l//2-1])/2)
    return c

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a_count = int(input().strip())

    a = []

    for _ in range(a_count):
        a_item = int(input().strip())
        a.append(a_item)

    result = runningMedian(a)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()