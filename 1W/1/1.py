# https://www.hackerrank.com/challenges/one-week-preparation-kit-plus-minus/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(a):
    print(format(len([x for x in a if x > 0])/n, ".6f"))
    print(format(len([x for x in a if x < 0])/n, ".6f"))
    print(format(len([x for x in a if x == 0])/n, ".6f"))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)