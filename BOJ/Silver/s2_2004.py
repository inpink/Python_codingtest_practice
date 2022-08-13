import sys
input = sys.stdin.readline

def f(n,k):
    ans=0
    while True:
        if n==0:
            break
        n=n//k
        ans+=n
    return ans

n, m = map(int, input().split())

print(min(f(n,2)-f(n-m,2)-f(m,2),f(n,5)-f(n-m,5)-f(m,5)))
