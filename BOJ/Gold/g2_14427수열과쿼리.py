import heapq,sys

#힙을 이용한 풀이 방식
#어차피 제일 작은 값만을 출력하기에, heap을 쓸 수 있는 것

input = sys.stdin.readline
    
n=int(input())
l=list(map(int,input().split()))
update=list(l) #깊은 복사

for i in range(n):
    l[i]=[l[i],i+1]
    
heapq.heapify(l)

m=int(input())

for i in range(m):
    order=list(map(int,input().split()))
    if len(order)==1:
        #★heap top 정보가 최신정보랑 "같아야"함
        #=> update list에 "값"을 담아놔야 함 
        while True:
            minVal,minIdx=l[0]
            if update[minIdx-1]==minVal:
                break
            heapq.heappop(l)
            heapq.heappush(l,[update[minIdx-1],minIdx])
        print(l[0][1])
    else:
        idx=order[1]
        cng=order[2]
        update[idx-1]=cng
        heapq.heappush(l,[cng,idx])
    #print(l,update)

