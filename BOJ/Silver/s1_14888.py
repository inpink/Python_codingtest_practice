'''
내가 푼 코드.
pypy3만 통과된다.
정답은 잘 나오는데 시간적으로 너무 오래 걸린다.

import sys
input = sys.stdin.readline

def four(): #연산
    sum=nums[0]
    for i in range(n-1): #i=0,1
        #print("sum:",sum,s[i],nums[i+1])
        if s[i]==0:
            #print(sum,"+",nums[i+1])
            sum+=nums[i+1]
        elif s[i]==1:
            #print(sum,"-",nums[i+1])
            sum-=nums[i+1]
        elif s[i]==2:
            #print(sum,"*",nums[i+1])
            sum*=nums[i+1]

        elif s[i]==3:
            if sum<0:
                sum*=-1
                sum//=nums[i+1]
                sum*=-1
            #print(sum,"//",nums[i+1])
            else:
                sum//=nums[i+1]
    maxx.add(sum)
    return sum

#dfs는 깊이 우선 탐색. 재귀 함수로 구현한다.
def dfs():
    #탐색 종료 조건 (★하나의 dfs가 종료되는 조건)
    if len(s)==n-1:
        #print(s)
        four()
        #print()
        return

    #탐색하며 s에 담고 뺴고 하기
    for i in range(n-1): #i=0,1,2,3....
        if visited[i]==False:
            visited[i]=True #방문함
            s.append(cals[i]) #방문함
            dfs()
            #★여기로 내려왔다는 것은 case 한개가 출력되었다는 것.
            s.pop()
            visited[i]=False
            #print(i,s)
            #print()



n=int(input())
nums=list(map(int,input().split()))
a, b,c,d = map(int, input().split())
cals=[]
for i in range(a):
    cals.append(0)
for i in range(b):
    cals.append(1)
for i in range(c):
    cals.append(2)
for i in range(d):
    cals.append(3)


#print("cals:",cals)

'''
import itertools
for i in itertools.permutations(cals,n-1):
    print(i)
'''
s=[] #각 케이스를 담아줄 리스트. 1234 1243 이렇게 값이 삭제되고 담기고 하면서 진행된다
visited=[0]*(n-1) #n개만큼 F를 만들어준다. 방문한 상태면 T가 된다.

maxx=set()

dfs() #탐색 시작
#print(maxx)
print(max(maxx))
print(min(maxx))



'''


'''
아래는   각 + - * /마다 개수가 정해져 있는 것으로 최적화한 답.


import sys
input = sys.stdin.readline

#+ + - * / 를 순열로 배치하는 방법 ( 각 + - * / 마다 중복된 것이 있다)
#(이전에는 중복되지 않은 숫자 1부터 n까지만 배치했다. 이런 경우 재귀로 dfs() 코드는 한번만 쓰이지만)
#이 문제는 중복된 것이 있기 때문에, 각 + - * /마다 dfs()를 불러줘야 한다.

n=int(input())
data = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

# 최댓값과 최솟값 초기화
max_value = -1e9 #10억
min_value = 1e9

def dfs(i,sum):
    global add, sub, mul, div, max_value, min_value
    # 주어진 수열을 다 받았을 경우 최댓값과 최솟값 계산
    if i == n:
        max_value = max(max_value, sum)
        min_value = min(min_value, sum)
        #print(s)
    else:
        if add>0: #더하기 기호 개수만큼 (dfs 중 + 사용에 대한 조건이다!)
            add-=1
            s.append('+')
            dfs(i+1, sum+data[i]) #add가 먼저 있으니까, 우선 +를 가능한 만큼 우선으로 배치한다.
            #++한 다음에 나머지 3개를 dfs 하며 정하게 된다. 
            #+ 개수의 끝까지 가면(add=0) 다시 되돌아온다. (++??? 모두 생성됨)
            #+????가 되며, +-+ 부터... +로 만들 수 있는 모든 순열에 대해 하게 되겠지
            add+=1
            s.pop()
        if sub>0:
            s.append('-')
            sub-=1
            dfs(i+1, sum-data[i]) #dfs를 여러 개 적을 수 있다.
            #어차피 하나만 적어도 dfs가 여러 번 호출 되는 거다. 
            sub += 1
            s.pop()
        # 곱하기
        if mul > 0:
            s.append('*')
            mul -= 1
            dfs(i+1, sum * data[i])
            mul += 1
            s.pop()
        # 나누기
        if div > 0:
            s.append('/')
            div -= 1
            dfs(i+1, int(sum / data[i]))
            div += 1
            s.pop()

s=[]
dfs(1,data[0])


# 최댓값과 최솟값 출력
print(max_value)
print(min_value)





'''


