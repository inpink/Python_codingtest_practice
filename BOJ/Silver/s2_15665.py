import sys

input = sys.stdin.readline


def dfs():
    if len(s) == m:
        for i in s:
            print(i, end=' ')
        print()
        return
    for i in l:
        s.append(i)
        dfs()
        s.pop()


n, m = map(int, input().split())
l = list(map(int, input().split()))
l = set(l)
l = list(l)
l = sorted(l)
s = []
visited = [False] * n
dfs()  # 탐색 시작
