# https://www.hackerrank.com/challenges/three-month-preparation-kit-gena/problem

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque

#
# Complete the 'hanoi' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY posts as parameter.
#

def hanoi(posts):
    l = len(posts)
    rangel = range(l)
    steps, state, win = 0, 0, 0
    
    def move(rod, disc):
        nonlocal state
        disc*= 2 
        state &= ~(3<<disc)
        state |= rod<<disc 
    
    def top(rod):
        st = state
        for i in rangel:
            r = 3&st  
            if(r==rod): return i
            st>>=2  
        return l  

    for z in rangel: move(posts[z]-1, z)
    if(state==win): return 0

    bfs = deque()       
    bfs.append(state) 
    depth = dict()
    depth[state] = 0 
    while True:
        cstate = state = bfs.popleft()
        steps = depth[state]           
        d = [top(r) for r in range(4)]
        for z in range(4):  
            if d[z] == l: continue
            for y in range(4): 
                if(d[y]>d[z]):
                    state = cstate 
                    move(y, d[z])
                    if (state==win): return steps + 1
                    if state not in depth:
                        depth[state] = steps + 1
                        bfs.append(state)
    return depth[0]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    loc = list(map(int, input().rstrip().split()))

    res = hanoi(loc)

    fptr.write(str(res) + '\n')

    fptr.close()