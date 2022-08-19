import sys

input = sys.stdin.readline


def dfs():
    if len(s) == m:
        for i in s:
            print(i, end=' ')
        print()
        return
    for i in d:
        if d[i] > 0:
            s.append(i)
            d[i] -= 1
            dfs()
            s.pop()
            d[i] += 1


n, m = map(int, input().split())
l = list(map(int, input().split()))
l = sorted(l)

d = {}
for i in l:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1
# print(d)
s = []
visited = [False] * n
dfs()  # 탐색 시작
