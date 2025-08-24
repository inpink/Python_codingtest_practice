import sys
input = sys.stdin.readline

import bisect

t=int(input())
for i in range(t):
  n,m=map(int,input().split())
  a_list=list(map(int,input().split()))
  b_list=list(map(int,input().split()))

  a_list.sort()
  b_list.sort()

  # print(a_list)
  # print(b_list)

  ans=0
  for a in a_list:
    pos = bisect.bisect_left(b_list, a)
    ans+=pos
    # print(pos)

  print(ans)