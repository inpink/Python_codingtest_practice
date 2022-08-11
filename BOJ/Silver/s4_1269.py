'''
#a-b와 b-a를 따로 구해서 각각 길이를 셈.
#문제는 없지만, 파이썬 set에는 ^라는 대칭차집합을 구하는 더 효율적인 기능이 있다.

import sys
input = sys.stdin.readline

a, b = map(int, input().split())

a_s = set(map(int, input().split()))

b_s = set(map(int, input().split()))

n=a_s-b_s
m=b_s-a_s

lenn=len(n)
lenm=len(m)

print(lenn+lenm)


'''



import sys
input = sys.stdin.readline

a, b = map(int, input().split())

a_s = set(map(int, input().split()))

b_s = set(map(int, input().split()))

print(len(a_s^b_s))
