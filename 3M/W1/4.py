# https://www.hackerrank.com/challenges/three-month-preparation-kit-breaking-best-and-worst-records/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(s): 
    return [sum([1 for z in range(1,len(s)) if(s[z]>max(s[0:z]))]),
            sum([1 for z in range(1,len(s)) if(s[z]<min(s[0:z]))])]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()