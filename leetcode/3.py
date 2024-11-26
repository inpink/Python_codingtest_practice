from collections import deque

def lengthOfLongestSubstring(s):
  q = deque()
  leng = len(s)
  maxLen=0
  for i in range(leng):
    c = s[i]
    if c not in q:
      q.append(c)
      maxLen=max(maxLen, len(q))
    else:
        while True:
          left = q.popleft()
          if left == c:
            q.append(c)
            break

    print(q)
  return maxLen


print(lengthOfLongestSubstring("aabaab!bb"))

'''

⭐️⭐️⭐️ 입력값의 길이가 "가능한 가장 최소"인 테스트케이스 꼭 만들기!!! 예외 발생하기 쉬움!!!!!!
⭐️⭐️ 시간복잡도 내에 가능하다면 더 절약하려고 하지 말고 일단 푸는게 먼저다.

https://leetcode.com/problems/add-two-numbers/description/

주어진 문자열 s에서 반복되지 않는 문자가 포함된 가장 긴 부분 문자열의 길이를 찾아야 함


제약 조건)
0 <= s.length <= 5 * 10^4
s는 영어 소문자, 대문자, 숫자, 기호, 공백으로 이루어져 있음

ex1)
s = "abcabcbb"
정답 3 (abc)

ex2)
s = "bbbbb"
정답 1 (b)

ex3)
s = "pwwkew"
정답 3 (wke)




'''