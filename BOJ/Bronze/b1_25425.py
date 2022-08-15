import sys
import math

input = sys.stdin.readline

n, m, a, k = map(int, input().split())

# 최대 팀 수
# max 30일 때
if a - k >= n - 1:  # 우리팀뺴고 남은 인원이 n개의 팀 수에 1명씩 들어가있다.
    max = n

else:  #
    max = a - k + 1

# 최소 팀 수
min = math.ceil((a - k) / m) + 1

print(max, min)

