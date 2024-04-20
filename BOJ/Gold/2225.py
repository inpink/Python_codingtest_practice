import sys
input = sys.stdin.readline
ans=0

n,k=map(int,input().split())

dp=[[1 for i in range(k+1)] for i in range(n+1)]

for i in range(1,n+1):
    for j in range(1,k+1):
        thisSum=0
        for a in range(0,i+1):
            thisSum+=dp[i-a][j-1]
        dp[i][j]=thisSum

ans=dp[n][k-1]
print(ans%(10**9))
'''

0~N K개 합이 N이 되는 "경우의 수"
덧셈의 순서가 바뀐 경우는 다른 경우로 센다(1+2와 2+1은 서로 다른 경우).
 또한 한 개의 수를 여러 번 쓸 수도 있다.
 
 N(1 ≤ N ≤ 200), K(1 ≤ K ≤ 200)
 
 답을 1,000,000,000으로 나눈 나머지를 출력
'''