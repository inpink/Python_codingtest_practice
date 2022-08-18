import sys

input = sys.stdin.readline

n = int(input())

dp = [0, 0, 1, 1, 2, 3, 2, 3, 3, 2, 3, 4]

if n <= 11:
    print(dp[n])
else:
    i = 12
    while True:
        if len(dp) == n + 1:
            print(dp[-1])
            break

        if i % 6 == 0:
            dp.append(min(dp[i // 3] + 1, dp[i // 2] + 1))
        elif i % 2 == 0:
            dp.append(min(dp[i // 2] + 1, dp[i - 1] + 1))
        elif i % 3 == 0:
            dp.append(min(dp[i // 3] + 1, dp[i - 1] + 1))
        else:
            dp.append(dp[i - 1] + 1)

        i += 1
