import sys
input = sys.stdin.readline

n, a, d = map(int, input().split())
melody = list(map(int, input().split()))


beforeMelody = dict()

for i in range(n):
  if (melody[i] - a) % d == 0: # 의미있는 숫자
    if melody[i] == a:
      beforeMelody[melody[i]] = 1
    elif (melody[i] - d) in beforeMelody:
      beforeMelody[melody[i]] = (melody[i] - a) // d + 1

# print(beforeMelody)
if len(beforeMelody) == 0:
  print(0)
  exit(0)
print(max(beforeMelody.values()))

'''
n은 입력 숫자 개수
a는 시작 숫자 (10^7 이하)
d는 공차 (10^7 이하)

의미있는 숫자 x = d * i + a
'''