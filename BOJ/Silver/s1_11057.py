import sys
input = sys.stdin.readline

n=int(input())

#DP[n자리수][시작수]=DP[n][0~9]-DP[n-1][0~9 -1]

dp = [[ 0 for i in range(10) ] for i in range(n+2)]

for i in range(10):
    dp[1][i]=1

for i in range(2,n+2):
    dp[i][0]=sum(dp[i-1])
    for j in range(1,10):
       dp[i][j]=dp[i][j-1]-dp[i-1][j-1]

#print(dp)
#print(sum(dp[1]))
print(dp[n+1][0] % 10007)


# 10007으로 나눈 나머지 출력하기