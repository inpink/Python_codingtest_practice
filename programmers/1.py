from collections import deque


def solution(tossConvenienceStoreMap, entrancePoint):  # 지도, 출발지점
  # 찾을 때까지 위, 아래로 움직이기
  def bfs(startX, startY):
    dir = [[(-1, 0), (1, 0)], [(0, -1), (0, 1)]]  # 상, 하 / 좌, 우
    # cur_score = tossConvenienceStoreMap[startX][startY]

    visited = [[False for i in range(n)] for i in range(n)]
    queue = deque([])
    queue.append([startX, startY])
    visited[startX][startY]=True
    turn=0 # 상, 하 먼저

    while True:
      # print(queue)
      if len(queue) == 0:
        break

      cur_x, cur_y = queue.popleft()
      cur_score = tossConvenienceStoreMap[cur_x][cur_y]
      for dir_x, dir_y in dir[turn]:
        next_x, next_y = cur_x + dir_x*cur_score, cur_y + dir_y*cur_score

        if (next_x<0 or next_x>=n or next_y<0 or next_y>=n):
          continue

        if visited[next_x][next_y]==True:
          continue

        if tossConvenienceStoreMap[next_x][next_y]==0 or tossConvenienceStoreMap[next_x][next_y]==8:
          continue

        if tossConvenienceStoreMap[next_x][next_y] == 7:
          return True

        queue.append([next_x,next_y])
        visited[next_x][next_y]=True
      turn=(turn+1)%2

    return False

  startX, startY = entrancePoint
  startScore = tossConvenienceStoreMap[startX][startY]
  n = len(tossConvenienceStoreMap)
  # 시작점에서 이동 불가능
  if startScore == 0 or startScore == 8:
    return False

  # 시작점에서 왼, 오로 움직이기
  leftStartX, leftStartY = startX, startY - startScore
  rightStartX, rightStartY = startX, startY + startScore

  detection = []
  if n > leftStartY >= 0:
    detection.append(bfs(leftStartX, leftStartY))

  if 0 <= rightStartY < n:
    detection.append(bfs(rightStartX, rightStartY))

  if True in detection:
    return True
  else:
    return False


print(solution([[1, 2, 1], [8, 2, 0], [1, 7, 2]], [0, 0]))
print(solution([[1,2,3,2,1],[4,2,0,7,1],[1,3,2,8,1],[2,0,1,1,1],[8,2,1,2,1]],[4,3]))
print(solution([[1,2,3,2,1],[4,2,0,7,2],[1,3,2,8,1],[2,0,1,1,1],[8,2,8,1,1]],[0,0]))
'''
7은 닭가슴살

0은 액상과당 음료수
8은 초콜릿

음료수, 초콜릿 피해서 닭가슴살 찾으러 가기

출발지점 : 왼, 오 이동 가능
이후: 위, 아래 가능 => 왼, 오 가능 (반복)
이동 방향으로 현재 위치의 숫자만큼 이동

'''
