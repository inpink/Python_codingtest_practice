import sys

input = sys.stdin.readline

n, k = map(int, input().split())
a=list(map(int,input().split()))
a=sorted(a, reverse=True) #리스트의 정렬은 O(nlog2(n))의 시간복잡도를 가진다.
#최악의 경우 10000*log2(10000)으로 약 13만회의 연산을 해야 한다.
#컴퓨터는 일반적으로 1초당 1억회의 연산을 할 수 있다고 생각하면,
#제한 시간인 1초에는 넉넉한 수준이다!
print(a[k-1])

