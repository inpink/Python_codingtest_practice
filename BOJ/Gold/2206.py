import sys
input = sys.stdin.readline

from collections import deque

n, m = map(int, input().split())
graph = []
for i in range(n):
  row = list(input().strip())
  graph.append(row)

# print(graph)

startX, startY = 0, 0
endX, endY = n-1, m-1
dir = [(-1,0), (1,0), (0,-1), (0,1)] #상 하 좌 우

#bfs
q= deque([])
q.append((startX,startY,0)) #0은 안뿌심, 1은 뿌심
visited = [[ [-1,-1] for i in range(m)] for i in range(n)] #n, m칸은 벽을 허물지 않고 최소 0회만에 올 수 있고, 벽을 허물었을 때 0번
visited[startX][startY][0] = 1

# for i in visited:
#   print(i)
# print()

while True:
  if len(q)==0:
    break

  curX,curY,isWalled = q.popleft()

  for x,y in dir:
    nextX = curX + x
    nextY = curY + y

    if nextX<0 or nextX>=n or nextY<0 or nextY>=m:
      continue

    if graph[nextX][nextY]=='0': #벽이 없으면
      if visited[nextX][nextY][isWalled]==-1 or visited[nextX][nextY][isWalled] > visited[curX][curY][isWalled] +1:
        visited[nextX][nextY][isWalled]=visited[curX][curY][isWalled]+1
        q.append((nextX, nextY, isWalled))

    elif graph[nextX][nextY]=='1': #벽이 있으면
      if isWalled==1: #이미 뿌셨으면 못함
        continue
      elif isWalled==0 and visited[nextX][nextY][isWalled]==-1 or visited[nextX][nextY][isWalled] > visited[curX][curY][isWalled] +1:
        visited[nextX][nextY][1]=visited[curX][curY][isWalled]+1
        q.append((nextX, nextY, 1))

# for i in visited:
#   print(i)


ans= max(visited[n-1][m-1])
print(ans)