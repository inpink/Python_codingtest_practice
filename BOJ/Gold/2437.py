import sys
input = sys.stdin.readline

n=int(input())
weights=list(map(int,input().split()))
weights.sort() #정렬 꼭 필요
ans = 0 #지금까지 만들 수 있는 숫자의 최댓값

for number in weights:
  if number>ans+1: #새로운 숫자가 지금까지 만들 수 있는 숫자보다 2이상 크면, 1개 이상의 간극이 생기는 것이기에 ans+1이 정답임
    break

  ans+=number


print(ans+1) #정답 = 만들 수 없는 최솟값  = 지금까지 만들 수 있는 숫자의 최댓값 + 1