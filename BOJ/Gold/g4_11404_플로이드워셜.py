import sys
from collections import deque

input = sys.stdin.readline

import heapq 

'''
플로이드 워셜 DP (점화식)
모든 노드에서 다른 모든 노드까지의 최단 비용을 구할 때 사용
(중간에 다른 노드를 거칠 수 있음)

a->b 최단거리 = 모든 k(1~n)에 대해 min(기존a->b최단거리, a->k+ k+b)
생각해보면 당연한 알고리즘인데, DP를 이용하고, 모든 k에대해 다 검사해야 답이 나온다는 특징이 있음


★
주로
1:N은 다익스트라
N:N은 플로이드 워셜
이라고 함
둘다 최소비용 경로를 구할 때 씀
시간복잡도는 dijk가 힙을썼을 때 
https://loosie.tistory.com/146 <- 두 알고리즘 비교 잘 되어있음
'''
n=int(input())
m=int(input())
MAX_COST=100_000*100

graph = [[MAX_COST+1 for i in range(n)] for i in range(n)]
heap=[]

for i in range(m):
    a,b,c=map(int,input().split())
    a-=1
    b-=1
    graph[a][b]=min(c,graph[a][b])
    

for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j]=min(graph[i][j], graph[i][k]+graph[k][j])

for i in range(n):
    for j in range(n):
        if graph[i][j]==MAX_COST+1:
            graph[i][j]=0

    
for i in range(n):
    graph[i][i]=0


for i in graph:
    print(*i)

   
