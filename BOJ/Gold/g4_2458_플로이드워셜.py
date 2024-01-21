import sys
input = sys.stdin.readline

n,m=map(int,input().split())
MAX_COST=500+1 #3이상이면 됨
graph=[[ MAX_COST for i in range(n)] for i in range(n)]

for i in range(m):
    a,b=map(int,input().split())
    a-=1
    b-=1
    graph[a][b]=1 #a학생이 b학생보다 작다
    graph[b][a]=2 #반대로 b학생이 a학생보다 크다고도 알 수 있음

#for i in graph:
#    print(i)

for k in range(n):
    for i in range(n):
        for j in range(n):
            if (graph[i][k]==1 and graph[k][j]==1): #i는 j보다 작다
                graph[i][j]=1
            elif (graph[i][k]==2 and graph[k][j]==2): #i는 k보다 크다
                graph[i][j]=2
#print()
#for i in graph:
#    print(i)

#정답 계산
count=0
for i in range(n):
    isPossible=True
    for j in range(n):
        if (graph[i][j]==MAX_COST and i!=j):
            isPossible=False
            break

    if isPossible:
        count+=1

print(count)
    
'''
1번부터  N(2 ≤ N ≤ 500)번까지 번호가 붙여져 있는 학생들
두 학생 키를 비교한 횟수 M (0 ≤ M ≤ N(N-1)/2)
N명의 학생들의 키는 모두 다르다
자신의 키가 몇 번째인지 정확히 알 수 있는 학생이 모두 몇명인지 출력
a학생이 b학생보다 키가 작다

일단 모든 n명의 학생에 대해 다 검사해야함
등수를 구할 수 있으면 graph에 값이 담길것임

pypy3으로만 풀림
'''
    
