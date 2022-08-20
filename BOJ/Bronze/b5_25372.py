import sys
input = sys.stdin.readline

n=int(input())
for i in range(n):
    a=input().rstrip()
    #print(a,len(a))
    if 6<=len(a)<=9:
        print("yes")
    else:
        print("no")
