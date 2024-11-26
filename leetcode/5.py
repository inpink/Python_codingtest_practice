def longestPalindrome(self, s):
  if not s or len(s) == 0:
    return ""

  start, end = 0, 0

  def expand_around_center(left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
      left -= 1
      right += 1
    return right - left - 1

  for i in range(len(s)):
    len1 = expand_around_center(i, i)
    len2 = expand_around_center(i, i + 1)
    max_len = max(len1, len2)
    if max_len > end - start:
      start = i - (max_len - 1) // 2
      end = i + max_len // 2

  return s[start:end + 1]


'''

문자열 내에서 가장 긴 팰린드롬 찾기
1<n<1000


"Expand Around Center" 방법 사용
- 팰린드롬의 중심을 찾아 확장하는 방법

가장 긴 팰린드롬 찾는 알고리즘은 여러 개 있음 그 중에 이 방법 선택함

'''