'''import sys

input = sys.stdin.readline


def dfs():
    global count
    if len(s) == m + 1:
        sum = 0
        for i in s:
            if i != 0:
                sum += l[i - 1]
        if sum == ans:
            count += 1
        return
    for i in range(1, n + 1):
        if visited[i - 1] == False and s[-1] < i:
            visited[i - 1] = True
            s.append(i)
            dfs()
            s.pop()
            visited[i - 1] = False


n, ans = map(int, input().split())
l = list(map(int, input().split()))
s = [0]
visited = [False] * n
count = 0
for i in range(n):
    m = i + 1
    dfs()  # 탐색 시작
print(count)

#pypy3로 통과하지만 모범정답에 비해 4배정도 비효율적인 코드
'''

'''
#모범 정답
import sys
input = sys.stdin.readline

def dfs(idx,sum): #idx는 트리의 깊이를 나타내는 효과도 있다.
    global count
    
    if idx==n:  #idx=n-1까지만 검사하게 된다.
        return # 완전 종료

    #여기로 내려왔다는 건, idx=0부터 n-1까지만
    if sum+l[idx]==m: #하나도 안 더해서 0이 나오는 경우를 막기 위해 sum이 아니라 sum+l[idx]를 검사해준다.
        #print(s)
        count+=1
        
    #s.append(l[idx]) 
    dfs(idx+1,sum+l[idx]) #검사와 무관하게, l[idx]값을 사용한 것을 dfs하고 사용하지 않은것도 아래에서 dfs한다.

    #s.pop()
    dfs(idx+1,sum)  


n, m = map(int, input().split())
l=list(map(int,input().split()))

s=[]
count=0
dfs(0,0) #탐색 시작
print(count)
​


'''
#조합 라이브러리를 이용한 brute force 알고리즘
import sys

input = sys.stdin.readline

import itertools

n, m = map(int, input().split())

l = list(map(int, input().split()))
count = 0
for i in range(1, n + 1):
    arr = itertools.combinations(l, i)
    for j in arr:
        if sum(j) == m:
            count += 1

print(count)
