import sys
input = sys.stdin.readline


def calculate(candidates):
  candidates.sort(reverse=True)

  maxCandi=max(candidates)

  count=maxCandi
  for i in range(1,len(candidates)):
    if i+candidates[i]>maxCandi:
      count+=i+candidates[i]-maxCandi
      maxCandi=max(maxCandi, i+candidates[i])
  return count

# print(calculate([4,4,3,1]))

n=int(input())
numbers=list(map(int,input().split()))

graph=[[] for i in range(n)] #graph[i]=[a,b] i의 자식은 a,b

for i in range(1,n):
  number=numbers[i]
  graph[number].append(i)

# print(graph)

def dfs(x):
  count=1
  candidates=[]
  for child in graph[x]:
    candidates.append(dfs(child))
  if len(candidates)==0: #리프노드
    count=1
  else:
    count+=(calculate(candidates))

  # print(x,"(x),", count, "(count)") #x윗가지까지 비용
  return count

print(dfs(0)-1)


