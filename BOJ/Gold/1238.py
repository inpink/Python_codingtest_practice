import sys
input = sys.stdin.readline

n, m, x  = map(int, input().split())

maxValue = 1000*100+1
graph = [ [maxValue for i in range(n+1)] for i in range(n+1) ]

for i in range(m):
  start,end,t = map(int, input().split())
  graph[start][end] = min(t,graph[start][end])

# i->j의 최단 경로는 min(현재i->j, new i->k->j)
for k in range(1,n+1):
  for i in range(1,n+1):
    if graph[i][k]==maxValue:
      continue
    for j in range(1,n+1):
      if graph[k][j]==maxValue:
        continue

      graph[i][j]= min(graph[i][j], graph[i][k]+graph[k][j])


for i in range(1,n+1):
  graph[i][i]=0

times=[]
for i in range(1,n+1):
  times.append(graph[i][x]+graph[x][i])
print(max(times))

'''

N개의 숫자로 구분된 각각의 마을에 한 명의 학생이 살고 있다.
N명의 학생이 X (1 ≤ X ≤ N)번 마을에 모여서 파티를 벌이기로 했다.
 이 마을 사이에는 총 M개의 단방향 도로들이 있고 i번째 길을 지나는데 Ti(1 ≤ Ti ≤ 100)의 시간을 소비
 걸어가서 다시 그들의 마을로 돌아와야 한다.
 이 학생들은 최단 시간에 오고 가기를 원한다.
 
 이 도로들은 단방향이기 때문에 아마 그들이 오고 가는 길이 다를지도 
출력:  N명의 학생들 중 오고 가는데 가장 많은 시간을 소비하는 학생은 누구일지 구하여라.

 N(1 ≤ N ≤ 1,000), M(1 ≤ M ≤ 10,000), 
시작점과 끝점이 같은 도로는 없으며, 시작점과 한 도시 A에서 다른 도시 B로 가는 도로의 개수는 최대 1개
모든 학생들은 집에서 X에 갈수 있고, X에서 집으로 돌아올 수 있는 데이터만 입력으로 주어진다.


'''