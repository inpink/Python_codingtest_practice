import sys
input = sys.stdin.readline
from collections import deque

n=int(input())
lands=[]
graph=[]
distributed_graph=[ [0 for i in range(n)] for i in range(n)]
for i in range(n):
  row= list(map(int, input().split()))
  graph.append(row)
  # distributed_graph.append(row)
  for j in range(n):
    if row[j]==1:
      lands.append((i,j))

for i in graph:
  print(i)
print(lands)


land_count=0
for x,y in lands:
  if distributed_graph[x][y]==0:
    #bfs
    land_count+=1
    land_q=deque([])
    land_q.append((x, y, land_count))
    while True:
      if len(land_q)==0:
        break

      this_x,this_y,this_land_count=land_q.popleft()


  else: #이미 땅 체크된 곳이면 패스
    continue
