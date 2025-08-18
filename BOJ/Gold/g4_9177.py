import sys
input=sys.stdin.readline

t=int(input())
for i in range(t):
  word1,word2,mixedCandidate=map(str,input().split())
  word1+=" "
  word2+=" "
  dp1=[-1 for i in range(len(mixedCandidate))]
  dp2=[-1 for i in range(len(mixedCandidate))]

  for j in range(len(mixedCandidate)):
    thisWord=mixedCandidate[j]

    untilMax1=dp1[j-1]
    untilMax2=dp2[j-1]

    if thisWord==word1[untilMax1+1]:
      dp1[j]=untilMax1+1
    else:
      dp1[j]=untilMax1

    if thisWord==word2[untilMax2+1]:
      dp2[j]=untilMax2+1
    else:
      dp2[j]=untilMax2

  # print(dp1,dp2)

  if dp1[-1]==len(word1)-2 and dp2[-1]==len(word2)-2:
    if
    print("Data set %d: yes" % (i+1))
  else:
    print("Data set %d: no" % (i+1))


