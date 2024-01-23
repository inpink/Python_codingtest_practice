import sys
input = sys.stdin.readline

n=int(input())
MAX_COST=100*15+1
graph=[[ MAX_COST for i in range(n)] for i in range(n)]

while True:
    a,b=map(int,input().split())
    if a==-1 and b==-1:
        break
    
    a-=1
    b-=1
    graph[a][b]=1 #a<->b : l cost
    graph[b][a]=1
    
#for i in graph:
#    print(i)

for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][k]+graph[k][j] < graph[i][j]:
                graph[i][j]=graph[i][k]+graph[k][j]

for i in range(n):
    graph[i][i]=0

#print()
#for i in graph:
#    print(i)

ansList=[]
for i in range(n):
    ansList.append(max(graph[i]))

minValue = min(ansList)
candidates=[]
for i in range(n):
    if ansList[i]==minValue:
        candidates.append(i+1)

print(minValue, len(candidates))
for i in candidates:
    print(i,end=' ')

'''
회원의 수는 2~50명
한 줄에 두 개의 회원번호가 있는데, 이것은 두 회원이 서로 친구임을 나타낸다.
회원번호는 1부터 회원의 수만큼 붙어 있다. 마지막 줄에는 -1이 두 개 들어있다.

회장은 회원들 중에서 점수가 가장 작은 사람이 된다.
회장의 점수와 회장이 될 수 있는 모든 사람을 찾는 프로그램을 작성
 
'''
    
