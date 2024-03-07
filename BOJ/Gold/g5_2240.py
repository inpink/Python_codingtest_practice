import sys
input=sys.stdin.readline

t,w=map(int,input().split())

dp=[[[-1 for i in range(w+2)] for i in range(3)] for i in range(t+1)]
falls=[-1]
for i in range(t):
    falls.append(int(input()))

opposite={1:2, 2:1}
dp[0][1][0]=0
maxValue=-1
for i in range(1,t+1): #i초 (1~t)
    for j in range(1,3): #위치j (1,2)
        for k in range(t+1): #움직인횟수k (0~t)
            if k>w: #w번까지만 움직일 수 있음
                break
            #k횟수에서 : 반대쪽에서 움직이기 vs 같은쪽에 가만히 있기
            move=dp[i-1][opposite[j]][k-1]
            stay=dp[i-1][j][k]

            if stay!=-1 and falls[i]==j: #현재 i초에 j 위치에 자두가 있으면 +1
                stay+=1
            else:
                if move!=-1:
                    move+=1

            dp[i][j][k]= max(dp[i][j][k],max(stay,move))
            maxValue=max(maxValue,dp[i][j][k])


print(maxValue)