import sys

input = sys.stdin.readline

# 전체 스도쿠가 2차원 리스트로 담긴다.
doku = []  # 0인 것들은 유망한 값으로 업데이트 되고, 유망하지 않으면 삭제되는 방식으로 업데이트 된다
blank = []  # 0인 것들의 x,y 쌍을 2차원 리스트로 담아준다. 이렇게 해야, 틀리면 이전 0값으로 이동할 수 있다★

# 입력받기
for i in range(9):
    help = list(map(int, input().split()))
    doku.append(help)

for i in range(9):
    for j in range(9):
        if doku[i][j] == 0:  # 빈 칸만
            blank.append([i, j])  # blank에 2차원 리스트로 모은다.


def checkRow(x, a):  # x는 doku에서의 행, a는 내가 넣을 수.
    # 가로에 같은 값이 있는 지 검사하는 것이기 때문에 x만 검사한다.
    for i in range(9):
        if doku[x][i] == a:  # 하나라도 같은 값이 있으면 종료
            return False
    return True


def checkCol(y, a):
    for i in range(9):
        if doku[i][y] == a:
            return False
    return True


def checkRect(x, y, a):
    # ★3x3 칸을 검사하는 방법. 3x3 칸에서 가장 왼쪽 위값의 인덱스를 찾아준다.
    nx = x // 3 * 3  # 수학적인 규칙. x=4번째 줄이면 3번째 줄이 가장 왼쪽 위 줄이다.
    ny = y // 3 * 3  # 외우기.
    for i in range(3):
        for j in range(3):
            if a == doku[nx + i][ny + j]:
                return False
    return True


def dfs(idx):
    # 완전 종료 조건
    if idx == len(blank):  # 얘도 마찬가지로 idx+1 하다가 "모든 blank의 검사가 끝났으면 dfs 완전 종료하기
        for i in doku:
            for j in i:
                print(j, end=' ')
            print()
        exit(0)  # 1개의 해를 찾아도 다른 해를 찾아나서는 다른 문제들과 다르게, 이 문제는 해를 1개라도 찾으면 바로 즉시 종료해야 시간 초과가 안난다. 해는 1개밖에 없다.

    for i in range(1, 10):  # 여기에서 i는, 0번에 들어갈 1~9 숫자. 아래에서 if문을 통해 '유망한' 1~9 중 숫자만 넣어가며, 틀리면 백하며 백트래킹.
        # ★ blank에서 하나하나 꺼낸다.
        x = blank[idx][0]  # x는, doku 2차원 배열에서 몇번째 x줄에 있는 지를 의미한다. 이 문제에서 x는 행이다.
        y = blank[idx][1]
        if checkRow(x, i) and checkCol(y, i) and checkRect(x, y, i):  # 3개 다 True여야(3개 다 겹치는 숫자가 없어야)
            doku[x][y] = i  # 백
            dfs(idx + 1)  # 트
            doku[x][y] = 0  # 래킹


dfs(0)  # blank에서 0번째 0부터 탐색 시작
