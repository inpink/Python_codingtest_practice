import sys

input = sys.stdin.readline

from collections import deque

# 실버3. 소요시간 20~25분.

l = deque()  # 값이 담기고 빠질 스택
n = int(input())
re = []  # + - 담을 정답 리스트

# 2번
count = 0  # 몇번까지 뽑아 썼는지를 count
for i in range(n):
    a = int(input())

    if a < count:  # count보다 a가 작다면 왼쪽으로
        if a != l[-1]:  # 바로 이전 것이 a가 아니라면 답없음.
            print("NO")
            sys.exit()  # NO가 나오는 경우는 push가 아니라 pop에서만.
        else:
            l.pop()
            re.append('-')

    else:  # count보다 큰 숫자 들어오면, 거기까지 추가(+)해준 뒤 마지막 하나 (-).
        for i in range(count + 1, a + 1):
            re.append('+')
            count += 1
            l.append(i)
        l.pop()
        re.append('-')

    # print(a,count,l,re)

for i in re:
    print(i)
