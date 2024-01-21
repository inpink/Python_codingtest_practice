import sys
from collections import deque
input = sys.stdin.readline

n,m=map(int,input().split())
MAX_COST=500+1 #3이상이면 됨
graph=[[ MAX_COST for i in range(n)] for i in range(n)]

for i in range(m):
    a,b=map(int,input().split())
    a-=1
    b-=1
    graph[a][b]=1 #a학생이 b학생보다 작다

#for i in graph:
    #print(i)


def bfs(init,start):
    q=deque([start])
    while True:
        if len(q)==0:
            break
        thisStart=q.pop()
        visited[thisStart]=True
        for j in range(n):
            if j==init or j==thisStart:
                continue
            if graph[thisStart][j]==1:
                graph[init][j]=1
                graph[j][init]=2
                if visited[j]==False:
                    q.append(j)
                
for i in range(n):
    visited=[False for i in range(n)]
    bfs(i,i)

#for i in graph:
    #print(i)

#정답 계산
count=0
for i in range(n):
    isPossible=True
    for j in range(n):
        if (graph[i][j]==MAX_COST and i!=j):
            isPossible=False
            break

    if isPossible:
        count+=1

print(count)

'''
어차피 주변에 하나에게만 전달하는거라면 bfs도 가능
pypy3만통과
'''
    
