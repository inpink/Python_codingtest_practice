import sys
input=sys.stdin.readline

def dfs(curX,curY):
    if curX==n-1 and curY==m-1:
        return 1
    
    if dp[curX][curY]!=-1:
        return dp[curX][curY]
    
    curScore=graph[curX][curY]
    ways=0
    for dirX,dirY in direction:
        nextX=dirX+curX
        nextY=dirY+curY

        if nextX<0 or nextX>=n or nextY<0 or nextY>=m:
            continue

        nextScore=graph[nextX][nextY]
        if nextScore < curScore:
            ways+=dfs(nextX,nextY)

    #print(curX,curY)       
    dp[curX][curY]=ways
    return ways
    
n,m=map(int,input().split())

graph=[]
direction=[(-1,0),(1,0),(0,-1),(0,1)] #상하좌우
dp=[[-1 for i in range(m)] for i in range(n)] #start지점에서 x,y까지 올 수 있는 경우의 수 / nextX,nextY

for i in range(n):
    row=list(map(int,input().split()))
    graph.append(row)

#print(graph)


print(dfs(0,0))
