# https://www.hackerrank.com/challenges/three-month-preparation-kit-picking-numbers/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a, ans=0, b=[]):
    b.append(a[0])
    for z in range(1,len(a)):
        if(abs(b[0]-a[z])>1): b=[]
        b.append(a[z])
        ans=max(ans,len(b))
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(sorted(a))

    fptr.write(str(result) + '\n')

    fptr.close()