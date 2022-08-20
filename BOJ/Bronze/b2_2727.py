import sys
input = sys.stdin.readline

n=int(input())

a=0
b=1

for i in range(n-1):
    help=b
    b+=a
    a=help

print(b)
