import sys
input=sys.stdin.readline

n=int(input())
colors=[]

for i in range(n):
  r,g,b=map(int,input().split())
  colors.append([r,g,b])

# print(colors)

INF=2147000000
ans=INF
for i in range(3):
  dp=[[INF,INF,INF] for i in range(n)]
  dp[0][i]=colors[0][i] #(0,i)빼고는 다 불가능하게 막아버림. start 3가지는 반드시 고정해서 탐색하면 됨

  for j in range(1,n):
    dp[j][0]=colors[j][0]+min(dp[j-1][1],dp[j-1][2])
    dp[j][1]=colors[j][1]+min(dp[j-1][0],dp[j-1][2])
    dp[j][2]=colors[j][2]+min(dp[j-1][0],dp[j-1][1])

  #정답 갱신
  for j in range(3):
    if i != j:
      ans = min(ans, dp[-1][j])
print(ans)