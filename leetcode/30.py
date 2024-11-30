class Solution:
  def findSubstring(self, s: str, words: List[str]) -> List[int]:
    if not s or not words:
      return []

    ans=[]
    wordLen = len(words[0])
    wordsLen= len(words)
    sLen = len(s)

    word_map = {}
    for word in words:
      word_map[word] = word_map.get(word, 0) + 1

    for i in range(sLen - wordLen * wordsLen + 1):
      word = s[i:i+wordLen]
      newWords= dict()

      count=0

      for j in range(wordsLen):
        nextIndex = i+ wordLen * j

        if nextIndex >= sLen:
          break
        nextWord= s[nextIndex:nextIndex+wordLen]
        #print(nextIndex, nextWord)
        if nextWord in word_map:
          newWords[nextWord] = newWords.get(nextWord,0)+1
        else:
          break

        if newWords[nextWord] > word_map[nextWord]:
          break

        count+=1

      #print(i,newWords,count)
      if count==wordsLen:
        ans.append(i)

    return ans



'''

⭐ 변수 이름 절대 비슷하게 짓지 말기

brute force 불가 (words의 모든 조합 계산하면 200억 넘음)
가지치기 안하면 시간초과 빡세게 잡던 문제
=> ⭐ 정답 string의 최소 길이는 총 wordLen(30) * wordsLen(5000)임! ⭐s를 모두 탐색하면 시간초과 떴음⭐ s- wordLen * wordsLen+1만 탐색해야함  ⭐

- 모든 가능한 시작점 s[i] (N-@) x 모든 가능한 단어(5000개) => (hashMap과 set 이용하면 시간복잡도 (N-@)*M에 가능)
  - 한 번이라도 어긋나는 경우 더 볼 필요 없음. 불가능한 경우 가지치기 하기 

'''