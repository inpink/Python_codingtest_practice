import sys
input = sys.stdin.readline

'''
가치의 합이 k원
동시에 동전의 개수가 최소
불가능한 경우에는 -1을 출력한다.
조건: 각각의 동전은 몇 개라도 사용할 수 있다.
조건: 1 ≤ n ≤ 100, 1 ≤ k ≤ 10,000, 1<= 각동전 가치 <= 100000
조건: 가치가 같은 동전이 여러 번 주어질 수도 있다.
'''

'''
dp문제 

'''
n,k=map(int, input().split(" "))

coins=[]
for i in range(n):
    coins.append(int(input()))

dp=[100001 for i in range(k+1)]
dp[0]=0

for i in range(1,k+1,1):

    for coin in coins:
        if i-coin>=0:
            dp[i] = min(dp[i], dp[i-coin]+1)

if dp[k]==100001: #만들 수 없는 경
    print(-1)
else:
    print(dp[k])


        
