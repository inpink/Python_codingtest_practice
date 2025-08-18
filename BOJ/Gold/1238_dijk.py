import sys
input = sys.stdin.readline

import heapq

n, m, x  = map(int, input().split())
max_value = 100*10000+1
graph = [ [] for i in range(n+1) ]
for i in range(m):
  start,end,t = map(int, input().split())
  graph[start].append((t,end))

def dijk(start):
  h = []
  heapq.heappush(h, (0, start)) #cost, node

  visited = [max_value for i in range(n+1)]
  visited[start]=0

  while True:
    if len(h)==0:
      break

    cum_cost, cur_node = heapq.heappop(h)

    for (next_cost, next_node) in graph[cur_node]:
      plus_cost = visited[cur_node]+next_cost
      if visited[next_node] > plus_cost:
        visited[next_node] = plus_cost
        heapq.heappush(h, (plus_cost, next_node))
  return visited

ans = [0 for i in range(n+1)]
for i in range(1,n+1):
  visited = dijk(i)

  if i==x:
    for j in range(1,n+1):
      ans[j]+=visited[j]
    continue

  ans[i]+=visited[x]

ans[x]=0



ans[x]=0

print(ans)
print(max(ans))