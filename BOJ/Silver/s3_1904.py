import sys
input = sys.stdin.readline


n=int(input())
a=1
b=1
for i in range(n-1):
    help=a+b
    a=b%15746
    b=help%15746
print(b)
