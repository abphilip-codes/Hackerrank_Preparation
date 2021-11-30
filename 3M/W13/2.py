# https://www.hackerrank.com/challenges/three-month-preparation-kit-contacts/problem

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'contacts' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts 2D_STRING_ARRAY queries as parameter.
#

def contacts(queries, ans=[]):
    c = Counter()
    for z in queries:
        if z[0]=='add':
            for y in range(1,len(z[1])+1):
                c.update([z[1][0:y]])
        else:
            ans.append(c[z[1]])
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    queries_rows = int(input().strip())

    queries = []

    for _ in range(queries_rows):
        queries.append(input().rstrip().split())

    result = contacts(queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()