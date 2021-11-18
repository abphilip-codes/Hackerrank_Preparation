# https://www.hackerrank.com/challenges/three-month-preparation-kit-camel-case/problem

import sys
import re
for s in sys.stdin.read().splitlines():
    op, ty, name = s.split(';')
    if(op=='C'):
        if(ty=='C'): print(''.join([z.capitalize() for z in name.split()]))
        else:
            t = name.split()
            c = [z.capitalize() for z in t[1:]]
            c.insert(0,t[0])
            print(''.join(c) + ('()' if(ty=='M') else ''))
    if(op=='S'):
        if(ty=='C'): print(' '.join([z.lower() for z in re.findall('[A-Z][^A-Z]*', name)]))
        else: print(' '.join([z.lower() for z in re.findall('[a-zA-Z][^A-Z]*', name.split('()')[0])]))