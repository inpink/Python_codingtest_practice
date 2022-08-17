import sys

input = sys.stdin.readline


def dfs():
    if len(s) == m + 1:
        for i in s:
            if i != 0:
                print(i, end=' ')
        print()
        return
    for i in range(n):
        if s[-1] <= l[i]:
            s.append(l[i])
            dfs()
            s.pop()


n, m = map(int, input().split())
l = list(map(int, input().split()))
l = sorted(l)  # 정렬 해줘야 한다.
s = [0]
dfs()  # 탐색 시작
