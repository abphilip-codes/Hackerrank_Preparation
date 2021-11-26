# https://www.hackerrank.com/challenges/three-month-preparation-kit-maxsubarray/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maxSubarray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def maxSubarray(arr):
    p = max(0,arr[0])
    l = e = m = arr[0]
    for z in arr[1:]:
        e,m,l,p = max(z,e+z),max(m,max(z,e+z)),max(l,z),max(0,z)+p
    return m,l if(l<0) else p

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = maxSubarray(arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()