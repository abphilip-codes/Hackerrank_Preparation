# https://www.hackerrank.com/challenges/one-month-preparation-kit-mini-max-sum/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr): 
    print((sum(arr)-(max(arr))),(sum(arr)-(min(arr))))

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)