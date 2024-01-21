import sys
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


def dfs(init,start):
    #print(smalls,visited)
    visited[start]=True
    for j in range(n):
        if start==j:
            continue
        if graph[start][j]==1:
            graph[init][j]=1 #i가 k보다 작다
            graph[j][init]=2 
            if visited[j]==False:
                dfs(init,j)


for i in range(n):
    visited=[False for i in range(n)]
    dfs(i,i)

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
dfs로도 풀 수 있네 
python으로도 통과
'''
    
