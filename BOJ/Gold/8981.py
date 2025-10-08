#역시뮬레이션 문제

N = int(input().strip())
Y = list(map(int, input().split()))

X = [0] * N
used = [False] * N
from_idx = 0

for y in Y:
  # 아직 채워지지 않은 자리 찾기
  while True:
    if used[from_idx]==False: #이미 채워져있으면
      break
    from_idx = (from_idx + 1) % N #from+1번째를 쓰기로 함

  X[from_idx] = y
  used[from_idx] = True

  #X에 찍어줬으니 다음 from도 찾아야지
  from_idx = (from_idx + y) % N

  # print(X) #디버깅용

print(N)
print(" ".join(map(str, X)))
