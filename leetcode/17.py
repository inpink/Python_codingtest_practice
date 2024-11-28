from itertools import product

class Solution:
  def letterCombinations(self, digits: str):
    if not digits:
      return []

    digit_to_char = {
      '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
      '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }

    char_lists = [digit_to_char[d] for d in digits]

    #product를 통해 모든 조합 생성
    return ["".join(chars) for chars in product(*char_lists)]

'''
쉬운 조합 문제 그냥 itertools.product 사용하면 됨

⭐️ product(*char_lists) = product("abc", "def") 
=
('a', 'd')
('a', 'e')
('a', 'f')
('b', 'd')
('b', 'e')
('b', 'f')
('c', 'd')
...

'''