# https://www.hackerrank.com/challenges/three-month-preparation-kit-separate-the-numbers/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'separateNumbers' function below.
#
# The function accepts STRING s as parameter.
#

def separateNumbers(s):
    for z in range(1, len(s)//2+1):
        a,b = s[:z],int(s[:z])
        while a in s:
            a,b = a+str(b+1),b+1
            if(a==s): return 'YES '+s[:z]        
    return 'NO'

if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        print(separateNumbers(s))