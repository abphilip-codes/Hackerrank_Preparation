# https://www.hackerrank.com/challenges/three-month-preparation-kit-merging-communities/problem

n, k = map(int, input().split())
s, ans = n*[-1], n*[1]

def get(s, z):
    while(s[z]!=-1): z = s[z]
    return z

def path(s, z, p):
    while(s[z]!=p): 
        j = s[z]
        s[z] = p 
        z = j

for _ in range(k):
    k = input().split()
    if(k[0]=='M'):
        p1 = get(s, int(k[1])-1)
        p2 = get(s, int(k[2])-1)
        if(p1!=p2):
            s[p1] = p2
            path(s, int(k[1])-1, p2)
            ans[p2] += ans[p1]
    else: print(ans[get(s, int(k[1])-1)])