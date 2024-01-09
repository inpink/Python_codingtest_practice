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



'''
Write a Solution after solving this problem
: dp문제임은 명확했음. i 시점에서 최선의 값이 담기기 때문. 
i원을 만들 때 단순히 이전 값(i-1같은)에서 dp[i-(i-1)]을 더해서 사용하는 것이 아니라,
최소가 갱신되는 경우는, 새로운 coin 1개로 바꿔치기 하는 경우이다. 
따라서 모든 coins에 대해 바꿔치기할 수 있는지 검사한다. ☆dp[i-coin]+1☆
'''
