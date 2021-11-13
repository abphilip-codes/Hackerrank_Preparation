# https://www.hackerrank.com/challenges/one-month-preparation-kit-grid-challenge/problem

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
    for z in range(len(grid)):
        grid[z]=''.join(sorted(grid[z]))
    for z in range(len(grid[0])):
        for y in range(len(grid)-1):
            if grid[y][z]>grid[y+1][z]: return 'NO'
    return 'YES'

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