# https://www.hackerrank.com/challenges/one-month-preparation-kit-queue-using-two-stacks/problem

a,b = [],[]
for _ in range(int(input())):
    z = list(map(int,input().split()))
    if(z[0]==1): b.append(z[1])
    elif(z[0]==2):
        if not a: a,b=b[::-1],[]
        a.pop()
    else: print(a[-1] if a else b[0])