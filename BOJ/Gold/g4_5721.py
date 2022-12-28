import sys

input = sys.stdin.readline

while True:
    m, n = map(int, input().split())
    if m == n == 0:
        break
    boxes = [[0 for i in range(n + 2)] for i in range(2)]
    dp = [[0 for i in range(n + 2)] for i in range(m + 2)]
    for i in range(m):
        tmp = list(map(int, input().split()))  # 각각 10자리수
        boxes.append([0, 0] + tmp + [0])
    # boxes.append([0 for i in range(n+2)])
    for i in range(2, m + 2):
        for j in range(2, n + 2):  # MxN 10만
            dp[i][j] = max(boxes[i][j] + dp[i][j - 2], dp[i][j - 1])  # 이 값을 선택하느냐 vs 선택하지 않느냐

    ans = [0 for i in range(m + 2)]
    for i in range(2, m + 2):
        ans[i] = max(dp[i][-1] + ans[i - 2], ans[i - 1])

    print(ans[-1])
