import sys
import time

input = sys.stdin.readline

max = 2020202 #?
n = int(input())
A = list(map(int, input().split()))

# 1999993, 2000003은 소수이다. 19..는 1~19..까지로 커버가 되지만
# 200..3은 200..3이라는 숫자가 있어야만 생성된다. 따라서 나올 수 있는 최대 mex는 2000003이다.
# 참고로 2000001이랑 2000002는 소인수분해가 돼서 충분히 만들어질 수 있다. 2000003을 넘는 숫자도 충분히 만들어지지만,
# 어쨌든 최대로 이어지는 것은 2000002까지니까 최대 mex는 2000003이다.
# set를 이용했더니 시간초과가 나서, 자리를 이용하는 배열을 이용함

B = [0] * max  # 입력된 A의 위치 찍어줌
C = [0] * max  # i*j 위치 찍어줌

for i in A:
    B[i] = 1  # 굳이 개수까지는 셀 필요가 없다. 1로 바꿔준다.

# B완성
# A=[0,1,2]라면 B=[1,1,1,0,0,0...]

if B[0] == 0:  # B에 0이 없다면, 무조건 0나옴
    print(0)
    sys.exit(0)

elif B[1] == 0:  # B에 0이 있는데 1이 없다면, 무조건 1나옴
    print(1)
    sys.exit(0)

C[0] = 1
C[1] = 1

for i in range(1, max):  # 0을 빼고 다 곱해준다. #i=1~2000002
    if B[i] == 1:
        for j in range(i, max // i):  # j=i~2000002 #?
            if i * j >= max:
                break
            elif B[j] == 1:
                C[i * j] = 1

for i in range(max):
    if C[i] == 0:
        print(i)
        break
