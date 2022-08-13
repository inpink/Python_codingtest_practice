import sys
input = sys.stdin.readline

def a():
    n=list(map(int,input().split()))

    if n==[1,2,3,4,5,6,7,8]:
        return 'ascending'
    elif n==[8,7,6,5,4,3,2,1]:
        return 'descending'
    else:
        return 'mixed'

print(a())
