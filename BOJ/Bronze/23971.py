import sys
input = sys.stdin.readline
import math

h,w,n,m=map(int, input().split())

print(math.ceil(w/(1+m)) * math.ceil(h/(1+n)))

'''
w은 열, h는 행
세로로 n칸 또는 가로로 m칸 이상 비우고 앉아야 한다
최대 몇명 강의실에 수용 가능?

열에 대해서, 한 열에는 ceil(w/(1+m)) 명이 앉을 수 있다
행에 대해서, 한 행에는 ceil(h/(1+n)) 명이 앉을 수 있다

'''