import sys
input=sys.stdin.readline

def rev(n):
  return int(str(int(n))[::-1])

x,y=map(int,input().split())


print(rev(rev(x)+rev(y)))


'''
8:39~
X의 모든 자리수가 역순이 된 수
X=123, Rev(X)=321
X=100,Rev(X)=1 (001인데 앞에 0은 사라짐)

1000이하의 양의 정수 X, Y
Rev(Rev(X) + Rev(Y))는?

예제 1
123 100 
321, 1
Rev(322)=223


예제 2
111 111
111, 111
222
222
  
예제 3
5 5
5,5
Rev(10)
1

예제 4
1000 1
1,1
2
2

예제 5
456 789
654, 987

1641
1461
'''