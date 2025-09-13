import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph=[]
for i in range(n):
  row=list(map(str, input().rstrip()))
  graph.append(row)

# print(graph)

dir = [(-1, 1), (0,1), (1,1)] #대각상, 바로옆, 대각아래

# visited=[[False for _ in range(m)] for i in range(n)]


def dfs(x,y):
  if y==m-1:
    return 1

  for dirX, dirY in dir:
    nextX=dirX+x
    nextY=dirY+y

    if nextX<0 or nextX>=n or nextY<0 or nextY>=m:
      continue
    if graph[nextX][nextY]!='x':
      graph[nextX][nextY]='x'
      ex = dfs(nextX, nextY)
      if ex==1:
        return 1

  return 0

count=0
for i in range(n):
  startX=i
  startY=0

  graph[startX][startY]='x'
  count+= dfs(startX, startY)
  # for a in graph:
  #   print(a)
  # print(i, count)
  # print()
print(count)


