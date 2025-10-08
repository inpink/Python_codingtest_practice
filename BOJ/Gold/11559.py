import sys
from copy import deepcopy

input = sys.stdin.readline

from collections import deque


graph=[list(input().strip()) for _ in range(12)]

# print(graph)

dir=[(1,0),(-1,0),(0,1),(0,-1)]

def bfs(letter, startX, startY, newGraph): #letter = 'R'
  # print(letter, startX, startY, newGraph)
  q=deque([])
  q.append([startX,startY])
  visited = [[False]*6 for _ in range(12)]
  visited[startX][startY]=True

  updatedGraph= deepcopy(newGraph)
  updatedGraph[startX][startY]='.'

  count=1
  while True:
    if len(q)==0:
      break

    x,y=q.popleft()

    if graph[x][y]!=letter:
      continue

    for i in range(4):
      dirX,dirY=dir[i]
      nextX,nextY=x+dirX,y+dirY

      if nextX<0 or nextX>=12 or nextY<0 or nextY>=6:
        continue

      if visited[nextX][nextY]:
        continue

      if graph[nextX][nextY]==letter:
        q.append((nextX, nextY))
        visited[nextX][nextY]=True
        updatedGraph[nextX][nextY]='.'
        count+=1


  if count>=4:
    return (True, updatedGraph)
  else:
    return (False, newGraph)


def down(newGraph):

  downGraph=[['.']*6 for _ in range(12)]

  for j in range(6):
    row=[]
    for i in range(12):
      if newGraph[i][j]!='.':
        row.append(newGraph[i][j])

    point=11
    while True:
      if len(row)==0:
        break

      x=row.pop()
      downGraph[point][j]=x
      point-=1

  # print(downGraph)
  return downGraph

# isEnd=False
ans=0
while True:
  # if isEnd:
  #   break
  isPoped=False
  newGraph = deepcopy(graph)

  for i in range(12):
    for j in range(6):
      if graph[i][j]=='.':
        continue

      result, newGraph = bfs(graph[i][j], i, j, newGraph)
      if result:
        isPoped=True

  if isPoped:
    ans+=1
    graph=down(newGraph)
  else:
    break

print(ans)