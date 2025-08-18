import sys
input = sys.stdin.readline


n= int(input())
aList = list(map(int, input().split()))

beforeA = dict()
for i in range(n):
  if aList[i] -1 in beforeA:
    beforeLen = beforeA[aList[i]-1]
    beforeA[aList[i]] = beforeLen+1
  else:
    beforeA[aList[i]] = 1

  # print(beforeA)

if len(beforeA) == 0:
  print(0)
  exit(0)
print(max(beforeA.values()))

'''
군계일 수열 = 각 항이 서로 연속적인 수열. ai = a1 + (i-1) 
길이가 N인 수(1~10만)
가장 긴 군일ㄹ학 수열을 구해야 함. 길이 출력하기

ai는 1~100만

1 5 2

1이 첫번쨰일 경우
5가 첫번째일 경우, 두번쨰일 경우
2가 첫번째일 경우, 두번째일 경우, 세번째일 경우
모든 경우 다 구하면 시간초과 거의 n^2

저 수식 자체가, 시작점은 뭐인지 알 수 없지만 1씩 증가하는 숫자들이란 것임

8
1 2 5 1 2 6 7 8 
=> 정답은 4 (5,6,7,8)

'''

