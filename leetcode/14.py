def longestCommonPrefix(self, strs):
  minLen = 200
  for s in strs:
    if len(s)<minLen:
      minLen=len(s)
  ans=""
  for i in range(minLen):
    thisS=strs[0][i]
    for j in range(len(strs)):
      if thisS!=strs[j][i]:
        return ans
    ans+=thisS
  return ans


#그냥 너무 쉬운 단순 구현 문제