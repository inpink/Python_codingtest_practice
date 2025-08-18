import sys
input = sys.stdin.readline


def backtracking(candidate, candiLen):
  # print(candidate, candiLen)
  if candiLen == len(s):
    # print("dd")
    if "".join(map(str, candidate)) == s:
      for i in range(1, max(visited)+1):
        if i not in visited:
          return False
      print(*candidate)
      exit(0)

    return False

  #숫자 하나만 쓰거나, 숫자 2개 쓰거나 둘 중에 하나임 (매번의 백트래킹 함수마다 선택지는 2개밖에 없음)
  if candiLen <len(s):
    addNum = int(s[candiLen])
    if int(addNum) > 0 and addNum not in visited:
      candidate.append(addNum)
      visited.add(addNum)
      if backtracking(candidate, candiLen+1)==False:
        candidate.pop()
        visited.remove(addNum)

  if candiLen+1 <len(s):
    addNum = int(s[candiLen:candiLen+2])
    if int(addNum) >=10 and addNum not in visited:
      candidate.append(addNum)
      visited.add(addNum)
      if backtracking(candidate, candiLen+2)==False:
        candidate.pop()
        visited.remove(addNum)

  return False



s = input().strip()
visited=set()
backtracking([],0)


'''
brute force할 경우 => 50! (시간초과)
칸 100개 중, 같은 빈칸 50개 배치 중복 조합 => 100! / 50! * 50! (시간초과)
백트래킹해야함
'''