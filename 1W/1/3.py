# https://www.hackerrank.com/challenges/one-week-preparation-kit-time-conversion/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s): 
    if((s[-2:]=='AM' and s[:2]!='12') or (s[-2:]=='PM' and s[:2]=='12')): return s[:-2] 
    else: return str((int(s[:2])+12)%24).zfill(2)+s[2:-2]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()