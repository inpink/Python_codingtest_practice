import sys
input = sys.stdin.readline

n=int(input())
k=int(input())

# print(square)

# n=1,2일때예외확인하기
if n==1:
  print(1)
  exit()

start=1
end=n**2
ans=0
while True:
  # print(start,end)
  if start>end: # ****** 이 이분탐색이 끝나서 얻는 값 x*(= “count(≤x) ≥ k가 처음 성립하는 최소 x”)는 반드시 배열 B에 실제로 존재하는 값이에요. 간단한 논리로 증명해봄.
    """
    F(x) = B에서 x 이하인 원소 개수(중복 포함)라고 하자.
	•	F(x)는 계단 모양 함수예요. 배열에 있는 값에서만 “툭” 하고 올라가고, 그 사이 값에서는 평평(증가 없음) 해요.
	•	우리는 F(x) ≥ k가 처음 되는 최소 x = x*를 찾고 있어요.
	•	만약 x*이 배열에 없는 값이라면, 그 지점은 계단이 안 올라가는 평평한 구간이므로
F(x* - 1) = F(x*)가 되어야 해요.
	•	그런데 “처음으로 ≥ k가 되는 최소 x”라는 정의상 **F(x* - 1) < k이고 F(x*) ≥ k**여야 하잖아요?
평평하면 이게 성립할 수 없죠. 모순!
	•	따라서 x*은 반드시 계단이 딱 올라가는 지점, 즉 배열에 실제 존재하는 값입니다."""
    break
  mid=(start+end)//2

  smaller_numbers=0
  for i in range(1,n+1):
    smaller_numbers+=(min(mid//i,n)) #mid보다 작거나 같은 숫자 개수
  # print("sm",smaller_numbers, mid,"(mid)")


  # if smaller_numbers==k: #**** mid보다 작거나 같은 숫자 개수를 발견했다고 멈추면 안됨!!!! 이유는, n=5, k=24, small=24, mid=22가 있다고 해보자. 22는 실제로 배열에 등장하는 숫자가 아니다.
  #   ans=mid
  #   break
  if smaller_numbers>=k:
    ans=mid # ******** 조건에 만족하는 mid만 ans후보임. mid=2일 때 smaller 3개이고, mid=1일 때 smaller 1개이고, k=2를 찾으면, 2가 2번 중복된다는거고 정답은 mid=2다****
    end=mid-1
  else:
    start=mid+1

print(ans)


'''


NXN 배열 A
A[i][j]=ixj

일차원 배열 B에 넣으면 B의 크기는 NXN
B를 오름차순 정렬했을 때,B[k]?

A,B의 인덱스는 1부터 시작
N: 1~10^5
k: 1~min(10^9, N^2)


--
숫자 10^10개 (100억개) => 다 정렬하면 시간초과, 다 구해도 메모리 초과
배열에 있을 수 있는 숫자 최소값 1, 최대값 100억
k도 최대값 10^9(10억)이라 O(k)도 안됨

----
**** a라는 숫자보다 작은 숫자가 몇 개 있는지 세는게 핵심

맵에서 a라는 숫자보다 작거나 같은 숫자는, 1~n에 대해서 min(a//i,n)개임
이분탐색 이용해서 1~100억 중에 a를 찾는 게 목표

print("sm",smaller_numbers, start,end, mid)

3
7
sm 6 1 9 5
sm 8 6 9 7
sm 8 6 6 6
6
**** => 5보다 작거나 같은건 6개다, 7보다 작거나 같은건 8개다, 6보다 작거나 같은건 8개다
6~8사이에 있는 k=7은 6이 최소범위****

***stop 조건이 k값과 일치하는지가 아니라 start,end를 비교하는 이유?원리?
mid라는 숫자가 맵 목록에서 여러 번 등장하니까.  
start>=end break로, 

*** mid==k,순서이다!
'''

