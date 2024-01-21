import sys
input = sys.stdin.readline

v,e=map(int,input().split())
MAX_COST=10_000*400*2+1
graph=[[ MAX_COST for i in range(v)] for i in range(v)]

for i in range(e):
    a,b,c=map(int,input().split())
    a-=1
    b-=1
    graph[a][b]=c #a->b : c cost

#for i in graph:
    #print(i)


for k in range(v):
    for i in range(v):
        for j in range(v):
            if (graph[i][k]+graph[k][j]<graph[i][j]):
                graph[i][j]=graph[i][k]+graph[k][j]

#print()
#for i in graph:
    #print(i)

ansList=[]
for i in range(v):
    if graph[i][i]!=MAX_COST:
        ansList.append(graph[i][i])

if len(ansList)==0:
    print(-1)
else:
    ansList.sort()
    print(ansList[0])

'''
V개의 마을,2 ≤ V ≤ 400, 1번부터 V번까지 번호
E개의 도로, 0 ≤ E ≤ V(V-1)
일방 통행 도로(단방향)
a마을->b마을, 비용c
c는10,000 이하의 자연수
(a, b) 쌍이 같은 도로가 여러 번 주어지지 않는다.
운동 경로를 찾는 것이 불가능한 경우에는 -1을 출력

운동을 하기 위한 경로를 찾으려고 한다.  시작점으로 돌아와야 한다. =  사이클을 찾기
사이클을 이루는 도로의 길이의 합의 최솟값 출력

두 마을을 왕복하는 경우도 사이클에 포함됨에 주의

아무 사이클이나 찾으면 됨
플로이드 워셜 400**3=6400만 문제없음

400*399/2개의 조합이 나올 수 있음


플로이드워셜 python3에서 2차원 리스트에 write하는 시간때문에 시간복잡도 V**3이면 통과돼야하는데 안됨.. pypy3만 가능.. 
'''
    
