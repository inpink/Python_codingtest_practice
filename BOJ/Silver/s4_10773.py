import sys
input = sys.stdin.readline

from collections import deque

#정수가 "0"일 경우에 지울 수 있는 수가 있음을 보장할 수 있다.
k=int(input())
s=deque()

for i in range(k):
    a=int(input())
    if a==0:
        s.pop()
    else:
        s.append(a)

print(sum(s))
