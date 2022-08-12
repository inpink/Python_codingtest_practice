import sys

input = sys.stdin.readline

from collections import deque

q = deque()

n = int(input())
for i in range(n):
    q.appendleft(i + 1)
# print(q)
while True:
    if len(q) == 1:
        print(q[0])
        break
    q.pop()
    q.rotate(1)
    # print(q)

