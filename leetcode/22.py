def generateParenthesis(n):
  def backtrack(s, open_count, close_count):
    #올바른 괄호 조합이 완성된 경우
    if len(s) == 2 * n:
      result.append(s)
      return

    #여는 괄호를 추가할 수 있는 경우
    if open_count < n:
      backtrack(s + "(", open_count + 1, close_count)

    #닫는 괄호를 추가할 수 있는 경우
    if close_count < open_count:
      backtrack(s + ")", open_count, close_count + 1)

  result = []
  backtrack("", 0, 0)
  return result


'''
⭐️ 백트래킹
(모든 조합을 구해도 16!/8!*8! = 12870개로 브루트포스 가능하긴함)

⭐⭐⭐️ 닫는 괄호는 여는 괄호보다 더 작은 개수일 때 추가하면 괄호 규칙 안 깨짐!!!!

⭐️ 이 문제의 개수는 "카탈란 수"라는 수열을 따름 
(2n)! / (n+1)!n!로, n=8일 때 1430개



'''