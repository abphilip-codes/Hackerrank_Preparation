# https://www.hackerrank.com/challenges/one-month-preparation-kit-caesar-cipher-1/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k, ans=''):
    for w in s:
        if w.isalpha() and w.isupper(): ans+=chr((ord(w)+k-65)%26+65)
        elif w.isalpha() and w.islower(): ans+=chr((ord(w)+k-97)%26+97)
        else: ans+=w
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()