import sys
input=sys.stdin.readline
from collections import deque

n,l,r=map(int,input().split())
graph=[]
for i in range(n):
    row=list(map(int,input().split()))
    graph.append(row)

directions=[(1,0),(-1,0),(0,1),(0,-1)]
count=0
changed=True
ansCount=0
while True:
    if changed==False:
        break
    changed=False
    checked=[[False for i in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if checked[i][j]: #이미 그룹 만들어졌으면 패스하기
                continue

            #bfs
            checked[i][j]=True
            q=deque([[i,j]])
            numbersSum=graph[i][j]
            numbers=[(i,j)]
            while True:
                if len(q)==0:
                    break
                x,y=q.popleft()
                #print(x,y)

                for dirX,dirY in directions:
                    if 0<=x+dirX<n and 0<=y+dirY<n and checked[x+dirX][y+dirY]==False and l<=abs(graph[x+dirX][y+dirY]-graph[x][y])<=r: #아래
                        checked[x+dirX][y+dirY]=True
                        q.append([x+dirX,y+dirY])
                        numbersSum+=graph[x+dirX][y+dirY]
                        numbers.append((x+dirX,y+dirY))
            #bfs 끝

            #하나의 그룹이 만들어졌으면 인구 이동
            if len(numbers)>1:
                changed=True
                people=numbersSum//len(numbers)

                for x,y in numbers:
                    graph[x][y]=people

    #이동 횟수 체크는 여기서
    if changed:
        ansCount+=1

    #for i in range(n):
    #print(graph[i])
    #print()

print(ansCount)