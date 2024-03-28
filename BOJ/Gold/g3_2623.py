import sys
input = sys.stdin.readline
from collections import deque

n,m=map(int,input().split())

inCounts=[0 for i in range(n+1)]
outs=[[] for i in range(n+1)]

for i in range(m):
    order=list(map(int,input().split()))

    for j in range(order[0]-1):
        x,y=order[j+1],order[j+2]
        inCounts[y]+=1
        outs[x].append(y)

#print(inCounts)
#print(outs)

q=deque()
for i in range(1,n+1):
    if inCounts[i]==0:
        q.append(i)

ansList=[]
while True:
    if len(q)==0:
        break
    thisNode=q.popleft()
    ansList.append(thisNode)

    for nextNode in outs[thisNode]:
        inCounts[nextNode]-=1
        if inCounts[nextNode]==0:
            q.append(nextNode)

if len(ansList)!=n:
    print(0)
else:
    for i in ansList:
        print(i)