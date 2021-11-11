# https://www.hackerrank.com/challenges/one-week-preparation-kit-no-prefix-set/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'noPrefix' function below.
#
# The function accepts STRING_ARRAY words as parameter.
#

def noPrefix(words):
    p = {}
    h = {}
    for z in words:
        c = ''
        if z in p: return f'BAD SET\n{z}'
        for l in z:
            c+=l
            p[c] = 1
            if c in h: return f'BAD SET\n{z}'
        h[z] = 1
    return f'GOOD SET'

if __name__ == '__main__':
    n = int(input().strip())

    words = []

    for _ in range(n):
        words_item = input()
        words.append(words_item)

    print(noPrefix(words))