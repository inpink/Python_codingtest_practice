import sys
input=sys.stdin.readline

n,k=map(int,input().split())
need=n-k
baseNumber=int(input())
strBaseNumber=str(baseNumber)
length=len(strBaseNumber)

stack=[strBaseNumber[0]]

for i in range(1,length):
    if stack[-1] >= strBaseNumber[i]:
        stack.append(strBaseNumber[i])
    else:
        while True:
            if k<=0 or len(stack)==0 or stack[-1]>= strBaseNumber[i]:
                break

            k-=1
            stack.pop()
        stack.append(strBaseNumber[i])

print("".join(stack[:need]))
