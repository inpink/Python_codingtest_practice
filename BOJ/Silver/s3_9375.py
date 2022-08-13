import sys

input = sys.stdin.readline


# 실3. 소요시간 10분.
# ★알몸이 아닌 경우로
def re(n):
    dic = {}
    for i in range(n):
        a, b = map(str, input().split())
        if b in dic:
            dic[b] += 1
        else:
            dic[b] = 1
    # print(dic)
    sum = 1
    for i in dic:  # dic에 들어온 자리 개수만큼
        sum *= (dic[i] + 1)
    print(sum - 1)


t = int(input())

for i in range(t):
    n = int(input())
    re(n)
