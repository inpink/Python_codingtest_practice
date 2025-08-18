import sys

input = sys.stdin.readline

from collections import deque

n = int(input())
bridge = list(map(int, input().split()))
start = int(input())

start -= 1

visited = [False for _ in range(n)]
q = deque([(start)])
visited[start] = True

while True:
  if len(q) == 0:
    break

  cur = q.popleft()

  nextCur = cur - bridge[cur]
  if nextCur >= 0 and nextCur < n:
    if visited[nextCur] == False:
      visited[nextCur] = True
      q.append((nextCur))

  nextCur = cur + bridge[cur]
  if nextCur >= 0 and nextCur < n:
    if visited[nextCur] == False:
      visited[nextCur] = True
      q.append((nextCur))

# print(q)
print(visited)

ans = 0
for i in range(n):
  if visited[i] == True:
    ans += 1

print(ans)
