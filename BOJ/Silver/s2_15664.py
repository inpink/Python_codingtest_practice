import sys

input = sys.stdin.readline


def dfs():
    if len(s) == m + 1:
        for i in s:
            if i != 0:
                print(i, end=' ')
        print()
        return
    for i in d:
        if d[i] > 0 and s[-1] <= i:
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
s = [0]
visited = [False] * n
dfs()  # 탐색 시작
