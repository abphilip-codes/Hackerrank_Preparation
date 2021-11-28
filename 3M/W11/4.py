# https://www.hackerrank.com/challenges/three-month-preparation-kit-richie-rich/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'highestValuePalindrome' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER n
#  3. INTEGER k
#

def highestValuePalindrome(s, n, k):
    if (n==1): return '9' if (k==1) else '-1'
    a = [0 for z in range(n)]
    for z in range(n//2+(n&1)):
        if(s[z] != s[n-1-z]):
            s[z] = s[n-1-z] = max(s[z], s[n-1-z])
            a[z],k = a[z]+1,k-1
        if(k < 0): return '-1'
    for z in range(n//2+(n&1)):
        if(s[z] != '9'):
            c = 1 if (a[z]==1 or z==(n-1-z)) else 2
            if(k>=c):
                s[z] = s[n-1-z] = '9'
                k-=c
            if(k<=0): break
    return ''.join(s)   

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(input())

    result = highestValuePalindrome(s, n, k)

    fptr.write(result + '\n')

    fptr.close()