# https://www.hackerrank.com/challenges/three-month-preparation-kit-strong-password/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumNumber' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING password
#

def minimumNumber(n, password, k = r'(\d){1,}|([a-z]){1,}|([A-Z]){1,}|(\W){1,}'):
    return max(6-n, 4-len([1 for z in zip(*re.findall(k, password)) if("".join(z))]))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()