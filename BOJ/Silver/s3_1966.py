import sys

input = sys.stdin.readline

from collections import deque


def f():
    n, m = map(int, input().split())  # 문서의 개수 n, 몇번째가 궁금한지 m
    rank = list(map(int, input().split()))

    # rank가 클수록 중요도가 높은 것.
    # rank는 여러 개 일 수 있다.

    deq = deque()

    for i in range(n):
        deq.append([rank[i], i])  # rank,몇번째
    # print(deq, rank)

    count = 0
    while True:
        maxx = max(rank)
        # print(count,maxx,deq[0], "deq:",deq )
        if deq[0][0] >= maxx:  # 가장 큰 값이 없으면
            count += 1
            if deq[0][1] == m:  # m이 삭제되면
                break
            deq.popleft()
            rank.remove(maxx)
        else:  # 더 큰 값이 있으면
            deq.rotate(-1)

    # print(deq, rank)
    return count  # m번째 서류가 몇번째로 출력되었는가


n = int(input())  # tese case 수
for i in range(n):
    print(f()) 

