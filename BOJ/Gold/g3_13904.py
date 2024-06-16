import sys
input=sys.stdin.readline
import heapq

n=int(input())
homeworks={}

for i in range(n):
    d,w=map(int, input().split()) #과제 마감일까지 남은 일수, 과제 점수

    if d in homeworks:
        heapq.heappush(homeworks[d],-w)
    else:
        homeworks[d]=[-w]
#print(homeworks)

ans=0
used=[] #힙
for day in range(1,1000+1):
    if day not in homeworks:
        continue

    #각 day에서 가장 큰 값은 일단 무조건 사용
    heapq.heappush(used,-1 * heapq.heappop(homeworks[day]))

    while True:
        if len(homeworks[day])==0:
            break

        cost=-1 * heapq.heappop(homeworks[day])
        #print(cost)
        if len(used)<day: # * 빈 날짜가 있다면 넣기만 하기!!  반례는 맨 밑에
            heapq.heappush(used,cost)
        elif used[0]<cost:
            heapq.heappop(used)
            heapq.heappush(used,cost)
    #print(used)

print(sum(used))

'''
7
1 1
2 2
2 2
3 2
3 2
5 3
5 3
=> 사용된 2 2 2 3 3으로 정답은 12
'''