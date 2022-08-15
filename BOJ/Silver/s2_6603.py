import sys

input = sys.stdin.readline


# kl에서 몇번째 index를 중복없이 출력해주냐! (중복 없어야 해서 visited 필요하다)
# 사전순이라 a<b<c<d 돼야 함
# n=7이면, 0부터 6까지를 오름차순으로 두는 것

def dfs():
    # 탐색 종료 조건
    if len(s) == 7:
        for i in s:
            if i != 0:  # 0번째 빼고 모두 가로로 출력해준다.
                print(kl[i], end=' ')
        print()
        return

    for i in range(1, kl[0] + 1):
        if visited[i - 1] == False and s[-1] < i:  # ★s에 i보다 큰 수가 담긴다..  일단 i로 담고 출력할 때kl에서 출력해주자
            visited[i - 1] = True  # 방문함
            s.append(i)  # 방문함
            dfs()
            # ★여기로 내려왔다는 것은 case 한개가 출력되었다는 것.
            s.pop()
            visited[i - 1] = False


s = [0]  # 1담기고 2담기고 2빠지고 하면서 각 정답 담아줄 리스트
# 오름차순 탐색을 위해 0을 담아놔준다.

while True:
    kl = list(map(int, input().split()))
    if kl[0] == 0:
        break
    visited = [False] * kl[0]
    dfs()
    print()  # 끝나면 한 칸 띄우기
