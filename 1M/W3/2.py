# https://www.hackerrank.com/challenges/one-month-preparation-kit-new-year-chaos/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(q, ans=0):
    q = [z-1 for z in q]
    for z in range(len(q)-1):
        if(q[z]-z>2): return "Too chaotic"
        y=z
        while(y>=0 and q[y+1]<q[y]):
            q[y+1],q[y] = q[y],q[y+1]
            ans,y = ans+1,y-1
    return ans

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        print(minimumBribes(q))