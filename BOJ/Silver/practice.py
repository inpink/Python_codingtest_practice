import sys
input = sys.stdin.readline

from collections import deque

s=input().rstrip()
t=input().rstrip()

q=deque([deque(list(t))])
# print(q)
ans=0

while True:
  if len(q)==0:
    break
  thisTransT=q.popleft()
  secondThisTransT=deque(list(thisTransT))
  if ''.join(thisTransT)==s:
    ans=1
    break
  if len(thisTransT)<len(s):
    break
  # removeB
  if thisTransT[0]=='B':
    thisTransT.popleft()
    thisTransT.reverse()
    q.append(deque(list(thisTransT)))
  if secondThisTransT[-1] == 'A': #removeA
    secondThisTransT.pop()
    q.append(deque(list(secondThisTransT)))
  # print(q)
print(ans)
