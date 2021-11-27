# https://www.hackerrank.com/challenges/three-month-preparation-kit-weighted-uniform-string/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'weightedUniformStrings' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER_ARRAY queries
#

def weightedUniformStrings(s, queries, ans=set()):
    for z in range(len(s)):
        if(z==0 or s[z]!=s[z-1]): a=(ord(s[z])-96)           
        else: a+=(ord(s[z])-96)            
        ans.add(a)
    return ["Yes" if(z in ans) else "No" for z in queries]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()