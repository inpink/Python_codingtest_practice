import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

t = int(input())


def dfs(thisNode, inList, outList, times, dp):
  if dp[thisNode]!=-1:
    return dp[thisNode]
  ins=inList[thisNode]


  if len(ins)==0:
    dp[thisNode] = max(dp[thisNode],times[thisNode])
    return times[thisNode]

  beforeTimes = []
  for beforeNode in ins:
    beforeTimes.append(times[thisNode]+dfs(beforeNode, inList, outList, times, dp))


  dp[thisNode] = max(dp[thisNode],max(beforeTimes))
  # print(thisNode, dp)
  return dp[thisNode]



for case in range(t):
  n, k = map(int, input().split()) #노드 n개, 선 k개
  times = [0] + list(map(int, input().split())) #걸리는 시간

  inList = [ [] for i in range(n+1)] # b를 가려면 a가 있어야 한다
  outList = [ [] for i in range(n+1)] #a에서 b를 갈수있다
  for i in range(k):
    x, y = map(int, input().split()) #x->y
    inList[y].append(x)
    outList[x].append(y)

  # print("inList:",inList)
  # print("outList:",outList)

  arrive=int(input())


  dp = [ -1 for i in range(n+1)]
  print(dfs(arrive, inList, outList, times,dp))



