# https://www.hackerrank.com/challenges/one-week-preparation-kit-balanced-brackets/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isBalanced(s):
    s=list(s)
    for z in range(1,len(s)):
        if s[z-1]=='(' and s[z]==')': s[z]=s[z-1]=0
        elif s[z-1]=='[' and s[z]==']': s[z]=s[z-1]=0
        elif s[z-1]=='{' and s[z]=='}': s[z]=s[z-1]=0
            
    if 0 not in s: return 'NO'
    s = [z for z in s if z!= 0]      
    if len(s)==0: return 'YES'
    return isBalanced(s)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()