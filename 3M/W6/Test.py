# Mock Test

#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'palindromeIndex' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def palindromeIndex(s):
    for z in range(len(s)//2+1):
        if(s[z]!=s[~z]):
            if(s[z+1:len(s)-z]==s[len(s)-z-1:z:-1]): return z
            elif(s[z:len(s)-z-1]==s[z:len(s)-z-1][::-1]): return len(s)-z-1
            return -1
    return -1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

        fptr.write(str(result) + '\n')

    fptr.close()