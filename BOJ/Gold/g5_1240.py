import sys
input = sys.stdin.readline

'''
dfs(pypy만 통과)
visited 2차원으로 두면 메모리초과/시간초과
'''

n,m=map(int,input().split())
graph=[[ 0 for i in range(n)] for i in range(n)]
for i in range(n-1):
    a,b,c=map(int,input().split())
    a-=1
    b-=1
    graph[a][b]=c
    graph[b][a]=c

#for i in graph:
    #print(i)
def findEnd(start,end,ans):
    visited[start]=True
    #print(start,end,ans)
    if graph[start][end]==0: #답이 없으면 답을 찾아와야함
        for i in range(n):
            if i==start:
                continue
            if graph[start][i]!=0 and visited[i]==False: 
                find=findEnd(i,end,ans+graph[start][i])
                if find!=0:
                    return find
        return 0     
                    
    else: #답이 나오는 유일한 경우
        return ans+graph[start][end]
    
for _ in range(m):
    start,end=map(int,input().split())
    start-=1
    end-=1
    visited=[ False for i in range(n)]  #★ visited가 2차원일 필요 없다! 각상황에서 end는 동일하고 검사할 start만 달라지기 때문
    print(findEnd(start,end,0)) #어차피 반드시 0임



