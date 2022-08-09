import sys

input = sys.stdin.readline

a = int(input())
n = list(map(int, input().split()))

b = int(input())
m = list(map(int, input().split()))

# 개수 셀 때는 딕셔너리(다른데선 map이라고 하기도 한다)
dic = {}

for i in n:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

for i in m:
    if i not in dic:
        print(0, end=' ')
    else:
        print(dic[i], end=' ')
