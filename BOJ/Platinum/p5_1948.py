import sys
input=sys.stdin.readline
from collections import deque

n=int(input())
m=int(input())
times=[0]
inDegree=[0 for i in range(n+1)]
inNodes=[[] for i in range(n+1)]
canOut=[[] for i in range(n+1)]
dp=[0 for i in range(n+1)]
graph=[ [0 for i in range(n+1)] for i in range(n+1)]

for i in range(m):
    a,b,time=list(map(int,input().split()))
    canOut[a].append((b,time))
    inDegree[b]+=1
    inNodes[b].append((a,time,i)) #b에서 a까지 time초걸리고 이 간선은 i번
    graph[a][b]=max(graph[a][b],time)

#print(times, inDegree, canOut)
    
start,end=map(int,input().split())

q=deque([start])

while True:
    if len(q)==0:
        break

    thisNode=q.popleft()

    for nextNode,nextTime in canOut[thisNode]:
        inDegree[nextNode]-=1
        dp[nextNode]=max(dp[nextNode],dp[thisNode]+nextTime)
        if inDegree[nextNode]==0:
            q.append(nextNode)
            
#print(dp, dp[end])
meetTime=dp[end]

q=deque([(end,meetTime)])
running=[False for i in range(m)]
while True:
    if len(q)==0:
        break
    #print(q)
    thisNode,lastTime=q.popleft()

    for beforeNode,beforeTime,beforeLine in inNodes[thisNode]: #2->7, 6->7 가능
        if running[beforeLine] in (True,-1) :
            continue
        
        if lastTime-beforeTime==dp[beforeNode]:
            running[beforeLine]=True
            q.append((beforeNode,lastTime-beforeTime))
        else:
            running[beforeLine]=-1
#print(running)

runningCount=0
for i in running:
    if i==True:
        runningCount+=1
print(meetTime)
print(runningCount)
'''
"""선행 노드를 방문해야만 다음 노드를 방문할 수 있고"""
1->7로 도착하는 가장 늦은 시간 == 위상정렬

이어진 노드들만 탐색하기에 기본적으로 위상정렬은 bfs/dfs를 사용하는 것

DP를 씀. end에 바로 연결된 간선들만 보면 됨

'''
