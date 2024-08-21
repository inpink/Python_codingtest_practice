import math
import sys
input = sys.stdin.readline

n,m=map(int,input().split())

graph=[]
for i in range(n):
  row = list(input().strip())
  graph.append(row)

# print(graph)
ans=-1

for x in range(n):
  for y in range(m):
    for a in range(-9,10):
      for b in range(-9,10):
        if a==0 and b==0:
          continue
        number=""
        curX=x
        curY=y
        while True:
          if curX<0 or curX>=n or curY<0 or curY>=m:
            break #더 이상 탐색 불가능, 현재 있는 값이 완전 제곱수인지 판단
          number+=str(graph[curX][curY])
          curX+=a
          curY+=b

          if math.sqrt(int(number)).is_integer() and int(number)>ans:
            ans=int(number)

print(ans)

'''

123
456

n행 m열

등차수열

startX, startX+a, startX+2a,...
startY, startY+b, startY+2b,...

a,b의 범위
-9~9로 19개

모든 경우의 수 19*19=400미만

시작가능점 10x10=100

모든 탐색해야할 것 = 400*100= 40만 
시간내에 가능

즉, brute force임

'''