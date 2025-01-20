import sys
input = sys.stdin.readline


n = int(input())
l = list(map(int, input().split()))


d = dict()
ans=100_000+1

for i in range(n):
  if l[i] in d:
    ans= min(ans, abs(d[l[i]] - i))
  else:
    d[l[i]] = i

if ans==100_000+1:
  ans=n
print(ans)