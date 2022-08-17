import sys
input = sys.stdin.readline

l=[1,1,1]

for i in range(3,101): #i=3~100
    l.append(l[i-3]+l[i-2])

n=int(input())

for i in range(n):
    a=int(input())
    print(l[a-1])
