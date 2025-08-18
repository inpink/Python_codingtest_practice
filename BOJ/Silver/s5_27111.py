import sys

input = sys.stdin.readline

n = int(input())

s = set()
ans = 0
for i in range(n):
  a,b = map(int, input().split())
  if b==1:
    if a in s:
      ans+=1
    else:
      s.add(a)
  elif b==0:
    if a in s:
      s.remove(a)
    else:
      ans+=1

if len(s)!=0:
  ans+=len(s)

print(ans)