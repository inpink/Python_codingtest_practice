import sys

input = sys.stdin.readline


def w(a, b, c):
    # 재귀를 최소화한 이번 문제의 dp는,모르는 값만 탐색한다.
    # 모르는 값을 탐색할 때, 순서는 그냥 이 문제의 재귀 알고리즘을 따른다.(약간 뇌뺴고 코드 짜도 되는 느낌)

    # 있는값 1
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)  # 밑에,위에 애들도 전부 return을 쓰고 있기 때문에, return을 꼭 해줘야 값을 토스하면서 출력된다.

    # 있는값 2
    if dp[a][b][c] != 0:  # 값이 이미 있으면
        return dp[a][b][c]

    # 값이 없으면 탐색하기. 이러면 이미 검색한 값을 또 검색하지 않는다.
    if a < b < c:
        dp[a][b][c] = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
    else:
        dp[a][b][c] = w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1)
    #
    return dp[a][b][c]


dp = [[[0 for _ in range(21)] for _ in range(21)] for _ in range(21)]

while True:
    a, b, c = map(int, input().split())

    if a == -1 and a == b == c:
        break

    print("w(" + str(a) + ", " + str(b) + ", " + str(c) + ") =", w(a, b, c))
