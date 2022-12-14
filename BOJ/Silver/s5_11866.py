import sys

input = sys.stdin.readline

# 순서가 있다. 1개씩만 있다. 따라서, set, dic 적절치 않다. list 사용해야 함

n, k = map(int, input().split())

# 리스트 완성 [1, 2, 3, 4, 5, 6, 7]
l = []
for i in range(n):
    l.append(i + 1)
# print(l)

result = []
a = 0
for i in range(n):
    count = 0
    while True:
        # print(count,a,l)
        if l[a % n] != 0:
            a += 1
            count += 1
        else:  # 0을 만나면
            a += 1  # count는 안올라가지만 a는 올라가야 함
        if count == k:  # 3번 건너뛰면 출력하고 그만하기
            result.append(l[(a - 1) % n])
            l[(a - 1) % n] = 0
            break

print("<", end='')
for i in result:
    print(i, end='')
    if i != result[-1]:
        print(end=", ")
print(">")


#위에는 내가 푼 방법. 아래는 deque를 사용한 방법.
'''
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

from collections import deque

#덱에 전부 담아주기
deq = deque()

for i in range(1,n+1):
    deq.append(i)
#print(deq)

#출력
print('<', end='')
for i in range(n):
    deq.rotate(-(k-1)) #앞에 있는 2개를 뒤로 옮기고,
    #print(deq) 
    print(deq.popleft(), end='') #맨 앞에 있는 것을 삭제한다.
    if i!=n-1: #마지막 것만 제외하고
        print(', ', end='') #, 출력
print('>')
    

'''