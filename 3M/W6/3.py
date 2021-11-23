# https://www.hackerrank.com/challenges/three-month-preparation-kit-misere-nim-1/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'misereNim' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY s as parameter.
#

def misereNim(s, k=0):
    if(len(s)==sum(s) and len(s)%2==0): return "First"
    elif(len(s)==sum(s) and len(s)%2!=0): return "Second"
    else:
        for z in s: k^=z 
        if(k==0): return "Second"
        else: return "First"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        s = list(map(int, input().rstrip().split()))

        result = misereNim(s)

        fptr.write(result + '\n')

    fptr.close()