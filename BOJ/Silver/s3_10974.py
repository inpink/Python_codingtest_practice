import sys

input = sys.stdin.readline


def dfs():
    if len(s) == n:
        for i in s:
            print(i, end=' ')
        print()
        return

    for i in range(1, n + 1):
        if visited[i - 1] == False:
            visited[i - 1] = True
            s.append(i)
            dfs()
            s.pop()
            visited[i - 1] = False


n = int(input())
s = []  # 각 케이스를 담아줄 리스트. 1234 1243 이렇게 값이 삭제되고 담기고 하면서 진행된다
visited = [False] * n  # n개만큼 F를 만들어준다. 방문한 상태면 T가 된다.
dfs()  # 탐색 시작
