import sys

input = sys.stdin.readline
from collections import deque

'''
위상정렬 + dp
'''
t = int(input())

for case in range(t):
    n, k = map(int, input().split())
    times = [0] + list(map(int, input().split()))
    ansTime = 0
    canOut = [[] for i in range(n + 1)]
    needCount = [0 for _ in range(n + 1)]
    dp = [0 for i in range(n + 1)]

    for i in range(k):
        x, y = map(int, input().split())
        canOut[x].append(y)
        needCount[y] += 1
    arrive=int(input())
    #print("times :", times)
    #print("needCount : ", needCount)
    #print("canOut",canOut)

    q=deque()
    for i in range(1,n+1):
        if needCount[i]==0:
            dp[i]=times[i]
            q.append(i)

    while True:
        if len(q)==0:
            break

        thisNode=q.popleft()

        for nextNode in canOut[thisNode]:
            needCount[nextNode]-=1
            dp[nextNode]=max(dp[nextNode],dp[thisNode]+times[nextNode])
            if needCount[nextNode]==0:
                q.append(nextNode)
    print(dp[arrive])