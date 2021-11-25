# https://www.hackerrank.com/challenges/three-month-preparation-kit-reduced-string/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superReducedString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def superReducedString(s,z=0):
    while(z<len(s)-1):
        if(s[z]==s[z+1]): s,z = s[:z]+s[z+2:],0
        else: z+=1
    return s if s else 'Empty String'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()