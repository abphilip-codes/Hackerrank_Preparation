# https://www.hackerrank.com/challenges/three-month-preparation-kit-jack-goes-to-rapture/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getCost' function below.
#
# The function accepts WEIGHTED_INTEGER_GRAPH g as parameter.
#

#
# For the weighted graph, <name>:
#
# 1. The number of nodes is <name>_nodes.
# 2. The number of edges is <name>_edges.
# 3. An edge exists between <name>_from[i] and <name>_to[i]. The weight of the edge is <name>_weight[i].
#
#

def getCost(n, g_from, g_to, g_weight):
    parent = [-1]*n
    def find(n):
        if parent[n]<0: return n
        p = find(parent[n])
        parent[n] = p
        return p

    edges = []
    for z in range(len(g_from)):
        a, b, c = g_from[z], g_to[z], g_weight[z]
        a,b = a-1,b-1
        edges.append((c, a, b))
    edges.sort()

    if(find(0)==find(n-1)): return 0
    else:
        for c,a,b in edges:
            a = find(a)
            b = find(b)
            if(a!=b):
                if(parent[a]==parent[b]): parent[b] -= 1
                if(parent[a]>parent[b]): parent[a] = b
                if(parent[a]<parent[b]): parent[b] = a
            if(find(0)==find(n-1)): return c
        else: return 'NO PATH EXISTS'

if __name__ == '__main__':
    g_nodes, g_edges = map(int, input().rstrip().split())

    g_from = [0] * g_edges
    g_to = [0] * g_edges
    g_weight = [0] * g_edges

    for i in range(g_edges):
        g_from[i], g_to[i], g_weight[i] = map(int, input().rstrip().split())

    print(getCost(g_nodes, g_from, g_to, g_weight))