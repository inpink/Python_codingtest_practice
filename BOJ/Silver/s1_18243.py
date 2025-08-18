import sys
input = sys.stdin.readline

from collections import deque

n, k = map(int, input().split())

graph = [ [] for _ in range(n)]
for i in range(k):
  a, b = map(int, input().split())
  a-=1
  b-=1
  graph[a].append(b)
  graph[b].append(a)

# print(graph)

for i in range(n):
  #bfs
  visited = [ -1 for _ in range(n)]
  visited[i] = 0
  q = deque([i])

  while True:
    if len(q) == 0:
      break
    cur = q.popleft()

    for to in graph[cur]:
      if visited[to] == -1:
        visited[to] = visited[cur] + 1
        q.append(to)

  # 확인
  for i in range(n):
    if visited[i] == -1:
      print("Big World!")
      exit(0)
    if visited[i] > 6:
      print("Big World!")
      exit(0)

print("Small World!")


'''
작은 세상 네트워크를 만족하면 "Small World!"를, 만족하지 않는다면 "Big World!"를 출력
'''