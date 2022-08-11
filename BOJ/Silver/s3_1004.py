import sys
input = sys.stdin.readline


#(-5,1)이 1 1 8 안에 들어있는가?
#1 1 8의 가장 왼쪽 점은 (1-8) 가장 위쪽 점은 (1+8)
def find():
    x1, y1, x2, y2 = map(int, input().split())
    n=int(input())
    count=0
    for i in range(n): #n개의 행성 원 그리기
        a,b,r= map(int, input().split())
        T1=(x1-a)**2+(y1-b)**2<r**2
        T2=(x2-a)**2+(y2-b)**2<r**2
        if T1 and T2: #둘 다 안에 있으면
            continue #카운트 안해
        elif T1: #점하나만 안에 있으면
            #print(a,b,r)
            count+=1
        elif T2: #또 다른 점 하나만 안에 있으면
            #print(a,b,r)
            count+=1
    print(count)

t=int(input())

for i in range(t): #t번의 케이스
    find()