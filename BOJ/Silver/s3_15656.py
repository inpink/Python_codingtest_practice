import sys

input = sys.stdin.readline


def dfs():
    if len(s) == m:
        for i in s:
            print(l[i - 1], end=' ')
        print()
        return
    for i in range(1, n + 1):
        s.append(i)
        dfs()
        s.pop()


n, m = map(int, input().split())
l = list(map(int, input().split()))
l = sorted(l)
s = []
dfs()  # 탐색 시작
