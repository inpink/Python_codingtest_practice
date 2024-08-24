import sys
input=sys.stdin.readline

r,c,t=map(int,input().split()) #r줄, c칸, t초

graph=[]
for i in range(r):
  row=list(map(int,input().split()))
  graph.append(row)

dir=[[-1,0],[1,0],[0,-1],[0,1]] #상하좌우 xy

def 확산(graph,air1X,air2X):
  newGraph=[ [0 for i in range(c)] for i in range(r) ]
  for x in range(r):
    for y in range(c):
      cell=graph[x][y]
      if cell>=1: #미세먼지 있으면

        확산횟수=0
        확산할곳=[]
        for dirX,dirY in dir:
          adjX=dirX+x
          adjY=dirY+y

          if adjX<0 or adjX>=r or adjY<0 or adjY>=c: #칸 범위 벗어남
            continue
          if graph[adjX][adjY]==-1: #공기청정기 있음
            continue #확산안됨
          확산횟수+=1
          확산할곳.append([adjX,adjY])

        확산될먼지=cell//5
        남은먼지=cell-확산될먼지*확산횟수

        for adjX,adjY in 확산할곳:
          newGraph[adjX][adjY]+=확산될먼지
        newGraph[x][y]+=남은먼지

  #에어컨은 갖다놓기
  newGraph[air1X][0]=-1
  newGraph[air2X][0]=-1

  # print("graph",graph)
  # print("newGraph",newGraph)
  return newGraph

def 공기청정기위치(graph):
  위쪽공기청정기=0
  아래쪽공기청정기=0

  for x in range(r):
    cell=graph[x][0]
    if cell==-1:
      if 위쪽공기청정기==0:
        위쪽공기청정기=(x,0)
      else:
        아래쪽공기청정기=(x,0)
        break

  # print(위쪽공기청정기,아래쪽공기청정기)
  return (위쪽공기청정기,아래쪽공기청정기)

def 위쪽순환(graph,위쪽공기청정기):
  x,y=위쪽공기청정기 #x,0
  빠진미세=0

  for 위쪽행 in range(x-1,-1,-1):
    if 위쪽행==x-1:
      빠진미세+=graph[위쪽행][y]
      # print(빠진미세,"위")
      continue

    graph[위쪽행+1][0]=graph[위쪽행][0]

  for 위쪽열 in range(c):
    if 위쪽열==0:
      graph[1][0]=graph[0][0]
      continue
    graph[0][위쪽열-1]=graph[0][위쪽열]


  for 오른쪽행 in range(1,x+1):
    graph[오른쪽행-1][-1]=graph[오른쪽행][-1]

  for 아래열 in range(c-1,0,-1):
    graph[x][아래열]=graph[x][아래열-1]

    if 아래열==1:
      graph[x][아래열]=0

  return (graph,빠진미세)

def 아래쪽순환(graph,아래쪽공기청정기):
  x,y=아래쪽공기청정기 #x,0
  빠진미세=0

  for 위쪽행 in range(x+1,r):
    if 위쪽행==x+1:
      빠진미세+=graph[위쪽행][0]
      # print(빠진미세,"아래")
      continue

    graph[위쪽행-1][0]=graph[위쪽행][0]

  for 위쪽열 in range(c):
    if 위쪽열==0:
      graph[r-2][0]=graph[r-1][0]
      continue
    graph[r-1][위쪽열-1]=graph[r-1][위쪽열]


  for 오른쪽행 in range(r-1,x,-1):
    graph[오른쪽행][-1]=graph[오른쪽행-1][-1]

  for 아래열 in range(c-1,0,-1):
    graph[x][아래열]=graph[x][아래열-1]

    if 아래열==1:
      graph[x][아래열]=0

  return (graph,빠진미세)



def 총미세먼지량(graph):
  summ=0
  for x in range(r):
    for y in range(c):
      cell=graph[x][y]
      summ+=cell

  summ+=2
  # print("총미세먼지량",summ)

  return summ

처음총미세=총미세먼지량(graph)
위쪽공기청정기,아래쪽공기청정기=공기청정기위치(graph)

빠진미세=0
for i in range(t):
  newGraph=확산(graph,위쪽공기청정기[0],아래쪽공기청정기[0])

  # for i in newGraph:
  #   print(i)

  newGraph,추가빠진미세1=위쪽순환(newGraph,위쪽공기청정기)
  newGraph,추가빠진미세2=아래쪽순환(newGraph,아래쪽공기청정기)

  # for i in newGraph:
  #   print(i)

  빠진미세+=(추가빠진미세1+추가빠진미세2)

  # print(빠진미세)
  # print()

  graph=newGraph

print(처음총미세-빠진미세)