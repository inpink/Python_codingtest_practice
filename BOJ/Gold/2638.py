import sys
input = sys.stdin.readline
from collections import deque
n,m= map(int,input().split())


graph=[]
ones=set()

for i in range(n):
  row =  list(map(int, input().split()))
  graph.append(row)
  for j in range(m):
    square = row[j]
    if square==1:
      ones.add((i,j))


for i in graph:
  print(i)
print(ones)

q = deque([])
while True:
  if len(q)==0:
    break


