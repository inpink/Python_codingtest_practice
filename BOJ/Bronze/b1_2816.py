import sys
input = sys.stdin.readline

n= int(input())
chanels = []
answer = []
kbs1_index = 0
kbs2_index = 0
cur_index = 1
for i in range(n):
  s= input().rstrip()
  chanels.append(s)
  if s == "KBS1":
    kbs1_index = i+1
  elif s == "KBS2":
    kbs2_index = i+1

#kbs1까지 이동
kbs1_toward_move_count = 0
while True:
  if cur_index == kbs1_index:
    break
  answer.append(1)
  cur_index+=1
  kbs1_toward_move_count+=1

for i in range(kbs1_toward_move_count):
  answer.append(4)
  cur_index-=1

# kbs1_index가 kbs2_index보다 밑에 있으면
if kbs2_index < kbs1_index:
  kbs2_index +=1

# kbs2까지 이동
kbs2_toward_move_count = 0
while True:
  if cur_index == kbs2_index:
    break
  answer.append(1)
  cur_index+=1
  kbs2_toward_move_count+=1

for i in range(kbs2_toward_move_count-1):
  answer.append(4)
  cur_index-=1

print(''.join(map(str, answer)))









'''
상근이는 채널 리스트를 조절해 KBS1을 첫 번째로, KBS2를 두 번째로 만들려고 한다.

네 가지 버튼
화살표를 한 칸 아래로 내린다. (채널 i에서 i+1로)
화살표를 위로 한 칸 올린다. (채널 i에서 i-1로)
현재 선택한 채널을 한 칸 아래로 내린다. (채널 i와 i+1의 위치를 바꾼다. 화살표는 i+1을 가리키고 있는다)
현재 선택한 채널을 위로 한 칸 올린다. (채널 i와 i-1의 위치를 바꾼다. 화살표는 i-1을 가리키고 있다)

화살표가 채널 리스트의 범위를 넘어간다면, 그 명령은 무시한다

*, KBS1를 첫 번째로, KBS2를 두 번째로 순서를 바꾸는 방법 - 버튼 순서대로 출력할것*
*방법의 길이는 500보다 작아야 한다.*
*두 채널을 제외한 나머지 채널의 순서는 상관없다.*

n은 채널 수(2~100)
채널 목록 n개

채널의 이름은 최대 10글자
 알파벳 대문자와 숫자로만 이루어져 있다
 이미 KBS1이 첫 번째에, KBS2가 두 번째에 있는 입력은 주어지지 않는다.
 모든 채널의 이름은 서로 다르다
 항상 KBS1과 KBS2를 포함하고 있다. 
'''
