import sys

input = sys.stdin.readline
from collections import deque

n=int(input())
times=[0]
inCount=[0 for i in range(n+1)]
outs=[[] for i in range(n+1)]
dp=[0 for i in range(n+1)]

for i in range(1,n+1):
    timeAndIns=list(map(int,input().split()))

    time=timeAndIns[0]
    times.append(time)
    for j in range(len(timeAndIns)-2):
        x=timeAndIns[j+1]
        y=i #x를 지어야만 y를 지을 수 있음
        inCount[y]+=1
        outs[x].append(y)

#print(inCount)
q=deque()
for i in range(1,n+1):
    if inCount[i]==0:
        dp[i]=times[i]
        q.append(i)

while True:
    if len(q)==0:
        break

    thisNode=q.popleft()

    for nextNode in outs[thisNode]:
        dp[nextNode]=max(dp[nextNode],dp[thisNode]+times[nextNode])
        inCount[nextNode]-=1
        if inCount[nextNode]==0:
            q.append(nextNode)

for i in range(1,n+1):
    print(dp[i])
