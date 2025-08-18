def solution(capacity, routes):
  counts=[0 for i in range(1000)]
  for giftNum, fromNum, toNum in routes:
    for i in range(fromNum, toNum):
      counts[i]+=giftNum
  # print(counts)
  for count in counts:
    if count>capacity:
      return False

  return True

print(solution(9, [[3,2,6],[5,1,4],[1,7,13]])) #True
print(solution(8,[[3,12,16],[8,2,12],[1,14,15]])) #True
print(solution(20,[[5,1,15,],[14,3,18],[3,15,21],[9,14,52]])) #False


'''
블루베리 새가 최대로 들 수있는 선물의 개수가 정수 capacity개
배달 경로가 배열 routes = [[giftNum,from,to], [..], ...] 로 주어짐

***블루베리 새가 모든 경로를 단방향으로 거쳐 배달할 수 있을까요?

예시 1)
capacity=9, rounts=[[3,2,6],[5,1,4],[1,7,13]]이면
새는 한 번에 최대 9개 들 수 있음

'''