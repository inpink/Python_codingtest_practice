import sys
input = sys.stdin.readline

n,q = map(int, input().split())
numbers = list(map(int, input().split()))

numbers.sort()
numbers = [0] + numbers

# print(numbers)

for i in range(1,n+1):
  numbers[i] += numbers[i-1]

# print(numbers)

for i in range(q):
  l,r = map(int, input().split())
  print(numbers[r]-numbers[l-1])



'''
비내림차순 정렬 후
l~r까지의 합을 구하는 문제

수열 길이 30만
질문 개수 30만
매번 구하면 시간 초과
-> 미리 합을 구해놓고 출력
'''