# https://www.hackerrank.com/challenges/one-month-preparation-kit-counter-game/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'counterGame' function below.
#
# The function is expected to return a STRING.
# The function accepts LONG_INTEGER n as parameter.
#

def counterGame(n, z=1):
    while(n>1):
        z,k = z+1,0
        while(2**k<n): k+=1
        n = n//2 if(2**k==n) else n-2**(k-1)
    return "Louise" if z % 2 == 0 else "Richard" 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = counterGame(n)

        fptr.write(result + '\n')

    fptr.close()