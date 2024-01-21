import sys
input = sys.stdin.readline

n,m=map(int,input().split())
MAX_COST=10_000*1000+1
graph=[[ MAX_COST for i in range(n)] for i in range(n)]
for i in range(n-1):
    a,b,c=map(int,input().split())
    a-=1
    b-=1
    graph[a][b]=c
    graph[b][a]=c


for k in range(n):
    for i in range(n):
        for j in range(n):
            if (graph[i][k]+graph[k][j]<graph[i][j]): #★ 시간제한 빡빡한문제는 2차원 배열에 min()쓰면 수정하는 시간때문에 시간초과
                graph[i][j]=graph[i][k]+graph[k][j]
    
for _ in range(m):
    start,end=map(int,input().split())
    start-=1
    end-=1
    print(graph[start][end])
    
