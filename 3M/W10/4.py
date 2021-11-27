# https://www.hackerrank.com/challenges/three-month-preparation-kit-qheap1/problem

import heapq
h,d = [],{}

for q in range(int(input())):
    l = list(map(int,input().strip().split()))
    a,b = (l[0],l[1] if(len(l)>1) else None)

    if(a==1): heapq.heappush(h,b)
    elif(a==2): d[b]=1 if b not in d else d[b]+1
    else:
        while True:
            x = h[0]
            if x in d:
                heapq.heappop(h)
                d[x]-=1
                if(d[x]<=0): del(d[x])
            else: break
        print(x)