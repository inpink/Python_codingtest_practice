import sys

input = sys.stdin.readline


# dfs는 깊이 우선 탐색. 재귀 함수로 구현한다.
def dfs():
    # 탐색 종료 조건 (★하나의 dfs가 종료되는 조건)
    if len(s) == m + 1:  # m개수만큼 들어오면 출력하고 종료한다.
        for i in s:
            if i != 0:  # 0번째 빼고 모두 가로로 출력해준다.
                print(i, end=' ')
        print()
        return  # 종료

    # 탐색하며 s에 담고 뺴고 하기
    for i in range(1, n + 1):  # i=1,2,3,4
        if s[-1] <= i:  # s의 가장 큰 값보다 크거나 같은 경우에만 방문한다.
            s.append(i)  # 방문함
            dfs()
            # ★여기로 내려왔다는 것은 case 한개가 출력되었다는 것.
            s.pop()
            # print(i,s,visited)
            # print()


n, m = map(int, input().split())
s = [0]  # 오름차순 탐색을 위해 0을 담아놔준다.
visited = [False] * n  # n개만큼 F를 만들어준다. 방문한 상태면 T가 된다.
dfs()  # 탐색 시작
