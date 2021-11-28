# https://www.hackerrank.com/challenges/three-month-preparation-kit-lilys-homework/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lilysHomework' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def lilysHomework(arr, ans=[]):
    d1 = {y:z for z,y in enumerate(arr)}
    for x in [sorted(arr), sorted(arr, reverse=True)]:
        d2 = {}
        for z,y in enumerate(x):
            b = d1[y]
            while True:
                try: b = d2[b]
                except KeyError: break
            if(b!=z): d2[z]=b
        ans.append(len(d2))
    return min(ans)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = lilysHomework(arr)

    fptr.write(str(result) + '\n')

    fptr.close()