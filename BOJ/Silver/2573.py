import sys

input = sys.stdin.readline

from collections import deque

n, m = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(n)]
dir = [(-1, 0), (1, 0), (0, 1), (0, -1)]

# print(g)
def countSurroundZero(i, j):

  count = 0
  for moveX, moveY in dir:
    if g[i + moveX][j + moveY] == 0:
      count += 1
  return count

def copyG():
  tempG=[[0 for j in range(m)] for i in range(n)]
  for i in range(n):
    for j in range(m):
      tempG[i][j]=g[i][j]
  return tempG

def reduceG():
  tempG=copyG()
  count=0
  for i in range(1, n-1):
    for j in range(1, m-1):
      if g[i][j]==0:
        continue
      count+=1
      zero = countSurroundZero(i, j)
      tempG[i][j]=max(0, tempG[i][j]-zero)
  # print(tempG)

  return tempG,count



def isSeparate(g):

  visited=[[False for j in range(m)] for i in range(n)]

  count=0
  for startX in range(1,n-1):
    if count>=2:
      break
    for startY in range(1,m-1):
      if g[startX][startY]==0 or visited[startX][startY]:
        continue
      if count>=2:
        break

      q=deque([])
      q.append((startX,startY))
      visited[startX][startY]=True

      while True:
        if len(q)==0:
          break

        x,y=q.popleft()

        for moveX,moveY in dir:
          nextX=x+moveX
          nextY=y+moveY

          if g[nextX][nextY]==0:
            continue
          if visited[nextX][nextY]:
            continue

          visited[nextX][nextY]=True
          q.append((nextX,nextY))
      count+=1

  # print(count)
  if count>=2:
    return True
  else:
    return False

time=0
while True:
  g,iceCount=reduceG()
  if iceCount==0:
    print(0)
    exit()

  time+=1

  if isSeparate(g):
    print(time)
    exit()





