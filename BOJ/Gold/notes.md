G3, https://www.acmicpc.net/problem/2206, 3차원 bfs
벽 하나 허무는 bfs 문제

visited = [[ ⭐[-1,-1]⭐ for i in range(m)] for i in range(n)] #n, m칸은 벽을 허물지 않고 최소 0회만에 올 수 있고, 벽을 허물었을 때 0번
visited[startX][startY][0] = 1
q.append((startX,startY,0)) #0은 안뿌심, 1은 뿌심
if visited[nextX][nextY][isWalled]==-1 or visited[nextX][nextY][isWalled] > visited[curX][curY][isWalled] +1:


- 불가능할 때는 -1을 출력할 거라 -1을 둔거임
- bfs 초기값 꼭 지정해주기
- if elif돼야할걸 if if 연달아 쓰지 않도록 주의

***

G3, https://www.acmicpc.net/problem/2252, 위상정렬
위상 정렬 · 사이클이 없는 방향 그래프의 모든 노드를 방향성에 거스르지 않도록 순서대로 나열하는 것

inDegree = [0 for i in range(n+1)]
graph[a].append(b) #1. a->b
inDegree[b]+=1 #2. b는 이 개수만큼 상위에 있다
if inDegree[i]==0: q.append(i) # 3.root 후보를 고른다
cur = q.popleft(),  ans.append(cur),     #4. root끼리는 순서가 상관없다. 현재 root인 것들을 상단에 담아준다.
for i in graph[cur]: inDegree[i]-=1  if inDegree[i]==0:    q.append(i)   #5. 상단에 담겼기 때문에 상위 의존성 하나 제거한다. 이 친구도 이로 인해 root가 된다면 다음 반복에서 ans 리스트에 담아준다.

- 위상 정렬 구현 방법을 외워야 함 

***

G3, https://www.acmicpc.net/problem/1238, 다익스트라 or 플로이드 워셜

플로이드 워셜
```
n, m, x  = map(int, input().split())
maxValue = 1000*100+1
graph = [ [maxValue for i in range(n+1)] for i in range(n+1) ]

for i in range(m):
  start,end,t = map(int, input().split())
  graph[start][end] = min(t,graph[start][end]) ⭐

# i->j의 최단 경로는 min(현재i->j, new i->k->j) ⭐
for k in range(1,n+1): ⭐
  for i in range(1,n+1): ⭐
    if graph[i][k]==maxValue: ⭐이거 체크 안하면 시간 초과. m=1만이고, n=1천임.(1000^3 X)
      continue
    for j in range(1,n+1): ⭐
      if graph[k][j]==maxValue:
        continue
      graph[i][j]= min(graph[i][j], graph[i][k]+graph[k][j]) ⭐

for i in range(1,n+1):
  graph[i][i]=0 ⭐

times=[]
for i in range(1,n+1):
  times.append(graph[i][x]+graph[x][i])
print(max(times))
```
- 플로이드 워셜 코드 외우기
- 플로이드 워셜 i,j,k 순서 제발 틀리지 말고 체크하기


다익스트라 
```
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
```
- 다익스트라 코드 외우기
- 다익스트라 한 번 돌리면 a에서 모든 노드까지의 최단 거리 구해짐
- 힙 이용 없이 구현하면, 매번 최단 거리가 가장 짧은 노드를 순차 탐색해야 하고, 현재 노드와 연결된 노드를 매번 확인해야 한다. -> 시간 초과 발생. 힙을 이용하게 되면, 최단 거리 정보를 힙에 담아 처리하므로 출발 노드부터 가장 거리가 짧은 노드를 빠르게 찾을 수 있다
- heap 이용했을 때 시간복잡도 = (간선)log(간선).  heap에서 간선개수만큼 빼내므로(힙에서 빼낼 때 정렬이 logE이다)

***

G3, https://www.acmicpc.net/problem/1520,  BFS + DP

minusWay,curX,curY = heapq.heappop(h)

if curX==n-1 and curY==m-1: #(x, y)까지 올 수 있는 모든 경로는 이미 다 탐지되었다. "내리막길만 가고(=⭐큰숫자부터 탐색함⭐)"
ans=visited[curX][curY]
break

if visited[nextX][nextY]!=0:
    visited[nextX][nextY]+=visited[curX][curY]
else:
    visited[nextX][nextY] = visited[curX][curY]
    heapq.heappush(h,(-1*graph[nextX][nextY],nextX,nextY))

- python heap은 기본 min heap이다 
- visited = [[0 for i in range(m)] for i in range(n)]    n가로, m세로 헷갈리지 말기!
- H는 10억 이하의 음이 아닌 정수이다. => 그냥 bfs하면 시간초과
- bfs하되, heap을 이용해 ⭐필드의 큰 숫자부터⭐뽑는다.  
- 겹치는 길이 있으면 더해주기만 해서 추후에 흘러간 물이 더 bfs하도록 한다. 없으면 힙에 넣어주기


***

G3, https://www.acmicpc.net/problem/15683, 구현 시뮬레이션

1. graph for for문 돌며 찾는다 | oneCCTV=[]twoCCTV=[]threeCCTV=[]fourCCTV=[]fiveCCTV=[]
2. cctv 방향 경우를 하드코딩해준다 | one=["u","d","l","r"] #상,하,좌,우 two=["ud","lr","ud","lr"] #상하, 좌우 (편의상 4개로 맞춰줌) three=["ur","rd","dl","lu"] four=["lur","urd","ldr","dlu"] five=["udlr","udlr","udlr","udlr"] direction={"u":(-1,0),"d":(1,0),"l":(0,-1),"r":(0,1)} totalDirection={1:one,2:two,3:three,4:four,5:five}
3. cctv가 7개면 0000부터 7777까지 모든 경우의 수 (7^4) | from itertools import product    products=list(product(range(4),repeat=cctv개수))
4. 가려지는 벽 개수 세기 | for pro in products:


- 순열, 조합 라이브러리 사용 방법 정리하기


***

G3, https://www.acmicpc.net/problem/1005, DFS/BFS + DP

- DFS는 가치지기가 중요하다! 여기서   if dp[thisNode]!=-1: return dp[thisNode] 안했으면 시간초과 떴음
- 여기서 DP 초기값은, time이 될 수 없는 값으로 해야 가지치기가 가능했음. time은 0~였음. 범위 잘보자!
- 위상정렬?이라는 문제지만 나는 그냥 DFS로 풀음. 어렵게 생각할거 없다. 논리가 맞으면 된다.


***

union fine https://study-yoon.tistory.com/241
