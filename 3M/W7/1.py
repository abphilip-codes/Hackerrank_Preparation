# https://www.hackerrank.com/challenges/three-month-preparation-kit-bomber-man/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bomberMan' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING_ARRAY grid
#

def bomberMan(n, grid):
    if(n<2): return grid 
    if(n%2==0): return ['O'*len(grid[0]) for _ in range(len(grid))] 

    for _ in range(2):
        g = [list(z) for z in grid]
        for z in range(len(grid)):
            for y in range(len(grid[0])):
                if(g[z][y]=='O'):
                    for a,b in (z,y+1),(z,y-1),(z+1,y),(z-1,y):
                        if(0<=a<len(grid) and 0<=b<len(grid[0]) and g[a][b]=='.'): g[a][b] = 'X' 
                    g[z][y] = 'X'
        grid = [''.join('.' if(y=='X') else 'O' for y in z) for z in g]
        if(n%4==3): return grid
    return grid

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    r = int(first_multiple_input[0])

    c = int(first_multiple_input[1])

    n = int(first_multiple_input[2])

    grid = []

    for _ in range(r):
        grid_item = input()
        grid.append(grid_item)

    result = bomberMan(n, grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()