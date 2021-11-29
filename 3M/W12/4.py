# https://www.hackerrank.com/challenges/three-month-preparation-kit-beadornaments/problem

#!/bin/python3

import math
import os
import random
import re
import sys
from operator import mul
from functools import reduce

#
# Complete the 'beadOrnaments' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY b as parameter.
#

def beadOrnaments(b, M=1000000007):
    return int((reduce(mul, map(lambda z: z**(z-1),b),1)*(sum(b)**(len(b)-2)))%M)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        b_count = int(input().strip())

        b = list(map(int, input().rstrip().split()))

        result = beadOrnaments(b)

        fptr.write(str(result) + '\n')

    fptr.close()