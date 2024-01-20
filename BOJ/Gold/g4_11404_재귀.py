import sys
from collections import deque

input = sys.stdin.readline



'''
n(2 ≤ n ≤ 100)개의 도시
한 도시에서 출발해서 다른 도시에 도착하는 m(1 ≤ m ≤ 100,000)개의 버스가 있다.
각 버스는 한 번 사용할 때 필요한 비용이 있다.
도시 A에서 B로 가는데 필요한 비용의 최솟값을 구하기
시작도시 a에서 도착도시 b로가는 비용 c
도시명은 1번부터 시작이지만 난 0번부터 쓸거임 
시작 도시와 도착 도시가 같은 경우는 없다
시작 도시와 도착 도시를 연결하는 노선은 하나가 아닐 수 있다.

비용은 100,000보다 작거나 같은 자연수
★한 경로가 10만인 것이니 최대값은 10만*100 일 수 있음
방향이 있는 문제임 
'''

n=int(input())
m=int(input())
MAX_COST=100_000*100

graph = [ [MAX_COST+1 for i in range(n)] for i in range(n) ]

for i in range(m):
    a,b,c=map(int,input().split())
    a-=1
    b-=1
    graph[a][b]=min(c,graph[a][b])

def update(i,j,n):
    value = graph[i][j]
    if value == MAX_COST+1:
        return
    
    for k in range(n):
        if graph[j][k]==MAX_COST+1:
            continue
        elif graph[j][k]+value < graph[i][k]:
            graph[i][k]=graph[j][k]+value
            update(i,k,n)


for i in range(n):
    for j in range(n):
        update(i,j,n)

for i in range(n):
    graph[i][i]=0

for i in range(n):
    for j in range(n):
        if graph[i][j]==MAX_COST+1:
            graph[i][j]=0
        
for i in graph:
    print(*i)

