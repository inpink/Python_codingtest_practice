import sys
input = sys.stdin.readline

n,k,d = map(int,input().split())
rules=[]
for i in range(k):
  a,b,c = map(int,input().split())
  rules.append([a,b,c])

# print(rules)
ans=0
start=1
end=n
while True:
  if start>end:
    break

  mid=(start+end)//2

  total=0
  for a,b,c in rules:
    if a>mid:
      continue

    if b<mid:
      total+=(b-a)//c+1
    else:
      total+=(mid-a)//c+1

    # print(a,"(a) ",b,"(b) ", c, "(c) ", mid, "(mid) ", total, "(total) ")
    # print()

  if total>=d:
    ans=mid
  '''위에서 total==d뿐만아니라 total>=d가 돼야하는이유
  n=5, k=3, d=2
  규칙:
  1 1 1   # 상자 1에 1개
  3 3 1   # 상자 3에 1개
  3 3 1   # 상자 3에 1개  <- 여기서 겹침!
  
  누적(상자별):
  1: 1
  2: 1
  3: 3   <- 2개가 한꺼번에 늘어 점프 (1 → 3)
  4: 3
  5: 3
  
  정답 상자 = 3 (처음으로 누적 ≥ 2)
  하지만 누적이 정확히 2가 되는 상자는 없음.
  '''

  if total<d:
    start = mid + 1
  else:
    end = mid - 1


print(ans)
'''
이분탐색. ***찾아야할 값을 mid라고 가정한다***
모든 k를 돌면서 mid까지 몇개가 들어가는지 확인한다 => 하나하나 다 세면 시건초과다. 등차수열이므로 수열식 이용해서 개수 센다!!

mid 값을 바로 출력하거나 upper bound 값을 출력하면 틀립니다. 아래 예시에서 2번 상자부터 10번 상자 모두 총 도토리가 담긴 수는 1 이기 때문입니다. 
10 1 1
2 2 1
// ans 2 (출처: https://www.acmicpc.net/board/view/160233)


'''