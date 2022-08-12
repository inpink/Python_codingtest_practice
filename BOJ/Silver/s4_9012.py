import sys

input = sys.stdin.readline

from collections import deque

n = int(input())
for i in range(n):
    q = deque()  # 매번 초기화 해줘야 한다.
    a = input().rstrip()
    ist = ''

    for i in range(len(a)):
        if a[i] == '(':
            q.append('(')
        else:  # ')'일 경우
            if len(q) == 0:  # (가 들어 있지 않은 경우
                ist = "NO"
                break
            else:  # (가 1개 이상 있는 경우
                q.pop()  # ( 한개 제거

    # 괄호 한 줄 검사다 끝났을 때
    if ist == "NO":  # )가 더 많은 경우 : 그냥 NO 출력
        print("NO")
    else:  # 그렇지 않은 경우 중, len이 0이면 딱 개수가 맞는거라 YES고 개수가 1개 이상이라면 (가 더 많은거니 NO
        if len(q) != 0:
            print("NO")
        else:
            print("YES")
    # print(q)
