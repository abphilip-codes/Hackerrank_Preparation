# https://www.hackerrank.com/challenges/three-month-preparation-kit-simple-text-editor/problem

s,a = '',[]
for _ in range(int(input())):
    z = input().split()
    if z[0]=='1':
        a.append(s)
        s = s+z[1]
    elif z[0]=='2':
        a.append(s)
        s = s[0:int(z[1])*-1]
    elif z[0]=='3': print(s[int(z[1])-1])
    else: s = a.pop()