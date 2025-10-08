import sys
input = sys.stdin.readline
sys.setrecursionlimit(1_500_000)

n = int(input())
edges = [tuple(map(int, input().split())) for _ in range(n - 1)]

# 인접 리스트 초기화
arr = [[] for _ in range(n + 1)]
for u, v in edges:
  arr[u].append(v)
  arr[v].append(u)

# DP 테이블 초기화
dp = [[0, 0] for _ in range(n + 1)]

# 방문 배열
visited = [False] * (n + 1)

# DFS 함수 정의
def dfs(node):
  visited[node] = True
  dp[node][1] = 1  # 현재 노드를 얼리 어답터로 선택한 경우

  for neighbor in arr[node]:
    if not visited[neighbor]:
      dfs(neighbor)
      dp[node][0] += dp[neighbor][1]  # 현재 노드를 얼리 어답터가 아닐 때
      dp[node][1] += min(dp[neighbor][0], dp[neighbor][1])  # 현재 노드를 얼리 어답터일 때

# DFS 호출 (트리의 루트는 1번 노드라고 가정)
dfs(1)

# 최종 답은 루트 노드가 얼리 어답터가 아닌 경우와 얼리 어답터인 경우 중 최소값
print(min(dp[1][0], dp[1][1]))

#출처: https://developer-traxer.tistory.com/31 [Developer-TraXer:티스토리]
#트리DP, 처음 풀어봐서 아직 아리까리함