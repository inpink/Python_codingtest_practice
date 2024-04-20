import sys
input=sys.stdin.readline
from collections import deque

n=int(input())

times=[0]
inDegree=[0]
canOut=[[] for i in range(n+1)]
dp=[0 for i in range(n+1)]

for thisNode in range(1,n+1):
    timeAndIns=list(map(int,input().split()))

    time=timeAndIns[0]
    times.append(time)

    insCount=timeAndIns[1]
    thisIns=timeAndIns[2:]
    inDegree.append(len(thisIns))
    
    for beforeNode in thisIns:
        canOut[beforeNode].append(thisNode)

#print(times, inDegree, canOut)
    

q=deque()

for thisNode in range(1,n+1):
    if inDegree[thisNode]==0:
        q.append(thisNode)
        dp[thisNode]=times[thisNode]

while True:
    if len(q)==0:
        break

    thisNode=q.popleft()

    for nextNode in canOut[thisNode]:
        inDegree[nextNode]-=1
        dp[nextNode]=max(dp[nextNode],dp[thisNode]+times[nextNode])
        if inDegree[nextNode]==0:
            q.append(nextNode)
print(max(dp))
        
#위상정렬
