# https://www.hackerrank.com/challenges/one-month-preparation-kit-plus-minus/problem

#!/bin/python3

import math
import os
import random
import re
import sys

def plusMinus(a):
    print(format(len([x for x in a if x > 0])/n, ".6f"))
    print(format(len([x for x in a if x < 0])/n, ".6f"))
    print(format(len([x for x in a if x == 0])/n, ".6f"))

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    plusMinus(arr)