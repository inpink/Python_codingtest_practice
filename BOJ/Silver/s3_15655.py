import sys

input = sys.stdin.readline


def dfs():
    if len(s) == m + 1:
        for i in s:
            if i != -1:
                print(l[i], end=' ')
        print()
        return

    for i in range(n):
        if visited[i] == False and s[-1] < i:
            visited[i] = True
            s.append(i)
            dfs()
            s.pop()
            visited[i] = False


n, m = map(int, input().split())
l = list(map(int, input().split()))
l = sorted(l)
s = [-1]
visited = [False] * n
dfs()
