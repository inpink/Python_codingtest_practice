import sys
input = sys.stdin.readline

n,k=map(int,input().split())
medals=[]
for i in range(n):
  nation, gold, silver, bronze = map(int,input().split())
  medals.append([gold,silver,bronze,nation])

medals.sort(key=lambda x:(-x[0], -x[1], -x[2]))


before_rank=[0,0,0,0,0] #
for i in range(n):
  if before_rank[0:3] == medals[i][0:3]:
    medals[i].append(before_rank[4])
  else:
    medals[i].append(i+1)

  before_rank=medals[i]

  if k==before_rank[3]:
    print(before_rank[4])