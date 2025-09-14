import sys
input = sys.stdin.readline

MAX_VALUE=10**8
n = int(input()) #4일 때
graph = []
for i in range(n):
  graph.append(list(map(int, input().split())))

# 1<<16 하면 2진수로는 10000000000000000 지만, 출력결과는 10진수인 65536임
dp=[[-1 for i in range(1<<n)] for i in range(n)] #dp[x][visited(2)]는, 현재 x에 있으며 visited를 방문했을 때의 최소 비용
def dfs(x, visited):
  # for a in dp:
  #   print(a)
  if visited == int('1'*n,2): # 1<<n -1도 됨 # 모든 도시 방문함
    if graph[x][0]!=0: #출발점으로 돌아갈 수 있다면
      return graph[x][0]
    else:
      return MAX_VALUE

  if dp[x][visited]!=-1: # 이미 최소 비용을 구했다면
    return dp[x][visited]

  for i in range(n): #x -> i  모든 도시 방문
    if graph[x][i]==0: #방문할 수 없는 도시라면 패스
      continue
    if visited & 1 << i: #방문한 도시라면 패스
      continue

    # dp 점화식, visited | (1<<i)는  새로운 도시 i를 방문했다고 표시하는 연산. |는 비트별로 OR 연산.  i=3이라면 1<<i == 1000(2), visited가 0100(2)였다면 1100이 됨
    if dp[x][visited]== -1:
      dp[x][visited] = dfs(i, visited | (1<<i)) + graph[x][i]
    else:
      dp[x][visited] = min(dp[x][visited], dfs(i, visited | (1<<i)) + graph[x][i])

  if dp[x][visited] == -1:
    return MAX_VALUE

  return dp[x][visited]

print(dfs(0, 1)) #0, 0001