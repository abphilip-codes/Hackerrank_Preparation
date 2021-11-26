# https://www.hackerrank.com/challenges/three-month-preparation-kit-waiter/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'waiter' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY number
#  2. INTEGER q
#

def waiter(number, q):
    n,y,p,ans = 2,0,[],[]
    while(y<q):
        for z in range(2,n//2+1):
            if(n%z==0): break
        else: p,y = p+[n],y+1
        n+=1
        
    for z in p:
        a,b = [],[]
        for y in number[::-1]:
            if(y%z!=0): a.append(y)
            else: b.append(y)
        ans,number = ans+b[::-1],a
    return ans+a[::-1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    number = list(map(int, input().rstrip().split()))

    result = waiter(number, q)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()