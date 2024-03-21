import sys
input=sys.stdin.readline

#플로이드 워셜로 풀음

maxValue=10**9
n,m=map(int,input().split())

graph=[ [] for i in range(n+1) ]

dp=[[maxValue for i in range(n+1)] for i in range(n+1)]
dpFirstVisit=[['-' for i in range(n+1)] for i in range(n+1)]

for i in range(m):
    a,b,cost=map(int,input().split())
    graph[a].append((b,cost))
    graph[b].append((a,cost))

    dp[a][b]=min(dp[a][b],cost)
    dp[b][a]=min(dp[b][a],cost)


    dpFirstVisit[a][b]=b
    dpFirstVisit[b][a]=a

for k in range(n+1):
    for i in range(n+1):
        for j in range(n+1):
            if dp[i][k]+dp[k][j]<dp[i][j]:
                dp[i][j]=dp[i][k]+dp[k][j]
                dpFirstVisit[i][j]=dpFirstVisit[i][k]
            
for i in range(1,n+1):
    dpFirstVisit[i][i]='-'

#for i in dp:
#    print(i)
    
#for i in dpFirstVisit:
#    print(i)    

for i in range(1,n+1):
    for j in range(1,n+1):
        print(dpFirstVisit[i][j],end=' ')
    print()
