import sys

input = sys.stdin.readline


def c(a, b):  # bCa
    if a == b:  # 2c2/ (2c0은 들어오지 않는다고 한다)
        return 1

    if b - a < a:  # 5c3, 6c4같은 것
        a = b - a
    j = 1
    k = 1
    for i in range(a):  # 5c2
        j *= (b - i)
        k *= (i + 1)
    return j // k


t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    print(c(a, b))
