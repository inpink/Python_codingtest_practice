import sys
input = sys.stdin.readline

from collections import deque


n = int(input())
bridge = list(map(int, input().split()))
start, end = map(int, input().split())

start -=1
end -=1

maxAns = 10000+1

visited = [maxAns for _ in range(n)]
q = deque([(start, 0)])
visited[start] = 0

ans = maxAns

while True:
  if len(q)==0:
    break

  cur, cnt = q.popleft()

  if cur == end:
    ans = min(ans, cnt)

  for i in range(bridge[cur], n, bridge[cur]):
    nextCur = cur - i
    if nextCur >=0 and nextCur < n:
      if visited[nextCur] > cnt+1:
        visited[nextCur] = cnt+1
        q.append((nextCur, cnt+1))

    nextCur = cur + i
    if nextCur >=0 and nextCur < n:
      if visited[nextCur] > cnt+1:
        visited[nextCur] = cnt+1
        q.append((nextCur, cnt+1))

  # print(q)

if ans == 10000+1:
  print(-1)
else:
  print(ans)
