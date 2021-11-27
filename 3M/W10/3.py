# https://www.hackerrank.com/challenges/three-month-preparation-kit-permutation-game/problem

#!/bin/python3

import math
import os
import random
import re
import sys
from copy import copy
from collections import defaultdict

#
# Complete the 'permutationGame' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def permutationGame(arr):
    if(tuple(arr) in d): return d[tuple(arr)]
    elif(arr==sorted(arr)):
        d[tuple(arr)]=0
        return d[tuple(arr)]
    else:
        ans=set()
        for z in arr:
            t=copy(arr)
            t.remove(z)
            t=[sorted(t).index(z)+1 for z in t]
            ans.add(permutationGame(t))
        r=0
        while r in ans: r+=1
        d[tuple(arr)]=r   
        return d[tuple(arr)]

if __name__ == '__main__':
    d=defaultdict(int)
    
    d[tuple([1])]=0
        
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        arr_count = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = 'Alice' if permutationGame(arr) else 'Bob'

        fptr.write(result + '\n')

    fptr.close()