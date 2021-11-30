# https://www.hackerrank.com/challenges/three-month-preparation-kit-short-palindrome/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'shortPalindrome' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def shortPalindrome(s):
    ans = mod = 10**9 + 7
    a = [0] * 26 ** 1
    b = [0] * 26 ** 2
    c = [0] * 26 ** 3
    for z in s:
        k = ord(z)-97
        x = 26*k-1
        y = k-26
        for w in range(26):
            y+=26
            x+=1
            ans+=c[y]
            c[x]+=b[x]
            b[x]+=a[w]
        a[k]+=1
    return ans%mod

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = shortPalindrome(s)

    fptr.write(str(result) + '\n')

    fptr.close()