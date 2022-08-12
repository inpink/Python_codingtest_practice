import sys

input = sys.stdin.readline

from collections import deque

while True:
    s = deque()  # 스택은 매번 초기화
    ist = ''
    # 각 줄 입력받기
    a = input().rstrip()
    if a == '.':
        break
    for i in a:
        if i == '(':
            s.append('(')
        elif i == '[':
            s.append('[')

        elif i == ')':
            if len(s) == 0:  # (가 들어 있지 않은 경우
                ist = "no"
                break
            elif s[-1] != '(':  # (가 아닌 게 있다면
                ist = "no"
                break
            else:
                s.pop()

        elif i == ']':
            if len(s) == 0:  # [가 들어 있지 않은 경우
                ist = "no"
                break
            elif s[-1] != '[':  # [가 아닌 게 있다면
                ist = "no"
                break
            else:
                s.pop()

    # 괄호 한 줄 검사다 끝났을 때
    if ist == "no":
        print("no")
    else:
        if len(s) != 0:
            print("no")
        else:
            print("yes")

