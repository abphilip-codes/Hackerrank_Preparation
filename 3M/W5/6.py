# https://www.hackerrank.com/challenges/three-month-preparation-kit-countingsort4/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSort' function below.
#
# The function accepts 2D_STRING_ARRAY arr as parameter.
#

def countSort(arr, a=[[] for z in range(100)]):
    for z in range(len(arr)):
        a[int(arr[z][0])].append(arr[z][1] if(z>=len(arr)//2) else '-')
    print(*[y for z in a for y in z if z])

if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)