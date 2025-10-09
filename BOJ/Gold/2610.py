import sys
input = sys.stdin.readline

INF = 10**9

# ---------- 입력 ----------
n = int(input().strip())
m = int(input().strip())

# 유니온-파인드(Disjoint Set Union)
parent = list(range(n + 1))

def find(x):
  while parent[x] != x:
    parent[x] = parent[parent[x]]
    x = parent[x]
  return x

def union(a, b):
  ra, rb = find(a), find(b)
  if ra != rb:
    parent[rb] = ra

# 인접 행렬(거리 행렬) - 플로이드 워셜용
dist = [[INF] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
  dist[i][i] = 0

for _ in range(m):
  a, b = map(int, input().split())
  union(a, b)
  # 무가중치 양방향 그래프
  dist[a][b] = 1 # ⭐
  dist[b][a] = 1 # ⭐

# ---------- 플로이드 워셜 ----------
for k in range(1, n + 1):
  dk = dist[k]
  for i in range(1, n + 1):
    di = dist[i]
    ik = di[k]
    if ik == INF:
      continue
    # j 루프를 안쪽으로 두는 일반형
    for j in range(1, n + 1):
      nk = ik + dk[j]
      if nk < di[j]:
        di[j] = nk

# ---------- 컴포넌트(위원회) 구성 ----------
# 각 노드의 루트를 갱신(경로압축 결과 반영)
for i in range(1, n + 1):
  parent[i] = find(i)

components = dict()
for i in range(1, n + 1):
  r = parent[i]
  components.setdefault(r, []).append(i)

# for i in dist:
#   print(i)
# print(parent)
# print(components)

# ---------- 각 컴포넌트 대표 선출 ----------
representatives = []

for comp_nodes in components.values():
  best_node = None
  best_ecc = INF

  # comp 내부에서의 이심도 계산: 해당 노드에서 comp 내 모든 노드까지 최단거리의 최댓값
  for node in comp_nodes:
    ecc = 0
    for neighbor_node in comp_nodes:
      ecc = max(ecc, dist[node][neighbor_node])
    if ecc < best_ecc:
      best_ecc = ecc
      best_node = node

  representatives.append(best_node)

# ---------- 출력 ----------
representatives.sort()
# print(representatives)
print(len(representatives))
print("\n".join(map(str, representatives)))

'''
서로 알고 있는 사람은 반드시 같은 위원회에 속해야 한다.
 위원회의 수는 최대가 되어야 한다.
 각 위원회의 대표를 한 명씩 뽑아야 한다.
 각 참석자는 자신이 알고 있는 사람에게만 의견을 전달할 수 있어 대표에게 의견을 전달하기 위해서는 때로 여러 사람을 거쳐야 한다. 
 . 대표에게 의견을 전달하는 경로가 여러 개 있을 경우에는 가장 적은 사람을 거치는 경로로 의견을 전달하며 이때 거치는 사람의 수를 참석자의 의사전달시간이라고 함
 위원회에서 모든 참석자들의 의사전달시간 중 최댓값이 최소가 되도록 대표를 정하라 
 
 예를 들어 1번, 2번, 3번 세 사람으로 구성되어 있는 위원회에서 1번과 2번, 2번과 3번이 서로 알고 있다고 하자. 1번이 대표가 되면 3번이 대표인 1번에게 의견을 전달하기 위해서 2번을 거쳐야만 한다. 반대로 3번이 대표가 되어도 1번이 대표인 3번에게 의견을 전달하려면 2번을 거쳐야만 한다. 하지만 2번이 대표가 되면 1번과 3번 둘 다 아무도 거치지 않고 대표에게 직접 의견을 전달 할 수 있다. 따라서 이와 같은 경우 2번이 대표가 되어야 한다.
 
 참석자들은 1부터 N까지의 자연수로 표현되며 회의에 참석하는 인원은 100 이하이다
 
 
 출력
 첫째 줄에는 구성되는 위원회의 수 K를 출력한다.
 다음 K줄에는 각 위원회의 대표 번호를 작은 수부터 차례로 한 줄에 하나씩 출력한다. 한 위원회의 대표가 될 수 있는 사람이 둘 이상일 경우 그중 한 명만 출력하면 된다.
 
 
풀이법
- 같은 그룹인지는 union find로 체크
- 8처럼 혼자 그룹인 친구도 빼먹지 말기
- 대표로부터 각 노드의 최단거리는 다익스트라 여러번 or 플로이드 워셜

'''