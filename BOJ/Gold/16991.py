import sys
input = sys.stdin.readline
import math


n = int(input())

coordinates=[]
for i in range(n):
  x,y = map(int,input().split())
  coordinates.append((x,y))

# print(coordinates)

graph=[[0 for i in range(n)] for i in range(n)]

for i in range(n):
  for j in range(n):
    value = ((coordinates[i][0]-coordinates[j][0])**2 +  (coordinates[i][1]-coordinates[j][1])**2)**0.5
    graph[i][j]= math.trunc(value * 10**15) / 10**15

# print(graph)

MAX_VALUE=10**6
dp=[ [-1 for i in range(1<<n)] for i in range(n)]

# print(dp)
def dfs(x, visited):
  # for a in dp:
  #   print(a)
  # print()
  if visited== (1<<n) -1: # *** 연산자 우선순위 -가 더 높아서 1<<n -1으로 하면 1<<(n-1)으로 취급된다! 괄호로 묶기
    return graph[x][0]

  if dp[x][visited]!=-1:
    return dp[x][visited]

  for i in range(n):
    if visited & 1<<i:
      continue

    if dp[x][visited]==-1:
      dp[x][visited]=dfs(i, visited | 1<<i)+graph[x][i]
    else:
      dp[x][visited]=min(dp[x][visited], dfs(i, visited | 1<<i)+graph[x][i])

  if dp[x][visited] == -1:
    return MAX_VALUE

  return dp[x][visited]



print(dfs(0, 1))