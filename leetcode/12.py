def intToRoman(self, num: int) -> str:
  ans=""
  values=[1000,500,100,50,10,5,1]
  symbols=["M","D","C","L","X","V","I"]
  s=str(num)
  sLen=len(s)
  for i in range(sLen):
    thisStrNum = int(s[i]) * 10 ** (sLen-i-1)
    thisNum = int(thisStrNum)
    print(thisNum)

    for j in range(len(values)):
      if thisNum>=values[j]:
        if s[i] in "123":
          ans+= symbols[j] * int(s[i])
          break
        elif s[i]== "4":
          ans+=(symbols[j]+symbols[j-1])
          break
        elif s[i]== "9":
          ans+=(symbols[j+1]+symbols[j-1])
          break
        elif s[i] in "50":
          ans+=  symbols[j]
          break
        elif s[i] in "678":
          ans+= (symbols[j]+ symbols[j+1] * (int(s[i])-5))
          break

  return ans


  '''
  
  주어진 규칙대로 분기 만들어서 잘 구현하면 됨
  1은 I
  2는 II
  3은 III
  4는 IV
  5는 V
  6은 VI
  7은 VII
  8은 VIII
  9는 IX
  10은 X
  '''


'''
다른 풀이법
로마표기법은 미리 4, 9. 40, 90만들어놓고 나누기 이용하면 됨!
출처 https://leetcode.com/problems/integer-to-roman/solutions/6034491/creating-mappings-bonus-coding/
 def intToRoman(self, num: int) -> str:
        value_symbols = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'),
            (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]
        
        res = []

        for value, symbol in value_symbols:
            if num == 0:
                break
            count = num // value
            res.append(symbol * count)
            num -= count * value

        return ''.join(res)             
'''