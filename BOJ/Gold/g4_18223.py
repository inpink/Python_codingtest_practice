import sys
input=sys.stdin.readline

'''
 고향으로 가는 가장 짧은 길을 찾는 것
 만약 고향으로 가는 길에 건우가 있다면 겸사겸사 도움을 줄 수 있을 것 같았다.
 양방향 그래프

  출발지는 1번 정점 마산은 V번 정점
  정점은 1~V까지 있다. 건우는 P번 정점에 있다.
   항상 1번 정점에서 P번과 V번 정점으로 갈 수 있는 경로가 존재한다.

   중복되는 간선과 자기 자신을 가리키는 간선은 존재하지 않는다.
민준이가 건우를 도와주는 경로의 길이가 최단 경로의 길이보다 길어지지 않는다면, 민준이는 반드시 건우를 도와주러 간다.
건우 구할 수 있으면  "SAVE HIM" 을 아니면 "GOOD BYE" 출력 
'''
import heapq
v,e,p=map(int,input().split())

graph=[ [] for i in range(v+1)]
for i in range(e):
    a,b,cost=map(int,input().split())
    graph[a].append((b,cost))
    graph[b].append((a,cost))

maxValue=10**9

# start부터 end까지 다익스트라 하기
heap=[]
heap.append([0,1]) #비용,시작점
costs=[maxValue for i in range(v+1)]

while True:
    if len(heap)==0:
        break
    curCost,curNode = heapq.heappop(heap)

    for nextNode, nextCost in graph[curNode]:
        sumCost=curCost+nextCost
        if sumCost<costs[nextNode]:
            costs[nextNode]=sumCost
            heapq.heappush(heap,[sumCost,nextNode])
costs[1]=0
#print(costs)

#start부터 p까지 다익스트라 : 위의 값 사용 가능 costs[p]

#p부터 end까지 다익스트라
pHeap=[]
pHeap.append([0,p]) #비용,시작점
pCosts=[maxValue for i in range(v+1)]

while True:
    if len(pHeap)==0:
        break
    curCost,curNode = heapq.heappop(pHeap)

    for nextNode, nextCost in graph[curNode]:
        sumCost=curCost+nextCost
        if sumCost<pCosts[nextNode]:
            pCosts[nextNode]=sumCost
            heapq.heappush(pHeap,[sumCost,nextNode])
pCosts[p]=0
#print(pCosts)

startToEnd=costs[v]
startToP=costs[p]
pToEnd=pCosts[v]

if startToEnd>=startToP + pToEnd:
    print("SAVE HIM")
else:
    print("GOOD BYE")