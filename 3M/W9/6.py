# https://www.hackerrank.com/challenges/three-month-preparation-kit-two-characters/problem

#!/bin/python3

import math
import os
import random
import re
import sys
import itertools 

#
# Complete the 'alternate' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def alternate(s, ans=0):
    for z in list(map(set,itertools.combinations(set(s),2))):
        t=s
        for y in set(s)-z: t=t.replace(y,"")
        r=("".join(z))*(len(t)//2)
        if(r+r[0]==t or r==t or r==t[::-1] or r[1]+r==t): ans=max(ans,len(t))
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())

    s = input()

    result = alternate(s)

    fptr.write(str(result) + '\n')

    fptr.close()