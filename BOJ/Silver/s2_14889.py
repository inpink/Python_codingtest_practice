import sys

input = sys.stdin.readline


def 순열계산(l):
    # 2개만 뽑는 거니까 중복 for문으로 가능하다.
    sum = 0
    # print(l)
    for i in range(1, len(l)):  # 1 #2
        for j in range(1, len(l)):  # 2 #1
            if i != j:
                # print("*",i,j,l[i]-1,l[j]-1)
                sum += score[l[i] - 1][l[j] - 1]
    # print()
    return sum


score = []
n = int(input())
for i in range(n):
    help = list(map(int, input().split()))
    score.append(help)

min_value = 10000  # 100x100=만이 최대값


# dfs는 깊이 우선 탐색. 재귀 함수로 구현한다.
def dfs():
    global s2, min_value
    # 탐색 종료 조건 (★하나의 dfs가 종료되는 조건)
    if len(s) == n // 2 + 1:
        # print("1번 팀:",s)
        for k in range(1, n + 1):
            if k not in s:
                s2.append(k)
        # print("2번 팀:",s2)
        # print("차:",abs(순열계산(s2)-순열계산(s)))
        # print()
        cha = abs(순열계산(s2) - 순열계산(s))
        if cha < min_value:
            min_value = cha

        s2 = [0]  # 상대 팀을 다 찾았으니 초기화해서 돌려준다. s만 백트캐링 된다.
        return

    # 탐색하며 s에 담고 뺴고 하기
    for i in range(1, n + 1):  # i=1,2,3,4
        if visited[i - 1] == False and s[-1] < i:  # 방문하지 않은 경우에만 방문하자
            visited[i - 1] = True  # 방문함
            s.append(i)  # 방문함
            dfs()  # 재귀함수이기 때문에, 얘는 결국 for문(n) 안에 for문(n)이 쓰이게되는 것. n=4이면 4차 for문이 쓰이게 된다. 물론 종료 조건이 있기에 n^4는 아니다. 백트래킹(DFS)는 근본적으로는 brute force처럼 모든 걸 탐색하는 걸 기반으로 하지만, 트리를 쳐내는 조건 (if break) 때문에 효율적이게 되는 것이다.
            # ★여기로 내려왔다는 것은 case 한개가 출력되었다는 것.
            s.pop()
            visited[i - 1] = False
            # print(i,s,visited)
            # print()


s = [0]  # 각 케이스를 담아줄 리스트. 1234 1243 이렇게 값이 삭제되고 담기고 하면서 진행된다
s2 = [0]
visited = [False] * n  # n개만큼 F를 만들어준다. 방문한 상태면 T가 된다.
dfs()  # 탐색 시작
print(min_value)
