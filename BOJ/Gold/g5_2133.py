import sys
input = sys.stdin.readline

n=int(input())


if n%2==1:
    print(0)
    sys.exit()


dp=[0]*31
dp[2]=3

for i in range(4,31,2): #dp[4], dp[6], dp[8]...
    dp[i]=dp[i-2]*3+2
    for j in range(2,i-2,2): #i=10일 때는, j=2,4,6
        dp[i]+=dp[j]*2

print(dp[n])
