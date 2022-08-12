import sys
input = sys.stdin.readline

d={}

for x in range(97,123): #소문자
	d[chr(x)]=x-96

#print(d)


n=int(input())
k=input().rstrip()

sum=0
for i in range(n):
    sum+=d[k[i]]*(31**i)
print(sum%1234567891)
#mod M은, M으로 나눈 나머지란 뜻이다!
