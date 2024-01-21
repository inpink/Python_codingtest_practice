import sys
from collections import deque

input = sys.stdin.readline

import heapq 

'''
플로이드-워셜
'''
    
n=int(input())
graph=[]
for i in range(n):
    graph.append(list(map(int,input().split())))

#print(graph)


for k in range(n):
    for i in range(n):
        for j in range(n):
            if (graph[i][k]==1 and graph[k][j]==1):
                graph[i][j]=1


for i in graph:
    print(*i)


