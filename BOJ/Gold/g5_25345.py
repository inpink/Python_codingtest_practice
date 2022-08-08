import sys

input = sys.stdin.readline


def c(n, k):
    if k == 0 or n == k:  # 5c5나 5c0같은 경우 계산안하고 1
        return 1
    elif k == 1 or (n - k) == 1:  # 5c1나 5c4 같은 경우 계산안하고 5
        return n
    else:
        if (n - k) < k:  # 5c3같은 경우 5c2로 하면 더 효율적이다.
            k = n - k
        a = 1  # 분자
        b = 1  # 분모
        for i in range(k):
            a *= (n - i)
            b *= (i + 1)
        return (a // b)  # nCk 값을 return


def games(k):
    r = 0
    for i in range(k):  # k번 할거임
        r += c((k - 1), i)
        # print(r)
    return r


N, K = map(int, input().split())
A = list(map(int, input().split()))

# 경우의 수 문제. k개의 겹치지 않는 케이스를 뽑아서, 가장 큰 것을 어디에 세우느냐

ans = c(N, K) * games(K)

print(ans % (10 ** 9 + 7))

