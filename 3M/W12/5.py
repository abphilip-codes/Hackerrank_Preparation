# https://www.hackerrank.com/challenges/three-month-preparation-kit-floyd-city-of-blinding-lights/problem

#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    road_nodes, road_edges = map(int, input().rstrip().split())
    ans=[[math.inf]*(road_nodes+1) for _ in range(road_nodes+1)]

    road_from = [0] * road_edges
    road_to = [0] * road_edges
    road_weight = [0] * road_edges

    for z in range(road_edges):
        road_from[z], road_to[z], road_weight[z] = map(int, input().rstrip().split())
        ans[road_from[z]][road_to[z]] = road_weight[z]
    
    for z in range(1,road_nodes+1): ans[z][z]=0
    
    for x in range(1,road_nodes+1):
        for y in range(1,road_nodes+1):
            for z in range(1,road_nodes+1):
                ans[y][z]=min(ans[y][z],ans[y][x]+ans[x][z])

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        x = int(first_multiple_input[0])

        y = int(first_multiple_input[1])
        
        print(ans[x][y] if ans[x][y]!=math.inf else -1)