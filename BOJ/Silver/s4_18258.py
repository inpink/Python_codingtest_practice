import sys

input = sys.stdin.readline

from collections import deque

q = deque()

n = int(input())

for i in range(n):  # n번 반복
    n = list(input().split())
    if len(n) == 2:  # push인 경우
        q.append(n[1])

    elif n[0] == 'pop':
        if len(q) == 0:
            print(-1)
        else:
            help = q.popleft()
            print(help)

    elif n[0] == 'size':
        print(len(q))

    elif n[0] == 'empty':
        if len(q) == 0:
            print(1)
        else:
            print(0)

    elif n[0] == 'front':
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])

    elif n[0] == 'back':
        if len(q) == 0:
            print(-1)
        else:
            print(q[-1])