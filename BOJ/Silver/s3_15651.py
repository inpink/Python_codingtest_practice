import sys

input = sys.stdin.readline


# dfs는 깊이 우선 탐색. 재귀 함수로 구현한다.
def dfs():
    # 탐색 종료 조건 (★하나의 dfs가 종료되는 조건)
    if len(s) == m:
        for i in s:
            print(i, end=' ')
        print()
        return

    # 탐색하며 s에 담고 뺴고 하기
    for i in range(1, n + 1):  # i=1,2,3,4
        if 1:  # 방문하지 않은 경우에만 방문하자
            visited[i - 1] = True  # 방문함
            s.append(i)  # 방문함
            # 값 넣은 다음에 또 탐색 시작
            # print("i",i,"일 때 dfs 실행") #dfs 재귀 실행될 때 마다 확인하면 좀 더 이해하기 쉽다.
            dfs()  # 재귀함수이기 때문에, 얘는 결국 for문(n) 안에 for문(n)이 쓰이게되는 것. n=4이면 4차 for문이 쓰이게 된다. 물론 종료 조건이 있기에 n^4는 아니다. 백트래킹(DFS)는 근본적으로는 brute force처럼 모든 걸 탐색하는 걸 기반으로 하지만, 트리를 쳐내는 조건 (if break) 때문에 효율적이게 되는 것이다.
            # ★여기로 내려왔다는 것은 case 한개가 출력되었다는 것.
            s.pop()
            visited[i - 1] = False
            # print(i,s,visited)
            # print()


n, m = map(int, input().split())
s = []  # 각 케이스를 담아줄 리스트. 1234 1243 이렇게 값이 삭제되고 담기고 하면서 진행된다
visited = [False] * n  # n개만큼 F를 만들어준다. 방문한 상태면 T가 된다.
dfs()  # 탐색 시작
