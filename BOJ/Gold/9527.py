import sys
input = sys.stdin.readline


def ones_upto(n: int) -> int:
  """0..n 에서 '1' 비트 총합 (n<0이면 0)"""
  if n < 0:
    return 0
  total = 0
  # 10^16 < 2^54 이므로 0..56이면 충분

  for i in range(56): #i번째 비트에 1 몇개 있는지 세는거임
    block = 1 << (i + 1)   # 주기 길이, 2 ** (i + 1)도 됨
    half  = 1 << i         # 주기의 절반(해당 비트가 1인 구간 길이), 2**i도 됨, block/2도됨
    full_cycles = (n + 1) // block # (n+1)개 숫자 중에서 주기(block) 단위로 몇 번 완전히 반복되는지
    rem = (n + 1) % block  # 마지막에 남는 부분 (주기가 완전히 안 찬 나머지)
    total += full_cycles * half # 완전한 주기 부분에서는 각 주기마다 half개씩 1이 등장

    # 나머지(rem) 부분에서 추가로 생기는 1들 계산
    # rem이 half보다 크면, 그 초과 부분만큼 1이 더 있음 (주기는 0부터 세고, 0011 이런식으로 처음 절반만 0이기 때문!)

    if rem > half:
      total += (rem - half)
    # print(block, half, full_cycles,rem)
  return total


A, B = map(int, input().split())
print(ones_upto(B) - ones_upto(A - 1))

'''
	•	0번째 비트(맨 오른쪽)는 1,0,1,0… 이렇게 1,0이 번갈아 나타남 → 주기 2
	•	1번째 비트는 0011, 0011… → 주기 4, 절반이 1
	•	2번째 비트는 00001111… → 주기 8, 절반이 1
⭐이 주기는 0부터 세는 거다. ⭐
0000
0001
0010
0011
0100
0110
0111
1000
...

즉,
⭐i번째 비트는 주기 = 2^(i+1)⭐, 그 안에     ⭐️1인 구간이 2^i개  ⭐️ 존재.


누적합
10^16개 전부 계산하면 시간초과이므로
위와 같은 알고리즘 쓰고,
b까지의 개수 - a까지의 개수
로 정답 구함 


'''