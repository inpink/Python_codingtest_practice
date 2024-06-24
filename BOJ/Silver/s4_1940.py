import sys
input=sys.stdin.readline

n=int(input())
m=int(input())
numbers=list(map(int,input().split()))

numbersSet=set(numbers)
count=0
for number in numbers:
    need=m-number
    if need in numbersSet:
       count+=1

print(count//2)