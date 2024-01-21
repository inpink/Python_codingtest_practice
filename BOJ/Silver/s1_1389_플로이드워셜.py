import sys
input = sys.stdin.readline

n,m=map(int,input().split())
MAX_COST=100+1
graph=[[MAX_COST for i in range(n)] for i in range(n)]

for i in range(m):
    a,b=map(int,input().split())
    a-=1
    b-=1
    graph[a][b]=1
    graph[b][a]=1

#for i in graph:
    #print(i)
    
for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][k]+graph[k][j]<graph[i][j]:
                graph[i][j]=graph[i][k]+graph[k][j]

minAns=[]
for i in range(n):
    minAns.append((sum(graph[i])-graph[i][i],i+1))
        

minAns.sort()
print(minAns[0][1])

'''
유저 n명, 관계 m개
A와 B가 친구이면 B와 A도 친구(양방향)
A와 B가 같은 경우는 없다
친구 관계는 중복되어 들어올 수도 있으며,
친구가 한 명도 없는 사람은 없다.
모든 사람은 친구 관계로 연결되어져 있다
사람의 번호는 1부터 N까지이며, 두 사람이 같은 번호를 갖는 경우는 없다.

케빈 베이컨의 수가 가장 작은 사람 번호를 출력
그런 사람이 여러 명일 경우에는 번호가 가장 작은 사람을 출력

cost가 1인 간선이 m개 들어오는 것과 같음

n**3으로 시간 내 통과
'''
    
