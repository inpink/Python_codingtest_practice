import sys
input = sys.stdin.readline


a,b = map(int,input().split())

graph=[ [0 for i in range(b+1)] for i in range(a+1)]

n=int(input())
for i in range(n):
  x,y=map(int,input().split())
  graph[x][y]=-1

for i in range(1,a+1):
  if graph[i][1]==-1:
    break
  graph[i][1]=1

for j in range(1,b+1):
  if graph[1][j]==-1:
    break
  graph[1][j]=1



# for i in graph:
#   print(i)

for i in range(2, a+1):
  for j in range(2, b+1):
    if graph[i][j]==-1: #벽이면 패스
      continue

    before1=graph[i-1][j]
    before2=graph[i][j-1]

    if before1==-1:
      before1=0
    if before2==-1:
      before2=0

    graph[i][j]=before1+before2


print(graph[a][b])