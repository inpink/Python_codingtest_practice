import sys
input = sys.stdin.readline

n=int(input())
costs=list(map(int,input().split()))
m=int(input())

dp = [-1 for i in range(m+1)]

for money in range(1,m+1): #money원으로 살 수 있는 최대 금액이 dp[money]다

  for j in range(n):
    cost=costs[j]

    if cost<=money: #6 13    7 13    13 13      6 21   7 21   8 21     1 3, 2 3, 3 3
      if dp[money-cost]==-1:
        dp[money] = max(dp[money],j)
      else:
        temp=str(j)+str(dp[money-cost])
        new_digit=int("".join(sorted(temp, reverse=True)))
        # print(money,new_digit, dp)
        dp[money]=max(dp[money], new_digit)

  # print(money,"(money)",dp)

print(max(dp))