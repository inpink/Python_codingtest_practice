import sys
input=sys.stdin.readline

s1=input().rstrip()
s2=input().rstrip()

dp=[[ 0 for i in range(len(s2))] for i in range(len(s1))]
for i in range(len(s1)):
    for j in range(len(s2)):
        if s1[i]==s2[j]:
            if i==0 or j==0:
                dp[i][j]=1
            else:
                dp[i][j]=dp[i-1][j-1]+1

#print(dp)

ans=0
for i in dp:
    ans=max(ans,max(i))

print(ans)