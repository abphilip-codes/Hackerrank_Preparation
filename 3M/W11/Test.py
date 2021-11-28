# Mock Test

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'connectedCell' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#

def connectedCell(matrix, ans=0):
    k = [(z,y) for z,row in enumerate(matrix) for y,col in enumerate(row) if(col)]
    while(k):
        l,z = [k.pop()],0
        while(l):
            x,z = l.pop(),z+1
            for y in list(k):
                if(abs(x[0]-y[0])<=1 and abs(x[1]-y[1])<=1):
                    l.append(y)
                    k.remove(y)
        else: ans = max(ans,z)
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    m = int(input().strip())

    matrix = []

    for _ in range(n):
        matrix.append(list(map(int, input().rstrip().split())))

    result = connectedCell(matrix)

    fptr.write(str(result) + '\n')

    fptr.close()