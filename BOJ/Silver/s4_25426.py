import sys
import math
input = sys.stdin.readline

n=int(input())

l=[]
k=0
sum=0
for i in range(n):
    a,b = map(int, input().split())
    l.append(a)
    k+=b #상수는 그냥 더하면 됨

l=sorted(l)
#print(l,k)

for i in range(n):
    sum=sum+l[i]*(i+1)

print(sum+k)
