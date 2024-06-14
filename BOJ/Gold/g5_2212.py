import sys
input=sys.stdin.readline

n=int(input())
k=int(input())
sensors=list(map(int,input().split()))

sortedSensors=sorted(sensors)
#print(sortedSensors)

differences=[]
for i in range(1,n):
    differences.append(sortedSensors[i] - sortedSensors[i - 1])

invertedSortedDifferences=sorted(differences,reverse=True)
ans=sum(invertedSortedDifferences[k-1:])
#print(invertedSortedDifferences)
print(ans)
'''
고속도로 위에 N개의 센서를 설치
 
 고속도로 위에 최대 K개의 집중국을 세울 수 있다


각 집중국은 센서의 수신 가능 영역을 조절할 수 있다. 집중국의 수신 가능 영역은 고속도로 상에서 연결된 구간으로 나타나게 된다. 


. N개의 센서가 적어도 하나의 집중국과는 통신이 가능해야 하며,    
 각 집중국의 수신 가능 영역의 길이의 합을 최소화해야 한다.
 
 고속도로는 평면상의 직선  
 센서들은 이 직선 위의 한 기점인 원점으로부터의 정수 거리의 위치에 놓여 있다
각 센서의 좌표는 정수 하나로 표현된다. 

**K개의 각 집중국의 수신 가능영역의 거리의 합의 최솟값을 구하라**

집중국의 수신 가능영역의 길이는 0 이상이며 모든 센서의 좌표가 다를 필요는 없다.


센서의 개수 N(1 ≤ N ≤ 10,000)
집중국의 개수 K(1 ≤ K ≤ 1000)
N개의 센서의 좌표가 한 개의 정수로 N개 주어진다. 각 좌표 사이에는 빈 칸이 하나 있으며, 좌표의 절댓값은 1,000,000 이하
'''