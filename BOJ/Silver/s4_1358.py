import sys

input = sys.stdin.readline

w, h, x, y, p = map(int, input().split())
r = h // 2  # ★ h는 짝수이다!
count = 0
for i in range(p):
    a, b = map(int, input().split())

    # 사각형 검사 (경계선 포함)
    if x <= a <= x + w and y <= b <= y + h:
        count += 1
        # print("사각형",a,b)

    # 사각형에 없는 경우에만 아래를 검사하게 된다.
    # 왼쪽 원
    elif x - r <= a <= x and y <= b <= y + h:  # 최소한으로 가능한 범위에만 원 검색한다.
        # print("*",a,b,x,y)
        if (x - a) ** 2 + ((y + r) - b) ** 2 <= r ** 2:  # 반 원 안에 있다면 #★ x, y가 아니 x, y+r이다! 문제 그림을 잘 보자.
            count += 1
            # print("왼원",a,b)

    # 오른 쪽 원
    elif x + w <= a <= x + w + r and y <= b <= y + h:
        if ((x + w) - a) ** 2 + ((y + r) - b) ** 2 <= r ** 2:
            count += 1
            # print("오른원",a,b)

print(count)
