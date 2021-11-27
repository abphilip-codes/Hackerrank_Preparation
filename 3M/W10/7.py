# https://www.hackerrank.com/challenges/three-month-preparation-kit-hackerland-radio-transmitters/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hackerlandRadioTransmitters' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY x
#  2. INTEGER k
#

def hackerlandRadioTransmitters(x, k):
    l,ans,m = x[0],1,0   
    for z in range(1,len(x)):
        if(x[z]-l<=k): m = x[z]
        if(x[z]-m>k): ans,l = ans+1,x[z]
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    x = list(map(int, input().rstrip().split()))

    result = hackerlandRadioTransmitters(sorted(x), k)

    fptr.write(str(result) + '\n')

    fptr.close()