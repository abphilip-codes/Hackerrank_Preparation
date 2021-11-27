# https://www.hackerrank.com/challenges/three-month-preparation-kit-largest-rectangle/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'largestRectangle' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY h as parameter.
#

def largestRectangle(h,ans=0,z=0):
    stack=[]
    while(z<len(h)):
        if not stack or h[stack[-1]]<=h[z]:
            stack.append(z)
            z+=1
        else:
            top=stack.pop()
            ans=max(ans,h[top]*(z-stack[-1]-1 if(stack) else z))
    while(stack):
        top=stack.pop()
        ans=max(ans,h[top]*(z-stack[-1]-1 if(stack) else z))
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    h = list(map(int, input().rstrip().split()))

    result = largestRectangle(h)

    fptr.write(str(result) + '\n')

    fptr.close()