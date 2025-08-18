import sys
input = sys.stdin.readline

def answer(k, start, n):
  if k<n: #전체 순회 전
    return nodes[k]
  else: #전체 순회 후(사이클로 가야함)
    cycleLen = n-start #사이클 길이= (n-start)
    return nodes[(k-start) % cycleLen + start] #사이클 전은 start개만큼만 해당된다. 사이클은 k-start개만큼 해당된다.

n,m,v = map(int, input().split())
nodes = list(map(int, input().split()))
for i in range(m):
  k= int(input())
  print(answer(k, v-1, n))



'''
노드 개수 n개(2~20만)
질문 m번(1~20만)

사이클이 발생한 곳의 start에 진입한 순간, 그 이후로는 무조건 사이클 내에서만 빙빙 돈다.


민달팽이 예시
2 3 2
10 20
1
2
5
'''