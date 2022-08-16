import sys

input = sys.stdin.readline


# 중복x => visited
# 오름차순x => s=[]

def dfs():
    if len(s) == m:
        for i in s:
            print(l[i - 1], end=' ')
        print()
        return

    for i in range(1, n + 1):  # i=1,2,3,4
        if visited[i - 1] == False:
            visited[i - 1] = True  # 방문함
            s.append(i)  # 방문함
            dfs()
            # ★여기로 내려왔다는 것은 case 한개가 출력되었다는 것.
            s.pop()
            visited[i - 1] = False


n, m = map(int, input().split())
l = list(map(int, input().split()))
l = sorted(l)  # 정렬을 해줘야 오름차순으로 나온다
s = []
visited = [False] * n
dfs()
