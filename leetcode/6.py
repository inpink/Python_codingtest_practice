import math

class Solution:
  def convert(self, s: str, numRows: int) -> str:
    if numRows==1:
      return s

    sLen = len(s)
    pairElementLen = numRows * 2 - 2
    pairLenCeil = math.ceil(sLen / pairElementLen)
    colLen = (numRows - 1) * pairLenCeil

    matrix = [['' for i in range(colLen)] for i in range(numRows)]

    def findAns(matrix):
      #for i in matrix:
      #print(i)
      ans = ""
      for a in range(numRows):
        for b in range(colLen):
          ans+=matrix[a][b]

      return ans

    #one pair
    count=0
    round=0
    while True:
      if count==sLen:
        break

      #one pair
      for i in range(numRows): #세로 한 줄 먼저 쓰고
        matrix[i][(numRows-1)*round] = s[count]
        count+=1
        if count==sLen:
          return findAns(matrix)

      for i in range(1,numRows-2+1):
        matrix[numRows-1-i][(numRows-1)*round +i] = s[count]
        count+=1
        if count==sLen:
          return findAns(matrix)
      round+=1

    return findAns(matrix)


'''
그냥 matrix 구현 잘 하면 되는 문제
'''