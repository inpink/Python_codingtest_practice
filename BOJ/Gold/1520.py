import sys
input = sys.stdin.readline
import heapq

n, m = map(int, input().split())
graph= [ ]
for i in range(n):
  row=list(map(int,input().split()))
  graph.append(row)


startX,startY=0,0
endX,endY=n-1, m-1
dir = [(-1,0), (1,0), (0,-1), (0,1)] #상 하 좌 우
visited = [[0 for i in range(m)] for i in range(n)]
visited[startX][startY]=1

# bfs
h= []
heapq.heappush(h,(-1,startX,startY))

while True:
  if len(h)==0:
    ans=0
    break

  minusWay,curX,curY = heapq.heappop(h)

  if curX==n-1 and curY==m-1: #(x, y)까지 올 수 있는 모든 경로는 이미 다 탐지되었다. "내리막길만 가고(=⭐큰숫자부터 탐색함⭐)"
    ans=visited[curX][curY]
    break

  for x,y in dir:
    nextX = curX+x
    nextY = curY+y

    if nextX<0 or nextX>=n or nextY<0 or nextY>=m:
      continue

    if graph[nextX][nextY]>=graph[curX][curY]:
      continue

    if visited[nextX][nextY]!=0:
      visited[nextX][nextY]+=visited[curX][curY]
    else:
      visited[nextX][nextY] = visited[curX][curY]
      heapq.heappush(h,(-1*graph[nextX][nextY],nextX,nextY))

print(ans)


'''
H는 10억 이하의 음이 아닌 정수이다. => 그냥 bfs하면 시간초과

'''