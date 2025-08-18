import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())

graph = [[] for i in range(n + 1)]
inDegree = [0 for i in range(n+1)]
for i in range(m):
  a, b = map(int, input().split())
  graph[a].append(b) #1. a->b
  inDegree[b]+=1 #2. b는 이 개수만큼 상위에 있다


# 3.root 후보를 고른다
q= deque([])
for i in range(1,n+1):
  if inDegree[i]==0:
    q.append(i)

ans=[]
while True:
  if len(q)==0:
    break
  cur = q.popleft()
  ans.append(cur) #4. root끼리는 순서가 상관없다. 현재 root인 것들을 상단에 담아준다.

  for i in graph[cur]:
    inDegree[i]-=1 #5. 상단에 담겼기 때문에 상위 의존성 하나 제거한다. 이 친구도 이로 인해 root가 된다면 다음 반복에서 ans 리스트에 담아준다.
    if inDegree[i]==0:
      q.append(i)

print(*ans)



'''
N명의 학생들을 키 순서대로 줄을 세우려고 한다
각 학생의 키를 알지 못한다

일부 학생들만 두 학생의 키를 비교했다
줄을 세우는 프로그램을 작성
 
 N(1 ≤ N ≤ 32,000), M(1 ≤ M ≤ 100,000)
 M은 키를 비교한 횟수
 
 A,B = A가 B 앞에 슨다
 학생들의 번호는 1번부터 N번이다.
 답이 여러 가지인 경우에는 아무거나 출력
 
 
 
 n=3 m=2
1 3
2 3

1 2 3



n=4 m=2
4 2
3 1 

4 2 3 1


logm
n+m
n
m

'''