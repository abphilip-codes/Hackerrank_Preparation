# https://www.hackerrank.com/challenges/one-week-preparation-kit-grid-challenge/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#

def gridChallenge(grid):
    a = [sorted(z) for z in grid]
    b = [list(z) for z in zip(*a)]
    c = [sorted(z) for z in b]
    return 'YES' if(a==sorted(a) and b==c) else 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

        fptr.write(result + '\n')

    fptr.close()