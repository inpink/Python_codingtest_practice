import sys
input = sys.stdin.readline

n,m,r=map(int,input().split())
MAX_COST=100*15+1
graph=[[ MAX_COST for i in range(n)] for i in range(n)]

items = list(map(int,input().split()))

for i in range(r):
    a,b,l=map(int,input().split())
    a-=1
    b-=1
    if l<=m:
        graph[a][b]=min(graph[a][b],l) #a<->b : l cost
        graph[b][a]=min(graph[b][a],l)
    
#for i in graph:
#    print(i)

for k in range(n):
    for i in range(n):
        for j in range(n):
            candidate = graph[i][k]+graph[k][j]
            if candidate<graph[i][j] and candidate<=m:
                graph[i][j]=candidate


#print()
#for i in graph:
#    print(i)

ansList = []
for i in range(n):
    count=0
    for j in range(n):
        if i==j:
            count+=items[j]

        elif graph[i][j]!=MAX_COST:
            count+=items[j]

    ansList.append(count)

#print(ansList)
ansList.sort()
print(ansList[-1])

'''
지역 개수 n(1 ≤ n ≤ 100), 수색범위 m (1 ≤ m ≤ 15),길의 개수 r (1 ≤ r ≤ 100)
둘째 줄에는 n개숫자있음. 각 구역에 있는 아이템의 수 t (1 ≤ t ≤ 30)
세 번째 줄부터 r+2번째 줄 까지 a<->b,  l(1 ≤ l ≤ 15)
지역의 번호는 1이상 n이하의 정수
두 지역의 번호가 같은 경우는 없다

양방향 통행이 가능
낙하한 지역을 중심으로
거리가 수색 범위 m (1 ≤ m ≤ 15) 이내의 모든 지역의 아이템을 습득 가능하다

예은이가 얻을 수 있는 아이템의 최대 개수 구하기

=> 모든 정점에서 비용을 구해야하므로 플로이드 워셜

'''
    
